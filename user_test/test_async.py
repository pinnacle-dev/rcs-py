#!/usr/bin/env python3
"""
Simple async test file for RCS SDK from user's perspective.
Usage:
  python test_async.py path/to/file.jpg  # Test async upload_from_path
  python test_async.py server            # Test async process with mock server
"""

import sys
import os
import asyncio
from pathlib import Path

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

# Add the src directory to the path so we can import the SDK
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rcs import AsyncPinnacle


async def test_process():
    """Run a simple async server to test webhook processing."""
    try:
        from fastapi import FastAPI, Request
        from fastapi.responses import JSONResponse
        import uvicorn
    except ImportError:
        print("❌ FastAPI and uvicorn are required. Install with: pip install fastapi uvicorn")
        sys.exit(1)

    # Initialize the async SDK
    api_key = os.environ.get("PINNACLE_API_KEY", "test-api-key")
    client = AsyncPinnacle(api_key=api_key)

    # Set a test secret
    os.environ["PINNACLE_SIGNING_SECRET"] = "test-secret"

    app = FastAPI()

    @app.post('/webhook')
    async def webhook(request: Request):
        try:
            message_event = await client.enhanced_messages.process(request)
            print(f"\n✅ Processed webhook:")
            print(f"   Type: {message_event.type}")
            print(f"   From: {message_event.conversation.from_}")
            print(f"   To: {message_event.conversation.to}")
            return JSONResponse({"status": "success"}, status_code=200)
        except Exception as e:
            print(f"\n❌ Error: {e}")
            return JSONResponse({"error": str(e)}, status_code=400)

    print("🚀 Async server running on http://localhost:8080/webhook")
    print("   Test with: curl -X POST http://localhost:8080/webhook \\")
    print("     -H 'Content-Type: application/json' \\")
    print("     -H 'PINNACLE-SIGNING-SECRET: test-secret' \\")
    print("     -d '{\"type\":\"MESSAGE.RECEIVED\",\"conversation\":{\"from_\":\"+14155551234\",\"to\":\"+14155555678\"}}'")
    print("\n   Press Ctrl+C to stop")

    config = uvicorn.Config(app=app, host="0.0.0.0", port=8080, log_level="error")
    server = uvicorn.Server(config)
    await server.serve()


async def test_upload_from_path(file_path, custom_name=None):
    """Test uploading a file with async client."""
    # Check API key
    api_key = os.environ.get("PINNACLE_API_KEY")
    if not api_key:
        print("❌ PINNACLE_API_KEY environment variable is required")
        sys.exit(1)

    # Initialize the async SDK
    client = AsyncPinnacle(api_key=api_key)

    # Check file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    print(f"📁 Uploading: {file_path}")
    if custom_name:
        print(f"   Custom name: {custom_name}")
    print(f"   Size: {os.path.getsize(file_path):,} bytes")

    try:
        result = await client.file_uploader.upload_from_path(
            file_path=file_path,
            name=custom_name
        )
        print(f"✅ Upload successful!")
        print(f"   Download URL: {result.download_url}")
        print(f"   Expires: {result.metadata.expires_at if result.metadata.expires_at else 'In 1 hour'}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        sys.exit(1)


async def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nUsage:")
        print("  python test_async.py server                     # Run webhook server")
        print("  python test_async.py <file_path>                # Upload file")
        print("  python test_async.py <file_path> <custom_name>  # Upload with custom name")
        sys.exit(1)

    arg = sys.argv[1]

    if arg.lower() == "server":
        await test_process()
    else:
        # Check if custom name is provided
        custom_name = sys.argv[2] if len(sys.argv) > 2 else None
        await test_upload_from_path(arg, custom_name)


if __name__ == "__main__":
    asyncio.run(main())