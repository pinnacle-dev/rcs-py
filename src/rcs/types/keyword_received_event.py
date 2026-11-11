import datetime as dt
import typing
import typing_extensions
from ..core.pydantic_utilities import UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_event import MessageEvent


class KeywordReceivedEventKeyword(UniversalBaseModel):
    value: str
    category: typing.Literal["OPT_IN", "OPT_OUT", "HELP"]
    campaign_type: typing_extensions.Annotated[typing.Literal["10DLC", "TOLL_FREE", "RCS"], FieldMetadata(alias="campaignType")]
    campaign_id: typing_extensions.Annotated[str, FieldMetadata(alias="campaignId")]


class KeywordReceivedEventConsent(UniversalBaseModel):
    status: typing.Optional[typing.Literal["OPT_IN", "OPT_OUT"]]
    applied: bool


class KeywordReceivedEventReply(UniversalBaseModel):
    status: typing.Literal["QUEUED", "SKIPPED", "ERROR"]
    message_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="messageId")]
    type: typing.Optional[typing.Literal["SMS", "MMS", "RCS_TEXT", "RCS_CARDS"]]
    text: typing.Optional[str]
    media_urls: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="mediaUrls")]
    reason: typing.Optional[typing.Literal["NO_RESPONSE_CONFIGURED", "STALE_EVENT", "REPLY_ERROR"]]


class KeywordReceivedEvent(MessageEvent):
    id: str
    type: typing.Literal["KEYWORD.RECEIVED"]
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]
    direction: typing.Literal["INBOUND"]
    status: typing.Literal["RECEIVED"]
    delivered_at: typing_extensions.Annotated[None, FieldMetadata(alias="deliveredAt")] = None
    keyword: KeywordReceivedEventKeyword
    consent: KeywordReceivedEventConsent
    reply: KeywordReceivedEventReply
