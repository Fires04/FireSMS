# FiresSMS

**FireSMS** is a Dockerized SMS Gateway built using [Gammu SMSD](https://wammu.eu/docs/manual/smsd/) and a custom API interface. It allows sending and receiving SMS messages using a GSM/USB modem connected to your server. FireSMS is ideal for IoT devices, alerting systems, or SMS-based applications.

---

## 📦 Features
- 📨 Send and receive SMS messages via a web API
- 🐳 Containerised using Docker and Docker Compose
- ⚙️ Configurable Gammu integration for different modem types
- 📁 Shared volume structure for SMS inbox/outbox
- 🔧 Simple, portable deployment

---

## 🧱 Project Structure
```
FireSMS/
├── configs/
│ ├── gammurc # Gammu configuration (device, connection)
│ └── smsdrc # SMS Daemon configuration
├── dockers/
│ ├── api/ # REST API for SMS interaction
│ └── gammu-smsd/ # Gammu SMSD container
├── docker-compose.yaml
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Fires04/FireSMS.git
cd FireSMS
```

### 2. Configure Gammu

Edit the configuration files under configs/:
gammurc – Set device path (e.g., /dev/ttyUSB0)

docker-compose.yml - Set your API token in API section

### 3. Start Services

```bash
docker-compose up --build
```
This will start:
gammu-smsd: the SMS daemon container
api: the REST API for sending and managing messages

#### 📡 Usage

Sending an SMS

POST to the API:
URL is http://yourserver:8080 (if you need to change the port, then you can edit the Docker compose file to change the port routing to the Docker container or edit the Python app under /dockers/api/app.py

```http
POST /send
Content-Type: application/json
{
  "token": "my-secret-token",
  "number": "+420123456789",
  "message": "Hello from Flask SMS gateway!"
}
```

#### Receiving SMS

The received messages will appear in the shared volume used by the api service, usually mapped from Gammu's inbox. The API will also allow read the sms by GET request.
```http://yoururl.url:8080/receive?token=my-secret-token```
The response:
```json
[
    {
        "content": "SMS one",
        "filename": "IN20250728_132555_00_+420123456789_00.txt"
    },
    {
        "content": "SMS two",
        "filename": "IN20250807_073751_00_+420123456789_00.txt"
    },
    {
        "content": "SMS three",
        "filename": "IN20250609_112118_00_+420123456789_00.txt"
    }
]
```
The messages are then automatically moved to folder /sms-data/archive/

#### 🛠️ Configuration

You may need to adjust:

USB modem device path in gammurc

Volume mounts in docker-compose.yaml

Port exposure for the API

Permissions to access serial devices (/dev/ttyUSB*)

