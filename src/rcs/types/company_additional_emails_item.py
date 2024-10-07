# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CompanyAdditionalEmailsItem(UniversalBaseModel):
    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The additional email address
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The label for the additional email address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow