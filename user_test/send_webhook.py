#!/usr/bin/env python3
"""
Send a test webhook request to the running webhook server.
This simulates what Pinnacle would send to your webhook endpoint.

Usage:
    1. First start the server: python test.py server
    2. In another terminal: python send_webhook.py
"""

import sys
from pathlib import Path

# Add the src directory to the path so we can import the SDK
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

# Import types for proper typing
from rcs.types.message_event import MessageEvent
from rcs.types.message_event_conversation import MessageEventConversation
from rcs.types.message_event_message import MessageEventMessage
from rcs.types.sms_content import SmsContent


def send_webhook():
    """Send a test webhook request to the local server"""
    try:
        import requests
    except ImportError:
        print("❌ requests library required. Install with: pip install requests")
        sys.exit(1)

    # Use a test secret for webhook testing
    WEBHOOK_SECRET = "test-webhook-secret"

    # Create typed webhook payload using actual types
    webhook_event = MessageEvent(
        type="MESSAGE.RECEIVED",
        conversation=MessageEventConversation(
            id=123,
            from_="+14155551234",
            to="+14155555678"
        ),
        status="received",
        direction="inbound",
        segments=1,
        sent_at="2024-01-01T00:00:00Z",
        message=MessageEventMessage(
            id=456,
            content=SmsContent(
                text="Test message from webhook simulator"
            )
        )
    )

    # Convert to dict for sending
    try:
        webhook_data = webhook_event.model_dump()  # Pydantic v2
    except AttributeError:
        webhook_data = webhook_event.dict()  # Pydantic v1

    # Send the request
    url = "http://localhost:8080/webhook"
    headers = {
        "Content-Type": "application/json",
        "PINNACLE-SIGNING-SECRET": WEBHOOK_SECRET
    }

    try:
        response = requests.post(url, json=webhook_data, headers=headers)

        if response.status_code == 200:
            print("✅ Webhook processed successfully!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Webhook failed with status {response.status_code}")
            print(f"   Response: {response.text}")

    except requests.exceptions.ConnectionError:
        print(f"❌ Could not connect to server at {url}")
        print("   Make sure the server is running: python test.py server")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    send_webhook()