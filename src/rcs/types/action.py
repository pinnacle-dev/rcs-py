# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .action_type import ActionType
import typing_extensions
from ..core.serialization import FieldMetadata
from .action_lat_long import ActionLatLong
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Action(UniversalBaseModel):
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the action (must be less than 25 characters).
    """

    type: typing.Optional[ActionType] = pydantic.Field(default=None)
    """
    Type of action for the button. 'openUrl' opens a URL, 'call' dials a phone number, 'trigger' sends the predefined payload to the webhook when pressed, 'requestLocation' requests the user's location, 'scheduleEvent' creates a calendar event, 'sendLocation' sends a location.
    """

    payload: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional payload associated with the action. This payload encodes the respective fields for the action type and is required. For 'openUrl', the payload is the URL to open. For 'call', the payload is the phone number to dial. For 'trigger', the payload is the predefined payload to send to the webhook.
    """

    metadata: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional metadata. This is sent alongside the payload to the webhook.
    """

    event_start_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="eventStartTime")] = (
        pydantic.Field(default=None)
    )
    """
    Start time for events. Required for 'scheduleEvent'.
    """

    event_end_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="eventEndTime")] = (
        pydantic.Field(default=None)
    )
    """
    End time for events. Required for 'scheduleEvent'.
    """

    event_title: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="eventTitle")] = pydantic.Field(
        default=None
    )
    """
    Event title. Required for 'scheduleEvent'.
    """

    event_description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="eventDescription")] = (
        pydantic.Field(default=None)
    )
    """
    Optional event description.
    """

    lat_long: typing_extensions.Annotated[typing.Optional[ActionLatLong], FieldMetadata(alias="latLong")] = (
        pydantic.Field(default=None)
    )
    """
    Latitude and longitude coordinates. Required for 'sendLocation'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
