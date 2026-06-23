from __future__ import annotations

import typing

from ...calls.client import AsyncCallsClient, CallsClient
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .voice_socket import AsyncVoiceSocket, VoiceSocket, VoiceSocketLike

SocketConstructor = typing.Callable[..., VoiceSocketLike]


class EnhancedVoice:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._calls = CallsClient(client_wrapper=client_wrapper)

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
            reconnect=reconnect,
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
            reconnect=reconnect,
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
    raise RuntimeError(
        "No default WebSocket implementation is bundled. Pass socket=... to client.voice.connect(...) or "
        "client.voice.connect_stream(...)."
    )


def _new_socket(
    socket: SocketConstructor, stream_url: str, protocols: typing.Optional[typing.Union[str, typing.Sequence[str]]]
) -> VoiceSocketLike:
    if protocols is None:
        return socket(stream_url)
    return socket(stream_url, protocols)

