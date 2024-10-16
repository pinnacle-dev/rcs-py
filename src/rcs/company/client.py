# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.company import Company
from ..core.pydantic_utilities import parse_obj_as
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.internal_server_error import InternalServerError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.company_details import CompanyDetails
from ..types.company_contact import CompanyContact
from ..types.point_of_contact import PointOfContact
from ..types.optionals import Optionals
from .types.company_register_response import CompanyRegisterResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.company_update_response import CompanyUpdateResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        company_id: typing.Optional[int] = None,
        company_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Company]:
        """
        Retrieve the company's information (i.e. approval status, company name, etc.). Search by company ID or company name.

        Parameters
        ----------
        company_id : typing.Optional[int]
            The unique identifier for the company

        company_name : typing.Optional[str]
            The name of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Company]
            Successfully retrieved company information

        Examples
        --------
        from rcs import Pinnacle

        client = Pinnacle(
            api_key="YOUR_API_KEY",
        )
        client.company.get()
        """
        _response = self._client_wrapper.httpx_client.request(
            "company",
            method="GET",
            params={
                "companyId": company_id,
                "companyName": company_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Company],
                    parse_obj_as(
                        type_=typing.List[Company],  # type: ignore
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

    def register(
        self,
        *,
        company: CompanyDetails,
        company_contact: CompanyContact,
        point_of_contact: PointOfContact,
        optionals: typing.Optional[Optionals] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompanyRegisterResponse:
        """
        Register a company for RCS with the Pinnacle platform

        Parameters
        ----------
        company : CompanyDetails

        company_contact : CompanyContact

        point_of_contact : PointOfContact

        optionals : typing.Optional[Optionals]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyRegisterResponse
            Successfully registered/updated brand

        Examples
        --------
        from rcs import CompanyContact, CompanyDetails, Pinnacle, PointOfContact

        client = Pinnacle(
            api_key="YOUR_API_KEY",
        )
        client.company.register(
            company=CompanyDetails(
                name="name",
                address="address",
                ein="ein",
                description="description",
                brand_color="brandColor",
                logo_url="logoUrl",
                hero_url="heroUrl",
            ),
            company_contact=CompanyContact(
                primary_website_url="primaryWebsiteUrl",
                primary_website_label="primaryWebsiteLabel",
                primary_phone="primaryPhone",
                primary_phone_label="primaryPhoneLabel",
                primary_email="primaryEmail",
                primary_email_label="primaryEmailLabel",
                privacy_policy_url="privacyPolicyUrl",
                tos_url="tosUrl",
            ),
            point_of_contact=PointOfContact(
                poc_name="pocName",
                poc_title="pocTitle",
                poc_email="pocEmail",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "company/register",
            method="POST",
            json={
                "company": convert_and_respect_annotation_metadata(
                    object_=company, annotation=CompanyDetails, direction="write"
                ),
                "companyContact": convert_and_respect_annotation_metadata(
                    object_=company_contact, annotation=CompanyContact, direction="write"
                ),
                "pointOfContact": convert_and_respect_annotation_metadata(
                    object_=point_of_contact, annotation=PointOfContact, direction="write"
                ),
                "optionals": convert_and_respect_annotation_metadata(
                    object_=optionals, annotation=Optionals, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CompanyRegisterResponse,
                    parse_obj_as(
                        type_=CompanyRegisterResponse,  # type: ignore
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

    def update(
        self,
        *,
        company_id: str,
        company: typing.Optional[Company] = OMIT,
        company_contact: typing.Optional[CompanyContact] = OMIT,
        point_of_contact: typing.Optional[PointOfContact] = OMIT,
        optionals: typing.Optional[Optionals] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompanyUpdateResponse:
        """
        Update a company on the Pinnacle platform

        Parameters
        ----------
        company_id : str

        company : typing.Optional[Company]

        company_contact : typing.Optional[CompanyContact]

        point_of_contact : typing.Optional[PointOfContact]

        optionals : typing.Optional[Optionals]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyUpdateResponse
            Successfully registered/updated brand

        Examples
        --------
        from rcs import Pinnacle

        client = Pinnacle(
            api_key="YOUR_API_KEY",
        )
        client.company.update(
            company_id="companyId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "company/update",
            method="POST",
            json={
                "companyId": company_id,
                "company": convert_and_respect_annotation_metadata(
                    object_=company, annotation=Company, direction="write"
                ),
                "companyContact": convert_and_respect_annotation_metadata(
                    object_=company_contact, annotation=CompanyContact, direction="write"
                ),
                "pointOfContact": convert_and_respect_annotation_metadata(
                    object_=point_of_contact, annotation=PointOfContact, direction="write"
                ),
                "optionals": convert_and_respect_annotation_metadata(
                    object_=optionals, annotation=Optionals, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CompanyUpdateResponse,
                    parse_obj_as(
                        type_=CompanyUpdateResponse,  # type: ignore
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


class AsyncCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        company_id: typing.Optional[int] = None,
        company_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Company]:
        """
        Retrieve the company's information (i.e. approval status, company name, etc.). Search by company ID or company name.

        Parameters
        ----------
        company_id : typing.Optional[int]
            The unique identifier for the company

        company_name : typing.Optional[str]
            The name of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Company]
            Successfully retrieved company information

        Examples
        --------
        import asyncio

        from rcs import AsyncPinnacle

        client = AsyncPinnacle(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.company.get()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "company",
            method="GET",
            params={
                "companyId": company_id,
                "companyName": company_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Company],
                    parse_obj_as(
                        type_=typing.List[Company],  # type: ignore
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

    async def register(
        self,
        *,
        company: CompanyDetails,
        company_contact: CompanyContact,
        point_of_contact: PointOfContact,
        optionals: typing.Optional[Optionals] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompanyRegisterResponse:
        """
        Register a company for RCS with the Pinnacle platform

        Parameters
        ----------
        company : CompanyDetails

        company_contact : CompanyContact

        point_of_contact : PointOfContact

        optionals : typing.Optional[Optionals]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyRegisterResponse
            Successfully registered/updated brand

        Examples
        --------
        import asyncio

        from rcs import AsyncPinnacle, CompanyContact, CompanyDetails, PointOfContact

        client = AsyncPinnacle(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.company.register(
                company=CompanyDetails(
                    name="name",
                    address="address",
                    ein="ein",
                    description="description",
                    brand_color="brandColor",
                    logo_url="logoUrl",
                    hero_url="heroUrl",
                ),
                company_contact=CompanyContact(
                    primary_website_url="primaryWebsiteUrl",
                    primary_website_label="primaryWebsiteLabel",
                    primary_phone="primaryPhone",
                    primary_phone_label="primaryPhoneLabel",
                    primary_email="primaryEmail",
                    primary_email_label="primaryEmailLabel",
                    privacy_policy_url="privacyPolicyUrl",
                    tos_url="tosUrl",
                ),
                point_of_contact=PointOfContact(
                    poc_name="pocName",
                    poc_title="pocTitle",
                    poc_email="pocEmail",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "company/register",
            method="POST",
            json={
                "company": convert_and_respect_annotation_metadata(
                    object_=company, annotation=CompanyDetails, direction="write"
                ),
                "companyContact": convert_and_respect_annotation_metadata(
                    object_=company_contact, annotation=CompanyContact, direction="write"
                ),
                "pointOfContact": convert_and_respect_annotation_metadata(
                    object_=point_of_contact, annotation=PointOfContact, direction="write"
                ),
                "optionals": convert_and_respect_annotation_metadata(
                    object_=optionals, annotation=Optionals, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CompanyRegisterResponse,
                    parse_obj_as(
                        type_=CompanyRegisterResponse,  # type: ignore
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

    async def update(
        self,
        *,
        company_id: str,
        company: typing.Optional[Company] = OMIT,
        company_contact: typing.Optional[CompanyContact] = OMIT,
        point_of_contact: typing.Optional[PointOfContact] = OMIT,
        optionals: typing.Optional[Optionals] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompanyUpdateResponse:
        """
        Update a company on the Pinnacle platform

        Parameters
        ----------
        company_id : str

        company : typing.Optional[Company]

        company_contact : typing.Optional[CompanyContact]

        point_of_contact : typing.Optional[PointOfContact]

        optionals : typing.Optional[Optionals]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanyUpdateResponse
            Successfully registered/updated brand

        Examples
        --------
        import asyncio

        from rcs import AsyncPinnacle

        client = AsyncPinnacle(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.company.update(
                company_id="companyId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "company/update",
            method="POST",
            json={
                "companyId": company_id,
                "company": convert_and_respect_annotation_metadata(
                    object_=company, annotation=Company, direction="write"
                ),
                "companyContact": convert_and_respect_annotation_metadata(
                    object_=company_contact, annotation=CompanyContact, direction="write"
                ),
                "pointOfContact": convert_and_respect_annotation_metadata(
                    object_=point_of_contact, annotation=PointOfContact, direction="write"
                ),
                "optionals": convert_and_respect_annotation_metadata(
                    object_=optionals, annotation=Optionals, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CompanyUpdateResponse,
                    parse_obj_as(
                        type_=CompanyUpdateResponse,  # type: ignore
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
