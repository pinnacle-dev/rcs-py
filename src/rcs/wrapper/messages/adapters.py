import json
from typing import Dict, Any, Protocol, runtime_checkable, Union
from ...errors.bad_request_error import BadRequestError


@runtime_checkable
class FlaskRequestLike(Protocol):
    """Protocol for Flask/Werkzeug-like request objects"""
    headers: Dict[str, str]
    def get_json(self, force: bool = False) -> Dict[str, Any]: ...


@runtime_checkable
class DjangoRequestLike(Protocol):
    """Protocol for Django request objects"""
    META: Dict[str, Any]
    body: bytes


@runtime_checkable
class PyramidRequestLike(Protocol):
    """Protocol for Pyramid request objects"""
    headers: Dict[str, str]
    json_body: Dict[str, Any]


@runtime_checkable
class FalconRequestLike(Protocol):
    """Protocol for Falcon request objects"""
    headers: Dict[str, str]
    media: Dict[str, Any]


@runtime_checkable
class BottleRequestLike(Protocol):
    """Protocol for Bottle request objects"""
    headers: Dict[str, str]
    json: Dict[str, Any]


@runtime_checkable
class TornadoRequestLike(Protocol):
    """Protocol for Tornado request objects"""
    headers: Dict[str, str]
    body: bytes


@runtime_checkable
class FastAPIRequestLike(Protocol):
    """Protocol for FastAPI/Starlette request objects"""
    headers: Dict[str, str]
    async def json(self) -> Dict[str, Any]: ...


@runtime_checkable
class QuartRequestLike(Protocol):
    """Protocol for Quart request objects"""
    headers: Dict[str, str]
    async def get_json(self) -> Dict[str, Any]: ...


@runtime_checkable
class AioHttpRequestLike(Protocol):
    """Protocol for aiohttp request objects"""
    headers: Dict[str, str]
    async def json(self) -> Dict[str, Any]: ...
    async def read(self) -> bytes: ...


@runtime_checkable
class SanicRequestLike(Protocol):
    """Protocol for Sanic request objects"""
    headers: Dict[str, str]
    json: Dict[str, Any]
    body: bytes


class NormalizedRequest:
    """
    Represents a framework-agnostic, normalized request
    for your SDK to process.
    """
    def __init__(self, headers: Dict[str, str], body: Dict[str, Any]):
        self.headers = headers
        self.body = body


class BaseAdapter:
    """Provides helper methods for adapters."""

    @staticmethod
    def parse_json(raw: Union[bytes, str]) -> Dict[str, Any]:
        try:
            if isinstance(raw, bytes):
                raw = raw.decode('utf-8')
            return json.loads(raw)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            raise BadRequestError(body=f"Invalid JSON payload: {str(e)}")

    @staticmethod
    def normalize_headers(headers: Dict[str, Any]) -> Dict[str, str]:
        """Convert all headers to str key/value"""
        return {str(k): str(v) for k, v in headers.items()}


class FlaskAdapter(BaseAdapter):
    @staticmethod
    def extract(request: FlaskRequestLike) -> NormalizedRequest:
        """Extract data from Flask/Werkzeug request objects"""
        if not isinstance(request, FlaskRequestLike):
            raise ValueError(f"Invalid Flask request: expected FlaskRequestLike, got {type(request).__name__}")

        try:
            body = request.get_json(force=True)
            if body is None:
                raise ValueError("Unable to extract JSON body from Flask request")

            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=body
            )
        except Exception as e:
            raise BadRequestError(body=f"Flask adapter error: {str(e)}")


class DjangoAdapter(BaseAdapter):
    @staticmethod
    def extract(request: DjangoRequestLike) -> NormalizedRequest:
        """Extract data from Django HttpRequest objects"""
        if not isinstance(request, DjangoRequestLike):
            raise ValueError(f"Invalid Django request: expected DjangoRequestLike, got {type(request).__name__}")

        try:
            headers = {
                k[5:].replace("_", "-"): v
                for k, v in request.META.items() if k.startswith("HTTP_")
            }
            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(headers),
                body=BaseAdapter.parse_json(request.body)
            )
        except BadRequestError:
            raise
        except Exception as e:
            raise BadRequestError(body=f"Django adapter error: {str(e)}")


class PyramidAdapter(BaseAdapter):
    @staticmethod
    def extract(request: PyramidRequestLike) -> NormalizedRequest:
        """Extract data from Pyramid request objects"""
        if not isinstance(request, PyramidRequestLike):
            raise ValueError(f"Invalid Pyramid request: expected PyramidRequestLike, got {type(request).__name__}")

        try:
            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=request.json_body
            )
        except Exception as e:
            raise BadRequestError(body=f"Pyramid adapter error: {str(e)}")


class FalconAdapter(BaseAdapter):
    @staticmethod
    def extract(request: FalconRequestLike) -> NormalizedRequest:
        """Extract data from Falcon request objects"""
        if not isinstance(request, FalconRequestLike):
            raise ValueError(f"Invalid Falcon request: expected FalconRequestLike, got {type(request).__name__}")

        try:
            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=request.media
            )
        except Exception as e:
            raise BadRequestError(body=f"Falcon adapter error: {str(e)}")


class BottleAdapter(BaseAdapter):
    @staticmethod
    def extract(request: BottleRequestLike) -> NormalizedRequest:
        """Extract data from Bottle request objects"""
        if not isinstance(request, BottleRequestLike):
            raise ValueError(f"Invalid Bottle request: expected BottleRequestLike, got {type(request).__name__}")

        try:
            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=request.json
            )
        except Exception as e:
            raise BadRequestError(body=f"Bottle adapter error: {str(e)}")


class TornadoAdapter(BaseAdapter):
    @staticmethod
    def extract(request: TornadoRequestLike) -> NormalizedRequest:
        """Extract data from Tornado request objects"""
        if not isinstance(request, TornadoRequestLike):
            raise ValueError(f"Invalid Tornado request: expected TornadoRequestLike, got {type(request).__name__}")

        try:
            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=BaseAdapter.parse_json(request.body)
            )
        except BadRequestError:
            raise
        except Exception as e:
            raise BadRequestError(body=f"Tornado adapter error: {str(e)}")


class WerkzeugAdapter(BaseAdapter):
    @staticmethod
    def extract(request: FlaskRequestLike) -> NormalizedRequest:
        """Extract data from Werkzeug request objects (uses same interface as Flask)"""
        if not isinstance(request, FlaskRequestLike):
            raise ValueError(f"Invalid Werkzeug request: expected FlaskRequestLike, got {type(request).__name__}")

        try:
            body = request.get_json(force=True)
            if body is None:
                raise ValueError("Unable to extract JSON body from Werkzeug request")

            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=body
            )
        except Exception as e:
            raise BadRequestError(body=f"Werkzeug adapter error: {str(e)}")


class FastAPIAdapter(BaseAdapter):
    @staticmethod
    async def extract(request: FastAPIRequestLike) -> NormalizedRequest:
        """Extract data from FastAPI/Starlette request objects"""
        if not isinstance(request, FastAPIRequestLike):
            raise ValueError(f"Invalid FastAPI request: expected FastAPIRequestLike, got {type(request).__name__}")

        try:
            body = await request.json()
            if body is None:
                raise ValueError("Unable to extract JSON body from FastAPI request")

            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=body
            )
        except Exception as e:
            raise BadRequestError(body=f"FastAPI adapter error: {str(e)}")


class QuartAdapter(BaseAdapter):
    @staticmethod
    async def extract(request: QuartRequestLike) -> NormalizedRequest:
        """Extract data from Quart request objects"""
        if not isinstance(request, QuartRequestLike):
            raise ValueError(f"Invalid Quart request: expected QuartRequestLike, got {type(request).__name__}")

        try:
            body = await request.get_json()
            if body is None:
                raise ValueError("Unable to extract JSON body from Quart request")

            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=body
            )
        except Exception as e:
            raise BadRequestError(body=f"Quart adapter error: {str(e)}")


class AioHttpAdapter(BaseAdapter):
    @staticmethod
    async def extract(request: AioHttpRequestLike) -> NormalizedRequest:
        """Extract data from aiohttp request objects"""
        if not isinstance(request, AioHttpRequestLike):
            raise ValueError(f"Invalid aiohttp request: expected AioHttpRequestLike, got {type(request).__name__}")

        try:
            body = await request.json()
            if body is None:
                raise ValueError("Unable to extract JSON body from aiohttp request")

            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=body
            )
        except Exception as e:
            raise BadRequestError(body=f"Aiohttp adapter error: {str(e)}")


class SanicAdapter(BaseAdapter):
    @staticmethod
    def extract(request: SanicRequestLike) -> NormalizedRequest:
        """Extract data from Sanic request objects"""
        if not isinstance(request, SanicRequestLike):
            raise ValueError(f"Invalid Sanic request: expected SanicRequestLike, got {type(request).__name__}")

        try:
            if request.json is None:
                raise ValueError("Unable to extract JSON body from Sanic request")

            return NormalizedRequest(
                headers=BaseAdapter.normalize_headers(dict(request.headers)),
                body=request.json
            )
        except Exception as e:
            raise BadRequestError(body=f"Sanic adapter error: {str(e)}")