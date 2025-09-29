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

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

# Add the src directory to the path so we can import the SDK
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rcs import Pinnacle


def test_process():
    """Run a simple server to test webhook processing."""
    try:
        from flask import Flask, request, jsonify
        from types import SimpleNamespace
    except ImportError:
        print("❌ Flask is required. Install with: pip install flask")
        sys.exit(1)

    # Initialize the SDK
    api_key = os.environ.get("PINNACLE_API_KEY")
    client = Pinnacle(api_key=api_key)
    app = Flask(__name__)

    @app.route('/webhook', methods=['POST'])
    def webhook():
        try:
            message_event = client.enhanced_messages.process({"headers": request.headers, "body": request.get_json()}) 
            print(f"\n✅ Processed webhook:")
            print(message_event)

            return jsonify({"status": "success"}), 200
        except Exception as e:
            print(f"\n❌ Error: {e}")
            return jsonify({"error": str(e)}), 400

    app.run(port=8080, debug=False)


def test_upload_from_path(file_path, custom_name=None):
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
    if custom_name:
        print(f"   Custom name: {custom_name}")
    print(f"   Size: {os.path.getsize(file_path):,} bytes")

    try:
        result = client.file_uploader.upload_from_path(
            file_path=file_path,
            name=custom_name
        )
        print(f"✅ Upload successful!")
        print(f"   Download URL: {result.download_url}")
        print(f"   Expires: {result.metadata.expires_at if result.metadata.expires_at else 'In 1 hour'}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nUsage:")
        print("  python test.py server                     # Run webhook server")
        print("  python test.py <file_path>                # Upload file")
        print("  python test.py <file_path> <custom_name>  # Upload with custom name")
        sys.exit(1)

    arg = sys.argv[1]

    if arg.lower() == "server":
        test_process()
    else:
        # Check if custom name is provided
        custom_name = sys.argv[2] if len(sys.argv) > 2 else None
        test_upload_from_path(arg, custom_name)