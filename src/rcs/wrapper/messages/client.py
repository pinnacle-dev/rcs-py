import os
from typing import Protocol, Dict, Any, Optional, List, Callable, Union, runtime_checkable
from ...messages.client import MessagesClient, AsyncMessagesClient
from ...errors.unauthorized_error import UnauthorizedError
from ...errors.bad_request_error import BadRequestError
from ...types.error import Error
from ...types.message_event import MessageEvent
from ...core.client_wrapper import SyncClientWrapper, AsyncClientWrapper

@runtime_checkable
class RequestLike(Protocol):
    headers: Dict[str, Union[str, List[str], None]]
    body: Any
    get: Optional[Callable[[str], Optional[str]]]
    protocol: Optional[str]
    original_url: Optional[str]


def _validate_webhook_secret(req: RequestLike, secret: Optional[str] = None) -> None:
    """Validate webhook signature for both sync and async clients."""
    header_secret = (
        req.headers.get("PINNACLE-SIGNING-SECRET") or
        req.headers.get("pinnacle-signing-secret")
    )
    env_secret = secret or os.environ.get("PINNACLE_SIGNING_SECRET")

    if header_secret is None:
        raise UnauthorizedError(body=Error(error="Failed to get the PINNACLE-SIGNING-SECRET header from request"))
    if env_secret is None:
        raise UnauthorizedError(body=Error(error="Make sure to set the PINNACLE-SIGNING-SECRET environment variable or pass the secret as an argument to the process method"))
    if header_secret != env_secret:
        raise UnauthorizedError(body=Error(error="Invalid webhook signature"))


class EnhancedMessages(MessagesClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    def process(self, req: RequestLike, secret: Optional[str] = None) -> MessageEvent:
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

        _validate_webhook_secret(req, secret)

        # Create and return MessageEvent
        try:
            return MessageEvent(**req.body)
        except Exception as e:
            raise BadRequestError(body=Error(error=f"Invalid message event format: {str(e)}"))

class AsyncEnhancedMessages(AsyncMessagesClient):
    """Async version of MessageProcessor"""

    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    async def process(self, req: RequestLike, secret: Optional[str] = None) -> MessageEvent:
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
        # Validate webhook secret
        _validate_webhook_secret(req, secret)

        # Create and return MessageEvent
        try:
            return MessageEvent(**req.body)
        except Exception as e:
            raise BadRequestError(body=Error(error=f"Invalid message event format: {str(e)}"))