# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
from .inbound_message_message_type import InboundMessageMessageType
import typing
from .inbound_message_metadata import InboundMessageMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class InboundMessage(UniversalBaseModel):
    from_: typing_extensions.Annotated[str, FieldMetadata(alias="from")]
    to: str
    message_type: typing_extensions.Annotated[InboundMessageMessageType, FieldMetadata(alias="messageType")]
    metadata: typing.Optional[InboundMessageMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
