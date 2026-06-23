import json

from rcs import CallStatusEvent, Pinnacle


def test_messages_process_call_status_event() -> None:
    client = Pinnacle(api_key="test")
    event = client.messages.process(
        {
            "headers": {"PINNACLE-SIGNING-SECRET": "secret"},
            "body": json.dumps(
                {
                    "type": "CALL.STATUS",
                    "sender": "+15551112222",
                    "call": {
                        "id": "call_123",
                        "from": "+15551112222",
                        "to": "+15551113333",
                        "direction": "OUTBOUND",
                        "status": "ANSWERED",
                    },
                }
            ),
        },
        secret="secret",
    )

    assert isinstance(event, CallStatusEvent)
    assert event.type == "CALL.STATUS"
    assert event.call.status == "ANSWERED"
