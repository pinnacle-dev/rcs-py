# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Url(UniversalBaseModel):
    action_type: typing.Literal["weburl"] = pydantic.Field(default="weburl")
    """
    The type of action being sent
    """

    title: str = pydantic.Field()
    """
    The title for the URL action. Maximum length is 25 characters.
    """

    payload: str = pydantic.Field()
    """
    The url to open. Maximum length is 1000 characters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
