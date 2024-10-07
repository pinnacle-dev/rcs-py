# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
import datetime as dt
from ..core.serialization import FieldMetadata
from .company_additional_websites_item import CompanyAdditionalWebsitesItem
from .company_additional_emails_item import CompanyAdditionalEmailsItem
from .company_additional_phone_numbers_item import CompanyAdditionalPhoneNumbersItem
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Company(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for the company
    """

    created_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdAt")] = (
        pydantic.Field(default=None)
    )
    """
    The date and time when the company was created
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the company
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The address of the company
    """

    ein: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Employer Identification Number (EIN) of the company
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the company
    """

    brand_color: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="brandColor")] = pydantic.Field(
        default=None
    )
    """
    The brand color of the company
    """

    logo_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="logoUrl")] = pydantic.Field(
        default=None
    )
    """
    The URL of the company's logo
    """

    hero_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="heroUrl")] = pydantic.Field(
        default=None
    )
    """
    The URL of the company's hero image
    """

    primary_website_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="primaryWebsiteUrl")] = (
        pydantic.Field(default=None)
    )
    """
    The primary website URL of the company
    """

    primary_website_label: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="primaryWebsiteLabel")
    ] = pydantic.Field(default=None)
    """
    The label for the primary website URL
    """

    primary_phone: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="primaryPhone")] = (
        pydantic.Field(default=None)
    )
    """
    The primary phone number of the company
    """

    primary_phone_label: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="primaryPhoneLabel")] = (
        pydantic.Field(default=None)
    )
    """
    The label for the primary phone number
    """

    primary_email: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="primaryEmail")] = (
        pydantic.Field(default=None)
    )
    """
    The primary email address of the company
    """

    primary_email_label: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="primaryEmailLabel")] = (
        pydantic.Field(default=None)
    )
    """
    The label for the primary email address
    """

    privacy_policy_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="privacyPolicyUrl")] = (
        pydantic.Field(default=None)
    )
    """
    The URL of the company's privacy policy
    """

    tos_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="tosUrl")] = pydantic.Field(
        default=None
    )
    """
    The URL of the company's terms of service
    """

    poc_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="pocName")] = pydantic.Field(
        default=None
    )
    """
    The name of the point of contact
    """

    poc_title: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="pocTitle")] = pydantic.Field(
        default=None
    )
    """
    The title of the point of contact
    """

    poc_email: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="pocEmail")] = pydantic.Field(
        default=None
    )
    """
    The email address of the point of contact
    """

    test_numbers: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="testNumbers")] = (
        pydantic.Field(default=None)
    )
    """
    A list of test phone numbers
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The approval status of the company
    """

    additional_websites: typing_extensions.Annotated[
        typing.Optional[typing.List[CompanyAdditionalWebsitesItem]], FieldMetadata(alias="additionalWebsites")
    ] = pydantic.Field(default=None)
    """
    A list of additional websites
    """

    additional_emails: typing_extensions.Annotated[
        typing.Optional[typing.List[CompanyAdditionalEmailsItem]], FieldMetadata(alias="additionalEmails")
    ] = pydantic.Field(default=None)
    """
    A list of additional email addresses
    """

    additional_phone_numbers: typing_extensions.Annotated[
        typing.Optional[typing.List[CompanyAdditionalPhoneNumbersItem]], FieldMetadata(alias="additionalPhoneNumbers")
    ] = pydantic.Field(default=None)
    """
    A list of additional phone numbers
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow