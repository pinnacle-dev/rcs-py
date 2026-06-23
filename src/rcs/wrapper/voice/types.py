from __future__ import annotations

import typing

VoiceCommandAction = typing.Literal[
    "call.answer",
    "call.end",
    "call.transfer",
    "recording.start",
    "recording.stop",
    "audio.play",
    "audio.stop",
    "audio.reduce_noise",
    "input.get",
    "input.cancel",
    "dtmf.send",
    "call.update_state",
]

VOICE_COMMAND_ACTIONS: typing.Tuple[VoiceCommandAction, ...] = (
    "call.answer",
    "call.end",
    "call.transfer",
    "recording.start",
    "recording.stop",
    "audio.play",
    "audio.stop",
    "audio.reduce_noise",
    "input.get",
    "input.cancel",
    "dtmf.send",
    "call.update_state",
)

VoiceCallEndCause = typing.Literal["user_busy", "call_rejected"]
VoiceNoiseReductionEngine = typing.Literal["default", "krisp", "aicoustics"]
VoiceNoiseReductionDirection = typing.Literal["inbound", "outbound", "both"]
VoiceMediaTrack = typing.Literal["inbound", "outbound"]

VoiceFrame = typing.Dict[str, typing.Any]
VoiceClientFrame = VoiceFrame
VoiceCommandFrame = VoiceFrame
VoiceCommandAckFrame = VoiceFrame
VoiceServerFrame = VoiceFrame
VoiceClientMedia = typing.Dict[str, typing.Any]

