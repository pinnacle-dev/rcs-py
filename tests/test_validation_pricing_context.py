import json

import httpx
import pytest

from rcs.client import AsyncPinnacle, Pinnacle


def response():
    return {
        "unit": 0.006,
        "total": {"gsm7": 0.006, "utf16": 0.006},
        "segments": {
            "gsm7": {"value": ["Hello"], "totalBytes": 5, "unsupported": []},
            "utf16": {"value": ["Hello"], "totalBytes": 10},
        },
        "pricingContext": {"status": "RESOLVED", "category": "SMS_10DLC", "direction": "INBOUND"},
    }


@pytest.mark.parametrize("direction", [None, "INBOUND", "OUTBOUND"])
def test_sms_context(direction):
    requests = []

    def handle(request):
        requests.append(json.loads(request.content))
        return httpx.Response(200, json=response())

    with httpx.Client(transport=httpx.MockTransport(handle)) as http:
        client = Pinnacle(api_key="test", httpx_client=http)
        args = {"text": "Hello"}
        if direction:
            args.update(sender="+14155550123", direction=direction)
        result = client.messages.sms.validate(**args)
    assert requests == [args]
    assert result.unit == 0.006
    assert result.pricing_context.status == "RESOLVED"


@pytest.mark.parametrize(
    "content", [{"text": "Hello"}, {"media": "https://example.com/img.png"}, {"cards": [{"title": "Hello"}]}]
)
def test_rcs_variants(content):
    requests = []

    def handle(request):
        requests.append(json.loads(request.content))
        return httpx.Response(200, json={"unit": 0.003, "total": 0.003, "segments": 1, "unsupportedFiles": []})

    request = dict(content, sender="agent_example", direction="INBOUND")
    with httpx.Client(transport=httpx.MockTransport(handle)) as http:
        result = Pinnacle(api_key="test", httpx_client=http).messages.rcs.validate(request=request)
    assert requests == [request]
    assert result.total == 0.003


@pytest.mark.asyncio
async def test_async_sms_context():
    requests = []

    def handle(request):
        requests.append(json.loads(request.content))
        return httpx.Response(200, json=response())

    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as http:
        result = await AsyncPinnacle(api_key="test", httpx_client=http).messages.sms.validate(
            text="Hello", sender="+14155550123", direction="INBOUND"
        )
    assert requests == [{"text": "Hello", "sender": "+14155550123", "direction": "INBOUND"}]
    assert result.unit == 0.006
