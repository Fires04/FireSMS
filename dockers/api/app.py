from flask import Flask, request, jsonify
import os
from datetime import datetime
import logging

app = Flask(__name__)

# Configure logging to stdout (default in Docker)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

SMS_OUTBOX_PATH = "/var/spool/gammu/outbox/"
SMS_INBOX_PATH = "/var/spool/gammu/inbox/"
SMS_ARCHIVE_PATH = "/var/spool/gammu/archive/"

# Ensure folders exist
for path in [SMS_OUTBOX_PATH, SMS_INBOX_PATH, SMS_ARCHIVE_PATH]:
    os.makedirs(path, exist_ok=True)
    app.logger.info("Ensured directory exists: %s", path)

API_TOKEN = os.getenv("API_TOKEN")

def validate_token(data):
    token = data.get("token")
    is_valid = token == API_TOKEN
    if not is_valid:
        app.logger.warning("Unauthorized access attempt with token: %s", token)
    return is_valid

@app.route("/send", methods=["POST"])
def send_sms():
    data = request.get_json()
    if not data or not validate_token(data):
        return jsonify({"error": "Invalid or missing token"}), 401

    number = data.get("number")
    message = data.get("message")

    if not number or not message:
        return jsonify({"error": "Number and message are required"}), 400

    now = datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M%S")

    sms_file = os.path.join(SMS_OUTBOX_PATH, f"OUTA{date_str}_{time_str}_1_{number}_sms.txt")
    with open(sms_file, "w") as f:
        f.write(f"{message}")

    app.logger.info("Queued SMS to %s: %s", number, message)

    return jsonify({"status": "Message queued"}), 200

@app.route("/receive", methods=["GET"])
def receive_sms():
    token = request.args.get("token")
    if token != API_TOKEN:
        app.logger.warning("Unauthorized receive attempt with token: %s", token)
        return jsonify({"error": "Invalid or missing token"}), 401

    messages = []
    for filename in os.listdir(SMS_INBOX_PATH):
        with open(os.path.join(SMS_INBOX_PATH, filename), "r") as f:
            content = f.read()
            messages.append({"filename": filename, "content": content})
            app.logger.info("Read SMS from file: %s", filename)
        # Move file to archive folder
        archive_path = os.path.join(SMS_ARCHIVE_PATH, filename)
        os.rename(filepath, archive_path)
        app.logger.info("Archived SMS file: %s", filename)

    return jsonify(messages), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
