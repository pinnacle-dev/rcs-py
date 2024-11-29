# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import PinnacleEnvironment
import httpx
from .core.client_wrapper import SyncClientWrapper
from .company.client import CompanyClient
from .send.client import SendClient
from .core.request_options import RequestOptions
from .types.rcs_functionalities import RcsFunctionalities
from .core.pydantic_utilities import parse_obj_as
from .errors.bad_request_error import BadRequestError
from .errors.unauthorized_error import UnauthorizedError
from .errors.internal_server_error import InternalServerError
from json.decoder import JSONDecodeError
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper
from .company.client import AsyncCompanyClient
from .send.client import AsyncSendClient


class PinnacleBase:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : PinnacleEnvironment
        The environment to use for requests from the client. from .environment import PinnacleEnvironment



        Defaults to PinnacleEnvironment.DEFAULT



    api_key : str
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from rcs import Pinnacle

    client = Pinnacle(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: PinnacleEnvironment = PinnacleEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.company = CompanyClient(client_wrapper=self._client_wrapper)
        self.send = SendClient(client_wrapper=self._client_wrapper)

    def get_rcs_functionality(
        self, *, phone_number: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> RcsFunctionalities:
        """
        Retrieve the RCS functionality of a phone number. For example checks if a phone number can receive RCS message and if it can receive RCS carousels.

        Parameters
        ----------
        phone_number : typing.Optional[str]
            The phone number to check for RCS functionality. Should be in E.164 format (i.e. +12345678901).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RcsFunctionalities
            Successfully retrieved RCS functionality

        Examples
        --------
        from rcs import Pinnacle

        client = Pinnacle(
            api_key="YOUR_API_KEY",
        )
        client.get_rcs_functionality()
        """
        _response = self._client_wrapper.httpx_client.request(
            "rcs_functionality",
            method="GET",
            params={
                "phoneNumber": phone_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RcsFunctionalities,
                    parse_obj_as(
                        type_=RcsFunctionalities,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPinnacleBase:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : PinnacleEnvironment
        The environment to use for requests from the client. from .environment import PinnacleEnvironment



        Defaults to PinnacleEnvironment.DEFAULT



    api_key : str
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from rcs import AsyncPinnacle

    client = AsyncPinnacle(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: PinnacleEnvironment = PinnacleEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.company = AsyncCompanyClient(client_wrapper=self._client_wrapper)
        self.send = AsyncSendClient(client_wrapper=self._client_wrapper)

    async def get_rcs_functionality(
        self, *, phone_number: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> RcsFunctionalities:
        """
        Retrieve the RCS functionality of a phone number. For example checks if a phone number can receive RCS message and if it can receive RCS carousels.

        Parameters
        ----------
        phone_number : typing.Optional[str]
            The phone number to check for RCS functionality. Should be in E.164 format (i.e. +12345678901).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RcsFunctionalities
            Successfully retrieved RCS functionality

        Examples
        --------
        import asyncio

        from rcs import AsyncPinnacle

        client = AsyncPinnacle(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_rcs_functionality()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "rcs_functionality",
            method="GET",
            params={
                "phoneNumber": phone_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RcsFunctionalities,
                    parse_obj_as(
                        type_=RcsFunctionalities,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: PinnacleEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")