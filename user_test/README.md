# Test Scripts for RCS SDK

Simple test scripts to verify the `process` and `upload_from_path` methods from a user's perspective.

## Prerequisites

```bash
# Install test dependencies
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory (`rcs-py/.env`) with your credentials:
```bash
PINNACLE_API_KEY="your-api-key-here"
PINNACLE_SIGNING_SECRET="your-signing-secret-here"
```

The test scripts will automatically load environment variables from the `.env` file.

## Usage

### Sync Version (`test.py`)

#### Test webhook processing
```bash
# Start the server
python test.py server

# In another terminal, send a test webhook using the helper script
python send_webhook_test.py

# Or manually with curl
curl -X POST http://localhost:8080/webhook \
  -H 'Content-Type: application/json' \
  -H 'PINNACLE-SIGNING-SECRET: your-secret-from-env' \
  -d '{"type":"MESSAGE.RECEIVED","conversation":{"id":123,"from_":"+14155551234","to":"+14155555678"},"status":"received","direction":"inbound","segments":1,"sent_at":"2024-01-01T00:00:00Z","message":{"id":456,"content":{"text":"Test message"}}}'
```

#### Test file upload
```bash
# Upload any file
python test.py /path/to/your/file.jpg

# Upload with custom name
python test.py /path/to/your/file.jpg custom-name.jpg

# Examples
python test.py image.png
python test.py document.pdf
python test.py video.mp4 "my-video.mp4"  # Upload with custom name
python test.py ../src/rcs/client.py       # Relative path
python test.py /path/to/file.jpg          # Absolute path
```

### Async Version (`test_async.py`)

#### Test async webhook processing
```bash
# Start the async server
python test_async.py server

# In another terminal, send a test webhook using the helper script
python send_webhook_test.py

# Or manually with curl
curl -X POST http://localhost:8080/webhook \
  -H 'Content-Type: application/json' \
  -H 'PINNACLE-SIGNING-SECRET: your-secret-from-env' \
  -d '{"type":"MESSAGE.RECEIVED","conversation":{"id":123,"from_":"+14155551234","to":"+14155555678"},"status":"received","direction":"inbound","segments":1,"sent_at":"2024-01-01T00:00:00Z","message":{"id":456,"content":{"text":"Test message"}}}'
```

#### Test async file upload
```bash
# Upload any file with async client
python test_async.py /path/to/your/file.jpg

# Upload with custom name
python test_async.py /path/to/your/file.jpg custom-name.jpg

# Examples
python test_async.py image.png
python test_async.py document.pdf report.pdf
python test_async.py video.mp4 "my-video.mp4"
python test_async.py requirements.txt dependencies.txt
```

## Expected Output

### Successful webhook processing
```
✅ Processed webhook:
   Type: MESSAGE.RECEIVED
   From: +14155551234
   To: +14155555678
```

### Successful file upload
```
📁 Uploading: image.jpg
   Size: 245,678 bytes
✅ Upload successful!
   Download URL: https://storage.pinnacle.com/...
   Expires: 2024-01-15T10:30:00Z
```

### Error scenarios
```
❌ PINNACLE_API_KEY environment variable is required
❌ File not found: /path/to/missing/file.jpg
❌ Upload failed: [error details]
```

## Notes

- The webhook server requires `PINNACLE_SIGNING_SECRET` from your `.env` file for signature validation
- The `send_webhook_test.py` script sends properly typed webhook payloads to test the server
- Upload tests require a valid `PINNACLE_API_KEY` environment variable
- The server runs on port 8080 by default
- Press `Ctrl+C` to stop the server

## Files

- `test.py` - Synchronous webhook server and file upload tests
- `test_async.py` - Asynchronous webhook server and file upload tests
- `send_webhook_test.py` - Helper script to send typed webhook requests to the server
- `requirements.txt` - Python dependencies for the test scripts