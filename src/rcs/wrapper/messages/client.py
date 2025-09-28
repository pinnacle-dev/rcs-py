import os
from typing import Protocol, Dict, Any, Optional, runtime_checkable
from ...messages.client import MessagesClient, AsyncMessagesClient
from ...errors.unauthorized_error import UnauthorizedError
from ...errors.bad_request_error import BadRequestError
from ...types.error import Error
from ...types.message_event import MessageEvent
from ...core.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from .adapters import (
    NormalizedRequest,
    BaseAdapter,
    FlaskAdapter,
    DjangoAdapter,
    PyramidAdapter,
    FalconAdapter,
    BottleAdapter,
    TornadoAdapter,
    WerkzeugAdapter,
    FastAPIAdapter,
    QuartAdapter,
    AioHttpAdapter,
    SanicAdapter
)


def _validate_webhook_secret(normalized: NormalizedRequest, secret: Optional[str] = None) -> None:
    """Validate webhook signature for both sync and async clients."""
    header_secret = (
        normalized.headers.get("PINNACLE-SIGNING-SECRET") or
        normalized.headers.get("pinnacle-signing-secret")
    )
    env_secret = os.environ.get("PINNACLE_SIGNING_SECRET") or secret

    if header_secret is None:
        raise UnauthorizedError(body=Error(error="Failed to get the PINNACLE-SIGNING-SECRET header from request"))
    if env_secret is None:
        raise UnauthorizedError(body=Error(error="Make sure to set the PINNACLE-SIGNING-SECRET environment variable or pass the secret as an argument to the process method"))
    if header_secret != env_secret:
        raise UnauthorizedError(body=Error(error="Invalid webhook signature"))


class EnhancedMessages(MessagesClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    def process(self, request: Any, secret: Optional[str] = None) -> MessageEvent:
        """Process incoming webhook request from any supported framework.

        Args:
            request: The framework-specific request object (Flask, Django, etc.)
            secret: Optional webhook secret. Uses PINNACLE_SIGNING_SECRET env var if not provided.

        Returns:
            MessageEvent: The validated and parsed message event

        Raises:
            UnauthorizedError: If webhook signature is invalid or missing
            BadRequestError: If request cannot be parsed or is invalid
        """

        # Auto-detect framework and extract normalized request
        normalized = self._detect_and_extract(request)

        # Validate webhook secret
        _validate_webhook_secret(normalized, secret)

        # Create and return MessageEvent
        try:
            return MessageEvent(**normalized.body)
        except Exception as e:
            raise BadRequestError(body=Error(error=f"Invalid message event format: {str(e)}"))

    def _detect_and_extract(self, request: Any) -> NormalizedRequest:
        """Auto-detect framework and extract normalized request data."""

        # Django - check META and body attributes
        if hasattr(request, 'META') and isinstance(getattr(request, 'META', None), dict):
            if hasattr(request, 'body'):
                return DjangoAdapter.extract(request)

        # Flask/Werkzeug - check for get_json method
        if hasattr(request, 'get_json') and callable(getattr(request, 'get_json', None)):
            return FlaskAdapter.extract(request)

        # Pyramid - check for json_body attribute
        if hasattr(request, 'json_body'):
            return PyramidAdapter.extract(request)

        # Falcon - check for media attribute
        if hasattr(request, 'media'):
            return FalconAdapter.extract(request)

        # Bottle - check for json attribute (non-callable)
        if hasattr(request, 'json') and not callable(getattr(request, 'json', None)):
            return BottleAdapter.extract(request)

        # Tornado - check for headers and body
        if hasattr(request, 'headers') and hasattr(request, 'body'):
            if not hasattr(request, 'META'):  # Not Django
                return TornadoAdapter.extract(request)

        raise BadRequestError(body="Cannot extract payload from request")

class AsyncEnhancedMessages(AsyncMessagesClient):
    """Async version of MessageProcessor"""

    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    async def process(self, request: Any, secret: Optional[str] = None) -> MessageEvent:
        """Process incoming webhook request from any supported async framework.

        Args:
            request: The framework-specific request object (FastAPI, Quart, aiohttp, etc.)
            secret: Optional webhook secret. Uses PINNACLE_SIGNING_SECRET env var if not provided.

        Returns:
            MessageEvent: The validated and parsed message event

        Raises:
            UnauthorizedError: If webhook signature is invalid or missing
            BadRequestError: If request cannot be parsed or is invalid
        """

        # Auto-detect framework and extract normalized request
        normalized = await self._detect_and_extract_async(request)

        # Validate webhook secret
        _validate_webhook_secret(normalized, secret)

        # Create and return MessageEvent
        try:
            return MessageEvent(**normalized.body)
        except Exception as e:
            raise BadRequestError(body=Error(error=f"Invalid message event format: {str(e)}"))

    async def _detect_and_extract_async(self, request: Any) -> NormalizedRequest:
        """Auto-detect async framework and extract normalized request data."""

        import inspect

        # Quart - check for async get_json method
        if hasattr(request, 'get_json'):
            if inspect.iscoroutinefunction(getattr(request, 'get_json', lambda: None)):
                return await QuartAdapter.extract(request)

        # FastAPI/Starlette - check for async json method
        if hasattr(request, 'json') and hasattr(request, 'headers'):
            if inspect.iscoroutinefunction(getattr(request, 'json', lambda: None)):
                return await FastAPIAdapter.extract(request)

        # AioHttp - check for json and read methods
        if hasattr(request, 'json') and hasattr(request, 'read'):
            if inspect.iscoroutinefunction(getattr(request, 'json', lambda: None)):
                return await AioHttpAdapter.extract(request)

        # Sanic - has non-callable json attribute and body
        if hasattr(request, 'json') and hasattr(request, 'body'):
            if not callable(getattr(request, 'json', None)):
                return SanicAdapter.extract(request)

        raise BadRequestError(body="Cannot extract payload from request")