# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class CompanyContact(UniversalBaseModel):
    primary_website_url: typing_extensions.Annotated[str, FieldMetadata(alias="primaryWebsiteUrl")] = pydantic.Field()
    """
    Primary website URL.
    """

    primary_website_label: typing_extensions.Annotated[str, FieldMetadata(alias="primaryWebsiteLabel")] = (
        pydantic.Field()
    )
    """
    Label for the primary website.
    """

    primary_phone: typing_extensions.Annotated[str, FieldMetadata(alias="primaryPhone")] = pydantic.Field()
    """
    Primary phone number in international format.
    """

    primary_phone_label: typing_extensions.Annotated[str, FieldMetadata(alias="primaryPhoneLabel")] = pydantic.Field()
    """
    Label for the primary phone number.
    """

    primary_email: typing_extensions.Annotated[str, FieldMetadata(alias="primaryEmail")] = pydantic.Field()
    """
    Primary email address.
    """

    primary_email_label: typing_extensions.Annotated[str, FieldMetadata(alias="primaryEmailLabel")] = pydantic.Field()
    """
    Label for the primary email address.
    """

    privacy_policy_url: typing_extensions.Annotated[str, FieldMetadata(alias="privacyPolicyUrl")] = pydantic.Field()
    """
    URL of the privacy policy.
    """

    tos_url: typing_extensions.Annotated[str, FieldMetadata(alias="tosUrl")] = pydantic.Field()
    """
    URL of the terms of service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
