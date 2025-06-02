# Flask SMS Gateway with Gammu Integration

This project provides a lightweight HTTP API for sending and receiving SMS messages via the Gammu SMS daemon using a Flask server. It interacts with the Gammu outbox and inbox directories to queue outgoing messages and read incoming ones.

## Features

- ✅ Secure token-based authentication  
- 📤 Send SMS by writing to Gammu's outbox  
- 📥 Receive SMS by reading from Gammu's inbox  
- 📦 Docker-compatible logging to stdout  

---

## Requirements

- Python 3.7+
- Gammu (configured to monitor `/var/spool/gammu`)
- Flask

### Install dependencies

```bash
pip install flask
```

### Request
API Endpoints

#### POST /send
Queue an SMS to be sent.

Headers:
Content-Type: application/json
Request Body:
```json
{
  "token": "your_api_token",
  "number": "+1234567890",
  "message": "Hello from Flask SMS gateway!"
}
```
Response:
```json
{
  "status": "Message queued"
}
```
