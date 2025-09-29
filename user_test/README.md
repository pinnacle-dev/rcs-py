# Test Scripts for RCS SDK

Simple test scripts to verify the `process` and `upload_from_path` methods from a user's perspective.

## Prerequisites

```bash
# Install test dependencies
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory (`rcs-py/.env`) with your API key:
```bash
PINNACLE_API_KEY="your-api-key-here"
```

The test scripts will automatically load environment variables from the `.env` file.

## Usage

### Sync Version (`test.py`)

#### Test webhook processing
```bash
# Start the server
python test.py server

# In another terminal, send a test webhook
curl -X POST http://localhost:8080/webhook \
  -H 'Content-Type: application/json' \
  -H 'PINNACLE-SIGNING-SECRET: test-secret' \
  -d '{"type":"MESSAGE.RECEIVED","conversation":{"from_":"+14155551234","to":"+14155555678"}}'
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

# In another terminal, send a test webhook
curl -X POST http://localhost:8080/webhook \
  -H 'Content-Type: application/json' \
  -H 'PINNACLE-SIGNING-SECRET: test-secret' \
  -d '{"type":"MESSAGE.RECEIVED","conversation":{"from_":"+14155551234","to":"+14155555678"}}'
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

- The webhook server uses a test secret `"test-secret"` by default
- Upload tests require a valid `PINNACLE_API_KEY` environment variable
- The server runs on port 8080 by default
- Press `Ctrl+C` to stop the server