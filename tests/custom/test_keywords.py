import asyncio
import json

import httpx
import pytest

from rcs import AsyncPinnacle, KeywordCategories, KeywordCategory, Pinnacle
from rcs.errors import ForbiddenError

CATEGORIES = KeywordCategories(
    opt_in=KeywordCategory(keywords=["JOIN"], response="Welcome"),
    opt_out=KeywordCategory(keywords=["LEAVE"], response="Unsubscribed"),
    help=KeywordCategory(keywords=["SUPPORT"], response="Contact support"),
)
WIRE_CATEGORIES = {
    "OPT_IN": {"keywords": ["JOIN"], "response": "Welcome"},
    "OPT_OUT": {"keywords": ["LEAVE"], "response": "Unsubscribed"},
    "HELP": {"keywords": ["SUPPORT"], "response": "Contact support"},
}
CONFIG = {
    "id": "cfg_test",
    "campaignType": "10DLC",
    "campaignId": "campaign_test",
    "sender": "+14155550101",
    "categories": WIRE_CATEGORIES,
    "createdAt": "2026-11-06T12:00:00Z",
    "updatedAt": "2026-11-06T12:00:00Z",
}


def transport(requests):
    def handle(request):
        assert request.headers["PINNACLE-API-KEY"] == "test-key"
        requests.append(request)
        path = request.url.path
        if request.method == "DELETE":
            body = {"success": True}
        elif request.method == "GET" and path in ("/keywords", "/keywords/events", "/keywords/subscriptions"):
            body = {"items": [], "total": 0, "pageIndex": 0, "pageSize": 25}
        elif path == "/keywords/effective":
            body = {**CONFIG, "configurationId": "cfg_test", "source": "SENDER"}
        else:
            body = CONFIG
        return httpx.Response(200, json=body)

    return httpx.MockTransport(handle)


def assert_requests(requests):
    assert [(r.method, r.url.path) for r in requests] == [
        ("POST", "/keywords"),
        ("GET", "/keywords/cfg_test"),
        ("PUT", "/keywords/cfg_test"),
        ("GET", "/keywords"),
        ("GET", "/keywords/subscriptions"),
        ("GET", "/keywords/events"),
        ("GET", "/keywords/effective"),
        ("DELETE", "/keywords/cfg_test"),
    ]
    assert json.loads(requests[0].content) == {
        "campaignType": "10DLC",
        "campaignId": "campaign_test",
        "sender": "+14155550101",
        "categories": WIRE_CATEGORIES,
    }
    assert json.loads(requests[2].content) == {"categories": WIRE_CATEGORIES}
    assert dict(requests[3].url.params) == {"campaignType": "10DLC", "pageIndex": "2", "pageSize": "10"}
    assert requests[4].url.params["recipient"] == "+14155550102"
    assert requests[5].url.params["sender"] == "+14155550101"
    assert requests[6].url.params["sender"] == "+14155550101"


def test_sync_keyword_operations():
    requests = []
    with httpx.Client(transport=transport(requests)) as http:
        client = Pinnacle(api_key="test-key", httpx_client=http)
        created = client.keywords.create(
            campaign_type="10DLC", campaign_id="campaign_test", sender="+14155550101", categories=CATEGORIES
        )
        assert created.id == "cfg_test"
        assert created.categories.opt_out.keywords == ["LEAVE"]
        client.keywords.get("cfg_test")
        client.keywords.update("cfg_test", categories=CATEGORIES)
        client.keywords.list(campaign_type="10DLC", page_index=2, page_size=10)
        client.keywords.list_subscriptions(recipient="+14155550102")
        client.keywords.list_events(sender="+14155550101")
        assert client.keywords.get_effective(sender="+14155550101").source == "SENDER"
        assert client.keywords.delete("cfg_test").success is True
    assert_requests(requests)


def test_async_keyword_operations():
    async def run():
        requests = []
        async with httpx.AsyncClient(transport=transport(requests)) as http:
            client = AsyncPinnacle(api_key="test-key", httpx_client=http)
            created = await client.keywords.create(
                campaign_type="10DLC", campaign_id="campaign_test", sender="+14155550101", categories=CATEGORIES
            )
            assert created.categories.opt_out.keywords == ["LEAVE"]
            await client.keywords.get("cfg_test")
            await client.keywords.update("cfg_test", categories=CATEGORIES)
            await client.keywords.list(campaign_type="10DLC", page_index=2, page_size=10)
            await client.keywords.list_subscriptions(recipient="+14155550102")
            await client.keywords.list_events(sender="+14155550101")
            await client.keywords.get_effective(sender="+14155550101")
            await client.keywords.delete("cfg_test")
        assert_requests(requests)

    asyncio.run(run())


def test_opt_out_error_retains_machine_readable_code():
    def blocked(_request):
        return httpx.Response(403, json={"error": "Recipient opted out", "code": "RECIPIENT_OPTED_OUT"})

    with httpx.Client(transport=httpx.MockTransport(blocked)) as http:
        client = Pinnacle(api_key="test-key", httpx_client=http)
        with pytest.raises(ForbiddenError) as error:
            client.messages.sms.send(from_="+14155550101", to="+14155550102", text="Hello")
        assert error.value.status_code == 403
        assert error.value.body.code == "RECIPIENT_OPTED_OUT"


def test_keyword_media_and_webhook_outcomes():
    from rcs import KeywordReceivedEvent
    from rcs.core.pydantic_utilities import parse_obj_as

    category = parse_obj_as(KeywordCategory, {
        "keywords": ["HELP"], "response": "Support", "mediaUrls": ["https://example.com/help.jpg"],
    })
    assert category.media_urls == ["https://example.com/help.jpg"]
    event = parse_obj_as(KeywordReceivedEvent, {
        "id": "kwevt_0123456789AbCdEf", "type": "KEYWORD.RECEIVED",
        "createdAt": "2026-11-10T20:00:00Z", "direction": "INBOUND", "status": "RECEIVED",
        "conversation": {"id": "conv_test", "from": "+12025550102", "to": "+12025550101"},
        "segments": 1, "sentAt": None, "deliveredAt": None,
        "message": {"id": "msg_test", "type": "SMS", "text": "HELP"},
        "keyword": {"value": "HELP", "category": "HELP", "campaignType": "10DLC", "campaignId": "dc_test"},
        "consent": {"status": None, "applied": False},
        "reply": {"status": "ERROR", "messageId": None, "type": "MMS", "text": "Support",
                  "mediaUrls": ["https://example.com/help.jpg"], "reason": "REPLY_ERROR"},
    })
    assert event.consent.applied is False
    assert event.reply.message_id is None
    assert event.reply.media_urls == category.media_urls
