import base64
import json
import sys
import time
import types
from typing import Any, Callable, Dict, List, Optional

from rcs import CallStatusEvent, Pinnacle
from rcs.wrapper.voice import VOICE_COMMAND_ACTIONS, VoiceSocket


def test_messages_process_call_status_event() -> None:
    client = Pinnacle(api_key="test")
    event = client.messages.process(
        {
            "headers": {"PINNACLE-SIGNING-SECRET": "secret"},
            "body": json.dumps(
                {
                    "type": "CALL.STATUS",
                    "sender": "+15551112222",
                    "call": {
                        "id": "call_123",
                        "from": "+15551112222",
                        "to": "+15551113333",
                        "direction": "OUTBOUND",
                        "status": "ANSWERED",
                    },
                }
            ),
        },
        secret="secret",
    )

    assert isinstance(event, CallStatusEvent)
    assert event.type == "CALL.STATUS"
    assert event.call.status == "ANSWERED"


def test_exports_voice_command_constants() -> None:
    assert VOICE_COMMAND_ACTIONS == (
        "call.answer",
        "call.end",
        "call.transfer",
        "recording.start",
        "recording.stop",
        "audio.play",
        "audio.stop",
        "audio.reduce_noise",
        "input.get",
        "input.cancel",
        "dtmf.send",
        "call.update_state",
    )


def test_connects_stream_with_injected_socket() -> None:
    FakeSocket.instances = []
    client = Pinnacle(api_key="test")
    socket = client.voice.connect_stream(
        "wss://voice.example.test/stream",
        socket=FakeSocket,
        protocols="voice.v1",
    )

    assert isinstance(socket, VoiceSocket)
    assert FakeSocket.instances[-1].url == "wss://voice.example.test/stream"
    assert FakeSocket.instances[-1].protocols == "voice.v1"


def test_create_and_connect_creates_call_and_stream_token() -> None:
    FakeSocket.instances = []
    client = Pinnacle(api_key="test")
    fake_calls = FakeCalls(["wss://voice.example.test/token-1"])
    client.voice._calls = fake_calls  # type: ignore[assignment]

    socket = client.voice.create_and_connect(
        from_="+14155559876",
        to="+14155551234",
        record=True,
        metadata={"customer_id": "cus_123"},
        socket=FakeSocket,
        token={"commands_enabled": True, "stream_id": "agent", "record": True},
    )

    assert socket.call_id == "call_123"
    assert socket.call.id == "call_123"
    assert FakeSocket.instances[-1].url == "wss://voice.example.test/token-1"
    assert fake_calls.create_requests == [
        {
            "from_": "+14155559876",
            "to": "+14155551234",
            "record": True,
            "metadata": {"customer_id": "cus_123"},
            "request_options": None,
        }
    ]
    assert fake_calls.token_requests == [
        {"id": "call_123", "commands_enabled": True, "stream_id": "agent", "record": True}
    ]


def test_uses_websocket_client_as_default_socket() -> None:
    FakeWebSocketApp.instances = []
    previous = sys.modules.get("websocket")
    websocket_module = types.ModuleType("websocket")
    websocket_module.WebSocketApp = FakeWebSocketApp  # type: ignore[attr-defined]
    sys.modules["websocket"] = websocket_module
    try:
        client = Pinnacle(api_key="test")
        socket = client.voice.connect_stream("wss://voice.example.test/stream", protocols="voice.v1")
    finally:
        if previous is None:
            sys.modules.pop("websocket", None)
        else:
            sys.modules["websocket"] = previous

    payload = base64.b64encode(bytes([0xFF] * 160)).decode("ascii")
    socket.send_media({"track": "outbound", "payload": payload})

    assert isinstance(socket, VoiceSocket)
    assert FakeWebSocketApp.instances[-1].url == "wss://voice.example.test/stream"
    assert FakeWebSocketApp.instances[-1].subprotocols == ["voice.v1"]
    assert json.loads(FakeWebSocketApp.instances[-1].sent[-1]) == {
        "event": "media",
        "media": {"track": "outbound", "payload": payload},
    }


def test_serializes_command_and_media_helpers() -> None:
    fake = FakeSocket("wss://voice.example.test/stream")
    socket = VoiceSocket(fake)

    socket.answer({"as": "Agent"}, "cmd_answer")
    socket.transfer({"call_id": "call_target", "as": "Support"}, "cmd_bridge")
    socket.play_audio({"text": "Please hold", "voice": "female", "language": "en-US"}, "cmd_play")
    socket.reduce_noise({"enabled": True, "direction": "both"}, "cmd_noise")
    socket.get_input({"maxDigits": 4, "terminatingDigit": "#"}, "cmd_input")
    socket.send_dtmf({"digits": "1234#", "duration_ms": 250}, "cmd_dtmf")
    socket.update_state({"metadata": {"customer_id": "cus_123"}}, "cmd_state")
    payload = base64.b64encode(bytes([0xFF] * 160)).decode("ascii")
    socket.send_media({"track": "outbound", "payload": payload, "chunk": 7})

    assert [json.loads(payload) for payload in fake.sent] == [
        {"event": "command", "command_id": "cmd_answer", "action": "call.answer", "params": {"as": "Agent"}},
        {
            "event": "command",
            "command_id": "cmd_bridge",
            "action": "call.transfer",
            "params": {"call_id": "call_target", "as": "Support"},
        },
        {
            "event": "command",
            "command_id": "cmd_play",
            "action": "audio.play",
            "params": {"text": "Please hold", "voice": "female", "language": "en-US"},
        },
        {
            "event": "command",
            "command_id": "cmd_noise",
            "action": "audio.reduce_noise",
            "params": {"enabled": True, "direction": "both"},
        },
        {
            "event": "command",
            "command_id": "cmd_input",
            "action": "input.get",
            "params": {"maxDigits": 4, "terminatingDigit": "#"},
        },
        {
            "event": "command",
            "command_id": "cmd_dtmf",
            "action": "dtmf.send",
            "params": {"digits": "1234#", "duration_ms": 250},
        },
        {
            "event": "command",
            "command_id": "cmd_state",
            "action": "call.update_state",
            "params": {"metadata": {"customer_id": "cus_123"}},
        },
        {"event": "media", "media": {"track": "outbound", "payload": payload, "chunk": 7}},
    ]


def test_routes_server_frames_and_resolves_command_acks() -> None:
    fake = FakeSocket("wss://voice.example.test/stream")
    socket = VoiceSocket(fake)
    frames: List[Dict[str, Any]] = []
    events: List[Dict[str, Any]] = []
    media: List[Dict[str, Any]] = []

    socket.on("frame", frames.append)
    socket.on("event", events.append)
    socket.on("media", media.append)

    ack = socket.wait_for_ack("cmd_wait", timeout_ms=100)
    socket.command({"event": "command", "command_id": "cmd_wait", "action": "audio.stop"})
    fake.emit_message({"event": "connected", "stream_sid": "stream_123", "sequence_number": 0})
    fake.emit_message(
        {
            "event": "event",
            "type": "call.answered",
            "stream_sid": "stream_123",
            "sequence_number": 1,
            "payload": {"call_id": "call_123"},
        }
    )
    fake.emit_message(
        {
            "event": "media",
            "stream_sid": "stream_123",
            "sequence_number": 2,
            "media": {"track": "inbound", "payload": base64.b64encode(bytes([0xFF] * 160)).decode("ascii")},
        }
    )
    fake.emit_message({"event": "ack", "command_id": "cmd_wait", "action": "audio.stop", "status": "ok"})

    assert ack.result(timeout=1)["status"] == "ok"
    assert len(frames) == 4
    assert len(events) == 1
    assert len(media) == 1


def test_surfaces_invalid_server_frames_through_error_listener() -> None:
    fake = FakeSocket("wss://voice.example.test/stream")
    socket = VoiceSocket(fake)
    errors: List[Any] = []

    socket.on("error", errors.append)
    fake.emit_raw_message("{")

    assert isinstance(errors[0], Exception)


def test_waits_for_open_and_supports_manual_reconnect() -> None:
    FakeSocket.instances = []
    first = FakeSocket("wss://voice.example.test/first")
    first.ready_state = 0
    socket = VoiceSocket(first, create_socket=lambda: FakeSocket("wss://voice.example.test/second"))

    first.open()
    socket.wait_until_open(100)
    socket.reconnect_now()

    assert socket.socket is FakeSocket.instances[-1]
    assert FakeSocket.instances[-1].url == "wss://voice.example.test/second"


def test_auto_reconnects_fixed_stream_urls_when_enabled() -> None:
    FakeSocket.instances = []
    client = Pinnacle(api_key="test")
    socket = client.voice.connect_stream(
        "wss://voice.example.test/fixed",
        socket=FakeSocket,
        reconnect={"enabled": True, "initial_delay_ms": 1, "max_attempts": 2},
    )
    reconnected: List[Any] = []
    socket.on("reconnected", reconnected.append)

    FakeSocket.instances[0].close()
    _wait_for(lambda: len(reconnected) == 1)

    assert [instance.url for instance in FakeSocket.instances] == [
        "wss://voice.example.test/fixed",
        "wss://voice.example.test/fixed",
    ]


def test_refreshes_stream_tokens_by_default_when_reconnecting_call_streams() -> None:
    FakeSocket.instances = []
    client = Pinnacle(api_key="test")
    stream_urls = ["wss://voice.example.test/token-1", "wss://voice.example.test/token-2"]
    fake_calls = FakeCalls(stream_urls)
    client.voice._calls = fake_calls  # type: ignore[assignment]

    socket = client.voice.connect(
        call_id="call_123",
        socket=FakeSocket,
    )
    reconnected: List[Any] = []
    socket.on("reconnected", reconnected.append)

    FakeSocket.instances[0].close()
    _wait_for(lambda: len(reconnected) == 1)

    assert fake_calls.requests == ["call_123", "call_123"]
    assert [instance.url for instance in FakeSocket.instances] == stream_urls


def test_partial_reconnect_options_keep_reconnect_enabled() -> None:
    FakeSocket.instances = []
    client = Pinnacle(api_key="test")
    stream_urls = ["wss://voice.example.test/token-1", "wss://voice.example.test/token-2"]
    fake_calls = FakeCalls(stream_urls)
    client.voice._calls = fake_calls  # type: ignore[assignment]

    socket = client.voice.connect(
        call_id="call_123",
        socket=FakeSocket,
        reconnect={"initial_delay_ms": 1, "max_attempts": 2},
    )
    reconnected: List[Any] = []
    socket.on("reconnected", reconnected.append)

    FakeSocket.instances[0].close()
    _wait_for(lambda: len(reconnected) == 1)

    assert fake_calls.requests == ["call_123", "call_123"]
    assert [instance.url for instance in FakeSocket.instances] == stream_urls


def _wait_for(predicate: Callable[[], bool]) -> None:
    deadline = time.time() + 1
    while time.time() < deadline:
        if predicate():
            return
        time.sleep(0.01)
    raise AssertionError("Timed out waiting for condition.")


class FakeStreamToken:
    def __init__(self, stream_url: str):
        self.stream_url = stream_url


class FakeCall:
    def __init__(self, id: str):
        self.id = id


class FakeCalls:
    def __init__(self, stream_urls: List[str]):
        self._stream_urls = stream_urls
        self.requests: List[str] = []
        self.create_requests: List[Dict[str, Any]] = []
        self.token_requests: List[Dict[str, Any]] = []

    def create(self, **params: Any) -> FakeCall:
        self.create_requests.append(params)
        return FakeCall("call_123")

    def create_stream_token(self, id: str, **params: Any) -> FakeStreamToken:
        self.requests.append(id)
        self.token_requests.append({"id": id, **params})
        return FakeStreamToken(self._stream_urls[len(self.requests) - 1])


class FakeSocket:
    instances: List["FakeSocket"] = []

    def __init__(self, url: str, protocols: Optional[Any] = None):
        self.url = url
        self.protocols = protocols
        self.sent: List[str] = []
        self.listeners: Dict[str, List[Callable[[Any], None]]] = {}
        self.ready_state = 1
        FakeSocket.instances.append(self)

    def send(self, data: str) -> None:
        self.sent.append(data)

    def close(self, *_: Any) -> None:
        self.ready_state = 3
        self.emit("close", {})

    def open(self) -> None:
        self.ready_state = 1
        self.emit("open", {})

    def add_event_listener(self, event: str, listener: Callable[[Any], None]) -> None:
        self.listeners.setdefault(event, []).append(listener)

    def emit_message(self, frame: Dict[str, Any]) -> None:
        self.emit_raw_message(json.dumps(frame))

    def emit_raw_message(self, data: str) -> None:
        self.emit("message", {"data": data})

    def emit(self, event: str, payload: Any) -> None:
        for listener in self.listeners.get(event, []):
            listener(payload)


class FakeWebSocketApp:
    instances: List["FakeWebSocketApp"] = []

    def __init__(
        self,
        url: str,
        subprotocols: Optional[List[str]] = None,
        on_open: Optional[Callable[[Any], None]] = None,
        on_message: Optional[Callable[[Any, Any], None]] = None,
        on_error: Optional[Callable[[Any, Any], None]] = None,
        on_close: Optional[Callable[..., None]] = None,
    ):
        self.url = url
        self.subprotocols = subprotocols
        self.on_open = on_open
        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close
        self.sent: List[str] = []
        FakeWebSocketApp.instances.append(self)

    def run_forever(self) -> None:
        if self.on_open is not None:
            self.on_open(self)

    def send(self, data: str) -> None:
        self.sent.append(data)

    def close(self) -> None:
        if self.on_close is not None:
            self.on_close(self, None, None)
