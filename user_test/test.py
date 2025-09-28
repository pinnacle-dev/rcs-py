#!/usr/bin/env python3
"""
Simple test file for RCS SDK from user's perspective.
Usage:
  python test.py path/to/file.jpg  # Test upload_from_path
  python test.py server            # Test process with mock server
"""

import sys
import os
from pathlib import Path

# Add the src directory to the path so we can import the SDK
sys.path.insert(0, str(Path(__file__).parent / "src"))

from rcs import Pinnacle


def test_process():
    """Run a simple server to test webhook processing."""
    try:
        from flask import Flask, request, jsonify
    except ImportError:
        print("❌ Flask is required. Install with: pip install flask")
        sys.exit(1)

    # Initialize the SDK
    api_key = os.environ.get("PINNACLE_API_KEY", "test-api-key")
    client = Pinnacle(api_key=api_key)

    # Set a test secret
    os.environ["PINNACLE_SIGNING_SECRET"] = "test-secret"

    app = Flask(__name__)

    @app.route('/webhook', methods=['POST'])
    def webhook():
        try:
            message_event = client.enhanced_messages.process(request)
            print(f"\n✅ Processed webhook:")
            print(f"   Type: {message_event.type}")
            print(f"   From: {message_event.conversation.from_}")
            print(f"   To: {message_event.conversation.to}")
            return jsonify({"status": "success"}), 200
        except Exception as e:
            print(f"\n❌ Error: {e}")
            return jsonify({"error": str(e)}), 400

    print("🚀 Server running on http://localhost:8080/webhook")
    print("   Test with: curl -X POST http://localhost:8080/webhook \\")
    print("     -H 'Content-Type: application/json' \\")
    print("     -H 'PINNACLE-SIGNING-SECRET: test-secret' \\")
    print("     -d '{\"type\":\"MESSAGE.RECEIVED\",\"conversation\":{\"from_\":\"+14155551234\",\"to\":\"+14155555678\"}}'")
    print("\n   Press Ctrl+C to stop")

    app.run(port=8080, debug=False)


def test_upload_from_path(file_path):
    """Test uploading a file."""
    # Check API key
    api_key = os.environ.get("PINNACLE_API_KEY")
    if not api_key:
        print("❌ PINNACLE_API_KEY environment variable is required")
        sys.exit(1)

    # Initialize the SDK
    client = Pinnacle(api_key=api_key)

    # Check file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    print(f"📁 Uploading: {file_path}")
    print(f"   Size: {os.path.getsize(file_path):,} bytes")

    try:
        result = client.file_uploader.upload_from_path(file_path=file_path)
        print(f"✅ Upload successful!")
        print(f"   URL: {result.url}")
        print(f"   Expires: {result.expires_at}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    arg = sys.argv[1]

    if arg.lower() == "server":
        test_process()
    else:
        test_upload_from_path(arg)