# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .additional_website import AdditionalWebsite
from ..core.serialization import FieldMetadata
import pydantic
from .additional_phone_number import AdditionalPhoneNumber
from .additional_email import AdditionalEmail
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Optionals(UniversalBaseModel):
    additional_websites: typing_extensions.Annotated[
        typing.Optional[typing.List[AdditionalWebsite]], FieldMetadata(alias="additionalWebsites")
    ] = pydantic.Field(default=None)
    """
    List of additional websites, up to 2.
    """

    additional_phone_numbers: typing_extensions.Annotated[
        typing.Optional[typing.List[AdditionalPhoneNumber]], FieldMetadata(alias="additionalPhoneNumbers")
    ] = pydantic.Field(default=None)
    """
    List of additional phone numbers, up to 2.
    """

    additional_emails: typing_extensions.Annotated[
        typing.Optional[typing.List[AdditionalEmail]], FieldMetadata(alias="additionalEmails")
    ] = pydantic.Field(default=None)
    """
    List of additional email addresses, up to 2.
    """

    test_numbers: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="testNumbers")] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow