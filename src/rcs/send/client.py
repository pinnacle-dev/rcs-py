# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.card import Card
from ..types.action import Action
from .types.rcs_fallback import RcsFallback
from ..core.request_options import RequestOptions
from .types.send_rcs_response import SendRcsResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.send_sms_response import SendSmsResponse
from .types.send_mms_response import SendMmsResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SendClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def rcs(
        self,
        *,
        from_: str,
        to: str,
        text: typing.Optional[str] = OMIT,
        media_url: typing.Optional[str] = OMIT,
        cards: typing.Optional[typing.Sequence[Card]] = OMIT,
        quick_replies: typing.Optional[typing.Sequence[Action]] = OMIT,
        fallback: typing.Optional[RcsFallback] = OMIT,
        status_callback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendRcsResponse:
        """
        Send an interactive RCS message with text, media, or cards. Each message can only contain either text, media, or card(s).

        Quick replies can also be added to the message.

        Parameters
        ----------
        from_ : str
            The id of the RCS agent sending the message.

            Use 'test' if you want to send from the Pinnacle test agent. The test agent can only send to whitelisted test numbers.

            See https://dashboard.trypinnacle.app/settings/test-numbers to whitelist a number.

        to : str
            The recipient's RCS-enabled phone number in E.164 format (e.g., +12345678901).

        text : typing.Optional[str]
            Text content of the message.

            Make sure you have either 'text', 'mediaUrl', or 'cards'. An error will be thrown if multiple (i.e. both 'text' and 'mediaUrl') is provided.

        media_url : typing.Optional[str]
            Media URL to be included in the message.

            Make sure you have either 'text', 'mediaUrl', or 'cards'. An error will be thrown if multiple (i.e. both 'text' and 'mediaUrl') is provided.

        cards : typing.Optional[typing.Sequence[Card]]
            List of rich cards. Maximum of 10 cards.

            Make sure you have either 'text', 'mediaUrl', or 'cards'. An error will be thrown if multiple (i.e. both 'text' and 'mediaUrl') is provided.

        quick_replies : typing.Optional[typing.Sequence[Action]]
            Optional list of quick reply actions (max 10).

        fallback : typing.Optional[RcsFallback]

        status_callback : typing.Optional[str]
            Optional URL to receive a POST request when the message status changes. Read more about status callbacks [here](/api-reference/receive-msg-statuses).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendRcsResponse
            RCS/Fallback message sent successfully

        Examples
        --------
        from rcs import Pinnacle

        client = Pinnacle(
            api_key="YOUR_API_KEY",
        )
        client.send.rcs(
            from_="from",
            to="to",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "send/rcs",
            method="POST",
            json={
                "from": from_,
                "to": to,
                "text": text,
                "mediaUrl": media_url,
                "cards": convert_and_respect_annotation_metadata(
                    object_=cards, annotation=typing.Sequence[Card], direction="write"
                ),
                "quickReplies": convert_and_respect_annotation_metadata(
                    object_=quick_replies, annotation=typing.Sequence[Action], direction="write"
                ),
                "fallback": convert_and_respect_annotation_metadata(
                    object_=fallback, annotation=RcsFallback, direction="write"
                ),
                "statusCallback": status_callback,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendRcsResponse,
                    parse_obj_as(
                        type_=SendRcsResponse,  # type: ignore
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def sms(
        self,
        *,
        to: str,
        from_: str,
        text: str,
        status_callback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendSmsResponse:
        """
        Send an SMS message to a recipient.

        Parameters
        ----------
        to : str
            The recipient's phone number in E.164 format (e.g., +12345678901).

        from_ : str
            The sender's phone number in E.164 format. Must be owned by the user.

        text : str
            The SMS message content (max 1600 characters).

        status_callback : typing.Optional[str]
            Optional URL to receive a POST request when the message status changes. Read more about status callbacks [here](/api-reference/receive-msg-statuses).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendSmsResponse
            SMS message sent successfully

        Examples
        --------
        from rcs import Pinnacle

        client = Pinnacle(
            api_key="YOUR_API_KEY",
        )
        client.send.sms(
            to="to",
            from_="from",
            text="text",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "send/sms",
            method="POST",
            json={
                "to": to,
                "from": from_,
                "text": text,
                "statusCallback": status_callback,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendSmsResponse,
                    parse_obj_as(
                        type_=SendSmsResponse,  # type: ignore
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def mms(
        self,
        *,
        to: str,
        from_: str,
        media_urls: typing.Sequence[str],
        text: typing.Optional[str] = OMIT,
        status_callback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendMmsResponse:
        """
        Send an MMS message with media attachments.

        Parameters
        ----------
        to : str
            The recipient's phone number in E.164 format (e.g., +12345678901).

        from_ : str
            The sender's phone number in E.164 format. Must be owned by the user.

        media_urls : typing.Sequence[str]
            The URLs of media to include. `jpeg`, `jpg`, `gif`, and `png` file types are fully supported and have a size limit of 5 MB. 500 KB limit for other types. Up to 10 media URLs can be included.

        text : typing.Optional[str]
            The MMS message content (max 1600 characters).

        status_callback : typing.Optional[str]
            Optional URL to receive a POST request when the message status changes. Read more about status callbacks [here](/api-reference/receive-msg-statuses).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendMmsResponse
            MMS message sent successfully

        Examples
        --------
        from rcs import Pinnacle

        client = Pinnacle(
            api_key="YOUR_API_KEY",
        )
        client.send.mms(
            to="to",
            from_="from",
            media_urls=[
                "https://example.com/image1.jpg",
                "https://example.com/video.mp4",
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "send/mms",
            method="POST",
            json={
                "to": to,
                "from": from_,
                "text": text,
                "mediaUrls": media_urls,
                "statusCallback": status_callback,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendMmsResponse,
                    parse_obj_as(
                        type_=SendMmsResponse,  # type: ignore
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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


class AsyncSendClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def rcs(
        self,
        *,
        from_: str,
        to: str,
        text: typing.Optional[str] = OMIT,
        media_url: typing.Optional[str] = OMIT,
        cards: typing.Optional[typing.Sequence[Card]] = OMIT,
        quick_replies: typing.Optional[typing.Sequence[Action]] = OMIT,
        fallback: typing.Optional[RcsFallback] = OMIT,
        status_callback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendRcsResponse:
        """
        Send an interactive RCS message with text, media, or cards. Each message can only contain either text, media, or card(s).

        Quick replies can also be added to the message.

        Parameters
        ----------
        from_ : str
            The id of the RCS agent sending the message.

            Use 'test' if you want to send from the Pinnacle test agent. The test agent can only send to whitelisted test numbers.

            See https://dashboard.trypinnacle.app/settings/test-numbers to whitelist a number.

        to : str
            The recipient's RCS-enabled phone number in E.164 format (e.g., +12345678901).

        text : typing.Optional[str]
            Text content of the message.

            Make sure you have either 'text', 'mediaUrl', or 'cards'. An error will be thrown if multiple (i.e. both 'text' and 'mediaUrl') is provided.

        media_url : typing.Optional[str]
            Media URL to be included in the message.

            Make sure you have either 'text', 'mediaUrl', or 'cards'. An error will be thrown if multiple (i.e. both 'text' and 'mediaUrl') is provided.

        cards : typing.Optional[typing.Sequence[Card]]
            List of rich cards. Maximum of 10 cards.

            Make sure you have either 'text', 'mediaUrl', or 'cards'. An error will be thrown if multiple (i.e. both 'text' and 'mediaUrl') is provided.

        quick_replies : typing.Optional[typing.Sequence[Action]]
            Optional list of quick reply actions (max 10).

        fallback : typing.Optional[RcsFallback]

        status_callback : typing.Optional[str]
            Optional URL to receive a POST request when the message status changes. Read more about status callbacks [here](/api-reference/receive-msg-statuses).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendRcsResponse
            RCS/Fallback message sent successfully

        Examples
        --------
        import asyncio

        from rcs import AsyncPinnacle

        client = AsyncPinnacle(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.send.rcs(
                from_="from",
                to="to",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "send/rcs",
            method="POST",
            json={
                "from": from_,
                "to": to,
                "text": text,
                "mediaUrl": media_url,
                "cards": convert_and_respect_annotation_metadata(
                    object_=cards, annotation=typing.Sequence[Card], direction="write"
                ),
                "quickReplies": convert_and_respect_annotation_metadata(
                    object_=quick_replies, annotation=typing.Sequence[Action], direction="write"
                ),
                "fallback": convert_and_respect_annotation_metadata(
                    object_=fallback, annotation=RcsFallback, direction="write"
                ),
                "statusCallback": status_callback,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendRcsResponse,
                    parse_obj_as(
                        type_=SendRcsResponse,  # type: ignore
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def sms(
        self,
        *,
        to: str,
        from_: str,
        text: str,
        status_callback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendSmsResponse:
        """
        Send an SMS message to a recipient.

        Parameters
        ----------
        to : str
            The recipient's phone number in E.164 format (e.g., +12345678901).

        from_ : str
            The sender's phone number in E.164 format. Must be owned by the user.

        text : str
            The SMS message content (max 1600 characters).

        status_callback : typing.Optional[str]
            Optional URL to receive a POST request when the message status changes. Read more about status callbacks [here](/api-reference/receive-msg-statuses).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendSmsResponse
            SMS message sent successfully

        Examples
        --------
        import asyncio

        from rcs import AsyncPinnacle

        client = AsyncPinnacle(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.send.sms(
                to="to",
                from_="from",
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "send/sms",
            method="POST",
            json={
                "to": to,
                "from": from_,
                "text": text,
                "statusCallback": status_callback,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendSmsResponse,
                    parse_obj_as(
                        type_=SendSmsResponse,  # type: ignore
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def mms(
        self,
        *,
        to: str,
        from_: str,
        media_urls: typing.Sequence[str],
        text: typing.Optional[str] = OMIT,
        status_callback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendMmsResponse:
        """
        Send an MMS message with media attachments.

        Parameters
        ----------
        to : str
            The recipient's phone number in E.164 format (e.g., +12345678901).

        from_ : str
            The sender's phone number in E.164 format. Must be owned by the user.

        media_urls : typing.Sequence[str]
            The URLs of media to include. `jpeg`, `jpg`, `gif`, and `png` file types are fully supported and have a size limit of 5 MB. 500 KB limit for other types. Up to 10 media URLs can be included.

        text : typing.Optional[str]
            The MMS message content (max 1600 characters).

        status_callback : typing.Optional[str]
            Optional URL to receive a POST request when the message status changes. Read more about status callbacks [here](/api-reference/receive-msg-statuses).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendMmsResponse
            MMS message sent successfully

        Examples
        --------
        import asyncio

        from rcs import AsyncPinnacle

        client = AsyncPinnacle(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.send.mms(
                to="to",
                from_="from",
                media_urls=[
                    "https://example.com/image1.jpg",
                    "https://example.com/video.mp4",
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "send/mms",
            method="POST",
            json={
                "to": to,
                "from": from_,
                "text": text,
                "mediaUrls": media_urls,
                "statusCallback": status_callback,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendMmsResponse,
                    parse_obj_as(
                        type_=SendMmsResponse,  # type: ignore
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
