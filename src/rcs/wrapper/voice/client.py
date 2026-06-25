from __future__ import annotations

import threading
import typing

from ...calls.client import OMIT, AsyncCallsClient, CallsClient
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.call_metadata import CallMetadata
from .voice_socket import AsyncVoiceSocket, VoiceSocket, VoiceSocketLike

SocketConstructor = typing.Callable[..., VoiceSocketLike]
DEFAULT_RECONNECT = {"enabled": True}


class EnhancedVoice:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._calls = CallsClient(client_wrapper=client_wrapper)

    def create_and_connect(
        self,
        *,
        to: str,
        from_: str,
        record: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[CallMetadata] = OMIT,
        token: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        reconnect: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        socket: typing.Optional[SocketConstructor] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceSocket:
        call = self._calls.create(
            to=to,
            from_=from_,
            record=record,
            metadata=metadata,
            request_options=request_options,
        )
        connection = self.connect(
            call_id=call.id,
            token=token,
            protocols=protocols,
            reconnect=_with_default_reconnect(reconnect),
            socket=socket,
        )
        connection.call = call
        connection.call_id = call.id
        return connection

    def connect(
        self,
        *,
        call_id: str,
        token: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        reconnect: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        socket: typing.Optional[SocketConstructor] = None,
    ) -> VoiceSocket:
        Socket = socket or _get_socket_constructor()
        token_params = dict(token or {})
        stream_token = self._calls.create_stream_token(call_id, **token_params)

        def create_socket() -> VoiceSocketLike:
            next_token = self._calls.create_stream_token(call_id, **token_params)
            return _new_socket(Socket, next_token.stream_url, protocols)

        return VoiceSocket(
            _new_socket(Socket, stream_token.stream_url, protocols),
            create_socket=create_socket,
            reconnect=_with_default_reconnect(reconnect),
        )

    def connect_stream(
        self,
        stream_url: str,
        *,
        protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        reconnect: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        socket: typing.Optional[SocketConstructor] = None,
    ) -> VoiceSocket:
        Socket = socket or _get_socket_constructor()

        def create_socket() -> VoiceSocketLike:
            return _new_socket(Socket, stream_url, protocols)

        return VoiceSocket(create_socket(), create_socket=create_socket, reconnect=reconnect)


class AsyncEnhancedVoice:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._calls = AsyncCallsClient(client_wrapper=client_wrapper)

    async def create_and_connect(
        self,
        *,
        to: str,
        from_: str,
        record: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[CallMetadata] = OMIT,
        token: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        reconnect: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        socket: typing.Optional[SocketConstructor] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncVoiceSocket:
        call = await self._calls.create(
            to=to,
            from_=from_,
            record=record,
            metadata=metadata,
            request_options=request_options,
        )
        connection = await self.connect(
            call_id=call.id,
            token=token,
            protocols=protocols,
            reconnect=_with_default_reconnect(reconnect),
            socket=socket,
        )
        connection.call = call
        connection.call_id = call.id
        return connection

    async def connect(
        self,
        *,
        call_id: str,
        token: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        reconnect: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        socket: typing.Optional[SocketConstructor] = None,
    ) -> AsyncVoiceSocket:
        Socket = socket or _get_socket_constructor()
        token_params = dict(token or {})
        stream_token = await self._calls.create_stream_token(call_id, **token_params)

        async def create_socket() -> VoiceSocketLike:
            next_token = await self._calls.create_stream_token(call_id, **token_params)
            return _new_socket(Socket, next_token.stream_url, protocols)

        return AsyncVoiceSocket(
            _new_socket(Socket, stream_token.stream_url, protocols),
            create_socket=create_socket,
            reconnect=_with_default_reconnect(reconnect),
        )

    def connect_stream(
        self,
        stream_url: str,
        *,
        protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        reconnect: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        socket: typing.Optional[SocketConstructor] = None,
    ) -> AsyncVoiceSocket:
        Socket = socket or _get_socket_constructor()

        async def create_socket() -> VoiceSocketLike:
            return _new_socket(Socket, stream_url, protocols)

        return AsyncVoiceSocket(_new_socket(Socket, stream_url, protocols), create_socket=create_socket, reconnect=reconnect)


def _get_socket_constructor() -> SocketConstructor:
    try:
        import websocket  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "The rcs package could not load its websocket-client dependency. Reinstall rcs or pass socket=... to "
            "client.voice.connect(...)."
        ) from exc

    class DefaultWebSocket:
        def __init__(
            self,
            url: str,
            protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ) -> None:
            self.ready_state = 0
            self._listeners: typing.Dict[str, typing.List[typing.Callable[[typing.Any], None]]] = {}
            self._socket = websocket.WebSocketApp(
                url,
                subprotocols=_protocols_list(protocols),
                on_open=lambda _: self._open(),
                on_message=lambda _, data: self._emit("message", {"data": _decode_message(data)}),
                on_error=lambda _, error: self._emit("error", error),
                on_close=lambda *_: self._close(),
            )
            self._thread = threading.Thread(target=self._socket.run_forever, daemon=True)
            self._thread.start()

        def add_event_listener(self, event: str, listener: typing.Callable[[typing.Any], None]) -> None:
            self._listeners.setdefault(event, []).append(listener)

        def send(self, data: str) -> None:
            self._socket.send(data)

        def close(self, *_: typing.Any) -> None:
            self._socket.close()

        def _open(self) -> None:
            self.ready_state = 1
            self._emit("open", {})

        def _close(self) -> None:
            self.ready_state = 3
            self._emit("close", {})

        def _emit(self, event: str, payload: typing.Any) -> None:
            for listener in self._listeners.get(event, []):
                listener(payload)

    return DefaultWebSocket


def _protocols_list(
    protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]]
) -> typing.Optional[typing.List[str]]:
    if protocols is None:
        return None
    if isinstance(protocols, str):
        return [protocols]
    return list(protocols)


def _decode_message(data: typing.Any) -> typing.Any:
    if isinstance(data, bytes):
        return data.decode("utf-8")
    return data


def _with_default_reconnect(
    reconnect: typing.Optional[typing.Mapping[str, typing.Any]]
) -> typing.Mapping[str, typing.Any]:
    return {**DEFAULT_RECONNECT, **dict(reconnect or {})}


def _new_socket(
    socket: SocketConstructor, stream_url: str, protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]]
) -> VoiceSocketLike:
    if protocols is None:
        return socket(stream_url)
    return socket(stream_url, protocols)
