# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .phone_number import PhoneNumber
import pydantic
import typing
from .card_rcs_message import CardRcsMessage
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CardRcs(UniversalBaseModel):
    phone_number: PhoneNumber = pydantic.Field()
    """
    Phone number to send the SMS message to
    """

    message_type: typing.Literal["card"] = pydantic.Field(default="card")
    """
    The type of message being sent
    """

    message: CardRcsMessage = pydantic.Field()
    """
    The content of the message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
