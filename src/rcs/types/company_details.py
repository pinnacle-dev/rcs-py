# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .company_category import CompanyCategory
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class CompanyDetails(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The name of the company.
    """

    category: CompanyCategory = pydantic.Field()
    """
    The category of the company.
    """

    address: str = pydantic.Field()
    """
    The address of the company.
    """

    ein: str = pydantic.Field()
    """
    The EIN (Employer Identification Number) of the company.
    """

    description: str = pydantic.Field()
    """
    A description of the company.
    """

    brand_color: typing_extensions.Annotated[str, FieldMetadata(alias="brandColor")] = pydantic.Field()
    """
    The brand color in hex format, must pass a contrast ratio of at least 4.5:1 with white.
    """

    logo_url: typing_extensions.Annotated[str, FieldMetadata(alias="logoUrl")] = pydantic.Field()
    """
    URL of the company logo.
    """

    hero_url: typing_extensions.Annotated[str, FieldMetadata(alias="heroUrl")] = pydantic.Field()
    """
    URL of the company's hero image.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
