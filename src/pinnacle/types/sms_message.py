# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .sms_message_message import SmsMessageMessage
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SmsMessage(UniversalBaseModel):
    phone_number: str = pydantic.Field()
    """
    The recipient's phone number
    """

    message_type: typing.Literal["sms"] = pydantic.Field(default="sms")
    """
    The type of message being sent
    """

    message: SmsMessageMessage = pydantic.Field()
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
