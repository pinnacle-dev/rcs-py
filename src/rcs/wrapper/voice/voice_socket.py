from __future__ import annotations

import asyncio
import concurrent.futures
import inspect
import json
import threading
import time
import typing
import uuid

from .types import (
    VoiceClientFrame,
    VoiceClientMedia,
    VoiceCommandAckFrame,
    VoiceCommandFrame,
    VoiceServerFrame,
)

VoiceEvent = typing.Literal[
    "open",
    "close",
    "error",
    "frame",
    "ack",
    "event",
    "media",
    "reconnecting",
    "reconnected",
]

VoiceSocketLike = typing.Any
VoiceSocketFactory = typing.Callable[[], VoiceSocketLike]
AsyncVoiceSocketFactory = typing.Callable[[], typing.Awaitable[VoiceSocketLike]]


class VoiceSocket:
    def __init__(
        self,
        socket: VoiceSocketLike,
        *,
        create_socket: typing.Optional[VoiceSocketFactory] = None,
        reconnect: typing.Optional[typing.Mapping[str, typing.Any]] = None,
    ) -> None:
        self._socket = socket
        self._create_socket = create_socket
        self._reconnect = _normalize_reconnect_options(reconnect)
        self._listeners: typing.Dict[VoiceEvent, typing.List[typing.Callable[[typing.Any], None]]] = {}
        self._pending_acks: typing.Dict[str, concurrent.futures.Future[VoiceCommandAckFrame]] = {}
        self._ack_timers: typing.Dict[str, threading.Timer] = {}
        self._closed_by_user = False
        self._reconnect_attempts = 0
        self._reconnect_timer: typing.Optional[threading.Timer] = None
        self._bind_socket()

    @property
    def socket(self) -> VoiceSocketLike:
        return self._socket

    @property
    def ready_state(self) -> int:
        return int(getattr(self._socket, "ready_state", getattr(self._socket, "readyState", 0)))

    @property
    def is_open(self) -> bool:
        return self.ready_state == 1

    def wait_until_open(self, timeout_ms: int = 10_000) -> None:
        if self.is_open:
            return

        event = threading.Event()
        errors: typing.List[BaseException] = []

        def cleanup() -> None:
            off_open()
            off_close()
            off_error()

        def opened(_: typing.Any) -> None:
            cleanup()
            event.set()

        def closed(_: typing.Any) -> None:
            cleanup()
            errors.append(RuntimeError("Voice socket closed before opening."))
            event.set()

        def errored(error: typing.Any) -> None:
            cleanup()
            errors.append(_to_error(error))
            event.set()

        off_open = self.on("open", opened)
        off_close = self.on("close", closed)
        off_error = self.on("error", errored)
        if not event.wait(timeout_ms / 1000 if timeout_ms > 0 else None):
            cleanup()
            raise TimeoutError("Timed out waiting for voice socket to open.")
        if errors:
            raise errors[0]

    def connect(self) -> None:
        self.wait_until_open()

    def on(self, event: VoiceEvent, listener: typing.Callable[[typing.Any], None]) -> typing.Callable[[], None]:
        listeners = self._listeners.setdefault(event, [])
        listeners.append(listener)

        def unsubscribe() -> None:
            if listener in listeners:
                listeners.remove(listener)
            if len(listeners) == 0:
                self._listeners.pop(event, None)

        return unsubscribe

    def send(self, frame: VoiceClientFrame) -> None:
        self._socket.send(json.dumps(frame, separators=(",", ":")))

    def command(self, frame: VoiceCommandFrame) -> str:
        self.send(frame)
        return typing.cast(str, frame["command_id"])

    def command_and_wait(
        self, frame: VoiceCommandFrame, *, timeout_ms: int = 10_000
    ) -> VoiceCommandAckFrame:
        ack = self.wait_for_ack(typing.cast(str, frame["command_id"]), timeout_ms=timeout_ms)
        self.command(frame)
        try:
            return ack.result(timeout=timeout_ms / 1000 if timeout_ms > 0 else None)
        except concurrent.futures.TimeoutError as exc:
            raise TimeoutError(f"Timed out waiting for ack {frame['command_id']}.") from exc

    def answer(
        self, params: typing.Optional[typing.Mapping[str, typing.Any]] = None, command_id: typing.Optional[str] = None
    ) -> str:
        return self.command(_with_optional_params(_command_frame(command_id, "call.answer"), params))

    def end(
        self, params: typing.Optional[typing.Mapping[str, typing.Any]] = None, command_id: typing.Optional[str] = None
    ) -> str:
        return self.command(_with_optional_params(_command_frame(command_id, "call.end"), params))

    def transfer(self, params: typing.Mapping[str, typing.Any], command_id: typing.Optional[str] = None) -> str:
        return self.command(_command_frame(command_id, "call.transfer", params))

    def start_recording(self, command_id: typing.Optional[str] = None) -> str:
        return self.command(_command_frame(command_id, "recording.start"))

    def stop_recording(self, command_id: typing.Optional[str] = None) -> str:
        return self.command(_command_frame(command_id, "recording.stop"))

    def play_audio(self, params: typing.Mapping[str, typing.Any], command_id: typing.Optional[str] = None) -> str:
        return self.command(_command_frame(command_id, "audio.play", params))

    def stop_audio(self, command_id: typing.Optional[str] = None) -> str:
        return self.command(_command_frame(command_id, "audio.stop"))

    def reduce_noise(self, params: typing.Mapping[str, typing.Any], command_id: typing.Optional[str] = None) -> str:
        return self.command(_command_frame(command_id, "audio.reduce_noise", params))

    def get_input(
        self, params: typing.Optional[typing.Mapping[str, typing.Any]] = None, command_id: typing.Optional[str] = None
    ) -> str:
        return self.command(_with_optional_params(_command_frame(command_id, "input.get"), params))

    def cancel_input(self, command_id: typing.Optional[str] = None) -> str:
        return self.command(_command_frame(command_id, "input.cancel"))

    def send_dtmf(self, params: typing.Mapping[str, typing.Any], command_id: typing.Optional[str] = None) -> str:
        return self.command(_command_frame(command_id, "dtmf.send", params))

    def update_state(self, params: typing.Mapping[str, typing.Any], command_id: typing.Optional[str] = None) -> str:
        return self.command(_command_frame(command_id, "call.update_state", params))

    def send_media(self, media: VoiceClientMedia) -> None:
        self.send({"event": "media", "media": media})

    def wait_for_ack(
        self, command_id: str, *, timeout_ms: int = 10_000
    ) -> concurrent.futures.Future[VoiceCommandAckFrame]:
        if command_id in self._pending_acks:
            raise RuntimeError(f"Already waiting for ack {command_id}.")

        future: concurrent.futures.Future[VoiceCommandAckFrame] = concurrent.futures.Future()
        self._pending_acks[command_id] = future
        if timeout_ms > 0:
            timer = threading.Timer(timeout_ms / 1000, lambda: self._timeout_ack(command_id))
            timer.daemon = True
            timer.start()
            self._ack_timers[command_id] = timer
        return future

    def close(self, code: typing.Optional[int] = None, reason: typing.Optional[str] = None) -> None:
        self._closed_by_user = True
        if self._reconnect_timer is not None:
            self._reconnect_timer.cancel()
            self._reconnect_timer = None
        _close_socket(self._socket, code, reason)

    def reconnect_now(self) -> "VoiceSocket":
        if self._create_socket is None:
            raise RuntimeError("Voice socket was not configured with a reconnect factory.")
        socket = self._create_socket()
        if inspect.isawaitable(socket):
            raise RuntimeError("Use AsyncVoiceSocket for async reconnect factories.")
        self._closed_by_user = False
        self._socket = socket
        self._bind_socket()
        self._reconnect_attempts = 0
        self._emit("reconnected", socket)
        return self

    def handle_message(self, data: typing.Any) -> None:
        try:
            frame = _parse_voice_frame(data)
            self._emit("frame", frame)
            if frame.get("event") == "ack":
                self._resolve_pending_ack(typing.cast(VoiceCommandAckFrame, frame))
                self._emit("ack", frame)
            elif frame.get("event") == "event":
                self._emit("event", frame)
            elif frame.get("event") == "media":
                self._emit("media", frame)
            else:
                raise RuntimeError("Voice socket received an unknown frame event.")
        except BaseException as error:
            self._emit("error", error)

    def _bind_socket(self) -> None:
        _bind_socket_event(self._socket, "open", lambda event: self._emit("open", event))
        _bind_socket_event(self._socket, "close", self._handle_close)
        _bind_socket_event(self._socket, "error", lambda event: self._emit("error", event))
        _bind_socket_event(self._socket, "message", lambda event: self.handle_message(_message_data(event)))

    def _handle_close(self, event: typing.Any) -> None:
        self._reject_pending_acks(RuntimeError("Voice socket closed before an ack was received."))
        self._emit("close", event)
        self._schedule_reconnect()

    def _schedule_reconnect(self) -> None:
        if self._closed_by_user or not self._reconnect["enabled"] or self._create_socket is None:
            return
        if self._reconnect_timer is not None:
            return
        if self._reconnect_attempts >= self._reconnect["max_attempts"]:
            self._emit("error", RuntimeError("Voice socket reconnect attempts exhausted."))
            return

        self._reconnect_attempts += 1
        delay_ms = _get_reconnect_delay(self._reconnect, self._reconnect_attempts)
        self._emit("reconnecting", {"attempt": self._reconnect_attempts, "delay_ms": delay_ms})
        self._reconnect_timer = threading.Timer(delay_ms / 1000, self._reconnect_from_timer)
        self._reconnect_timer.daemon = True
        self._reconnect_timer.start()

    def _reconnect_from_timer(self) -> None:
        self._reconnect_timer = None
        try:
            self.reconnect_now()
        except BaseException as error:
            self._emit("error", error)
            self._schedule_reconnect()

    def _resolve_pending_ack(self, ack: VoiceCommandAckFrame) -> None:
        command_id = typing.cast(str, ack.get("command_id"))
        future = self._pending_acks.pop(command_id, None)
        timer = self._ack_timers.pop(command_id, None)
        if timer is not None:
            timer.cancel()
        if future is not None and not future.done():
            future.set_result(ack)

    def _reject_pending_acks(self, error: BaseException) -> None:
        for command_id, future in list(self._pending_acks.items()):
            self._pending_acks.pop(command_id, None)
            timer = self._ack_timers.pop(command_id, None)
            if timer is not None:
                timer.cancel()
            if not future.done():
                future.set_exception(error)

    def _timeout_ack(self, command_id: str) -> None:
        future = self._pending_acks.pop(command_id, None)
        self._ack_timers.pop(command_id, None)
        if future is not None and not future.done():
            future.set_exception(TimeoutError(f"Timed out waiting for ack {command_id}."))

    def _emit(self, event: VoiceEvent, payload: typing.Any) -> None:
        for listener in list(self._listeners.get(event, [])):
            listener(payload)


class AsyncVoiceSocket(VoiceSocket):
    def __init__(
        self,
        socket: VoiceSocketLike,
        *,
        create_socket: typing.Optional[AsyncVoiceSocketFactory] = None,
        reconnect: typing.Optional[typing.Mapping[str, typing.Any]] = None,
    ) -> None:
        self._async_create_socket = create_socket
        self._reconnect_task: typing.Optional[asyncio.Task[None]] = None
        super().__init__(socket, create_socket=None, reconnect=reconnect)

    async def wait_until_open(self, timeout_ms: int = 10_000) -> None:  # type: ignore[override]
        if self.is_open:
            return

        loop = asyncio.get_running_loop()
        future: asyncio.Future[None] = loop.create_future()

        def cleanup() -> None:
            off_open()
            off_close()
            off_error()

        def resolve() -> None:
            if not future.done():
                future.set_result(None)

        def reject(error: BaseException) -> None:
            if not future.done():
                future.set_exception(error)

        def opened(_: typing.Any) -> None:
            cleanup()
            resolve()

        def closed(_: typing.Any) -> None:
            cleanup()
            reject(RuntimeError("Voice socket closed before opening."))

        def errored(error: typing.Any) -> None:
            cleanup()
            reject(_to_error(error))

        off_open = self.on("open", opened)
        off_close = self.on("close", closed)
        off_error = self.on("error", errored)

        try:
            await asyncio.wait_for(future, timeout=timeout_ms / 1000 if timeout_ms > 0 else None)
        except asyncio.TimeoutError as exc:
            cleanup()
            raise TimeoutError("Timed out waiting for voice socket to open.") from exc

    async def connect(self) -> None:  # type: ignore[override]
        await self.wait_until_open()

    async def reconnect_now(self) -> "AsyncVoiceSocket":  # type: ignore[override]
        if self._async_create_socket is None:
            raise RuntimeError("Voice socket was not configured with a reconnect factory.")
        socket = await self._async_create_socket()
        self._closed_by_user = False
        self._socket = socket
        self._bind_socket()
        self._reconnect_attempts = 0
        self._emit("reconnected", socket)
        return self

    def _schedule_reconnect(self) -> None:
        if self._closed_by_user or not self._reconnect["enabled"] or self._async_create_socket is None:
            return
        if self._reconnect_task is not None and not self._reconnect_task.done():
            return
        if self._reconnect_attempts >= self._reconnect["max_attempts"]:
            self._emit("error", RuntimeError("Voice socket reconnect attempts exhausted."))
            return

        self._reconnect_attempts += 1
        delay_ms = _get_reconnect_delay(self._reconnect, self._reconnect_attempts)
        self._emit("reconnecting", {"attempt": self._reconnect_attempts, "delay_ms": delay_ms})
        self._reconnect_task = asyncio.create_task(self._reconnect_after_delay(delay_ms))

    async def _reconnect_after_delay(self, delay_ms: int) -> None:
        await asyncio.sleep(delay_ms / 1000)
        try:
            await self.reconnect_now()
        except BaseException as error:
            self._emit("error", error)
            self._schedule_reconnect()


def create_voice_command_id() -> str:
    return f"cmd_{uuid.uuid4()}"


def _command_frame(
    command_id: typing.Optional[str], action: str, params: typing.Optional[typing.Mapping[str, typing.Any]] = None
) -> VoiceCommandFrame:
    frame: VoiceCommandFrame = {
        "event": "command",
        "command_id": command_id or create_voice_command_id(),
        "action": action,
    }
    if params is not None:
        frame["params"] = dict(params)
    return frame


def _with_optional_params(
    frame: VoiceCommandFrame, params: typing.Optional[typing.Mapping[str, typing.Any]]
) -> VoiceCommandFrame:
    if params is not None:
        frame["params"] = dict(params)
    return frame


def _parse_voice_frame(data: typing.Any) -> VoiceServerFrame:
    if not isinstance(data, str):
        raise RuntimeError("Voice socket received a non-string frame.")
    frame = json.loads(data)
    if not isinstance(frame, dict):
        raise RuntimeError("Voice socket received a non-object frame.")
    return typing.cast(VoiceServerFrame, frame)


def _bind_socket_event(socket: VoiceSocketLike, event: str, listener: typing.Callable[[typing.Any], None]) -> None:
    if hasattr(socket, "add_event_listener"):
        socket.add_event_listener(event, listener)
    elif hasattr(socket, "addEventListener"):
        socket.addEventListener(event, listener)
    elif hasattr(socket, "on"):
        socket.on(event, listener)
    else:
        setattr(socket, f"on{event}", listener)


def _message_data(event: typing.Any) -> typing.Any:
    if isinstance(event, dict):
        return event.get("data")
    return getattr(event, "data", event)


def _close_socket(socket: VoiceSocketLike, code: typing.Optional[int], reason: typing.Optional[str]) -> None:
    close = getattr(socket, "close")
    if code is None and reason is None:
        close()
    elif reason is None:
        close(code)
    else:
        close(code, reason)


def _normalize_reconnect_options(
    options: typing.Optional[typing.Mapping[str, typing.Any]]
) -> typing.Dict[str, typing.Any]:
    options = options or {}
    return {
        "enabled": options.get("enabled", False),
        "max_attempts": options.get("max_attempts", options.get("maxAttempts", 5)),
        "initial_delay_ms": options.get("initial_delay_ms", options.get("initialDelayMs", 250)),
        "max_delay_ms": options.get("max_delay_ms", options.get("maxDelayMs", 5_000)),
        "backoff_multiplier": options.get("backoff_multiplier", options.get("backoffMultiplier", 2)),
    }


def _get_reconnect_delay(options: typing.Mapping[str, typing.Any], attempt: int) -> int:
    delay = int(options["initial_delay_ms"]) * float(options["backoff_multiplier"]) ** max(0, attempt - 1)
    return int(min(delay, int(options["max_delay_ms"])))


def _to_error(error: typing.Any) -> BaseException:
    return error if isinstance(error, BaseException) else RuntimeError("Voice socket error.")
