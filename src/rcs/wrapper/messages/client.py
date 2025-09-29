import os
from typing import Dict, Any, Optional, List, Union
import json
from dataclasses import dataclass
from ...messages.client import MessagesClient, AsyncMessagesClient
from ...errors.unauthorized_error import UnauthorizedError
from ...errors.bad_request_error import BadRequestError
from ...types.error import Error
from ...types.message_event import MessageEvent
from ...core.client_wrapper import SyncClientWrapper, AsyncClientWrapper

@dataclass
class NormalizedRequest:
    headers: Dict[str, Union[str, List[str], None]]
    body: Any

def _validate_webhook_secret(req: NormalizedRequest, secret: Optional[str] = None) -> None:
    """Validate webhook signature for both sync and async clients."""
    header_secret = (
        req.headers.get("PINNACLE-SIGNING-SECRET") or
        req.headers.get("pinnacle-signing-secret")
    )

    env_secret = secret or os.environ.get("PINNACLE_SIGNING_SECRET")
    print(env_secret)
    if header_secret is None:
        raise UnauthorizedError(body=Error(error="Failed to get the PINNACLE-SIGNING-SECRET header from request"))
    if env_secret is None:
        raise UnauthorizedError(body=Error(error="Make sure to set the PINNACLE-SIGNING-SECRET environment variable or pass the secret as an argument to the process method"))
    if header_secret != env_secret:
        raise UnauthorizedError(body=Error(error="Invalid webhook signature"))

def normalize(req: Dict[str, Any]) -> NormalizedRequest:
    if "headers" not in req or "body" not in req:
        raise BadRequestError(
            body="Request must contain 'headers' and 'body'."
        )
    
    body = req["body"]
    # if body is bytes (e.g., from await request.body()), decode it
    if isinstance(body, bytes):
        try:
            body = json.loads(body)
        except (json.JSONDecodeError, TypeError):
            body = body.decode("utf-8")

    return NormalizedRequest(headers=req["headers"], body=req["body"])
    

class EnhancedMessages(MessagesClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
    
    def process(self, req: Dict[str, Any], secret: Optional[str] = None) -> MessageEvent:
        """Process incoming webhook request from any supported framework.

        Args:
            request: The framework-specific request object (Flask, Django, etc.), or dict formatted as {"header":..., "body":...}
            secret: Optional webhook secret. Uses PINNACLE_SIGNING_SECRET env var if not provided.

        Returns:
            MessageEvent: The validated and parsed message event

        Raises:
            UnauthorizedError: If webhook signature is invalid or missing
            BadRequestError: If request cannot be parsed or is invalid
        """

        normalized_req = normalize(req)
        
        _validate_webhook_secret(normalized_req, secret)

        # Create and return MessageEvent
        try:
            return MessageEvent(**normalized_req.body)
        except Exception as e:
            raise BadRequestError(body=f"Invalid message event format: {str(e)}")

class AsyncEnhancedMessages(AsyncMessagesClient):
    """Async version of MessageProcessor"""

    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    async def process(self, req: Dict[str, Any], secret: Optional[str] = None) -> MessageEvent:
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

        normalized_req = normalize(req)
        
        _validate_webhook_secret(normalized_req, secret)

        # Create and return MessageEvent
        try:
            return MessageEvent(**normalized_req.body)
        except Exception as e:
            raise BadRequestError(body=Error(error=f"Invalid message event format: {str(e)}"))