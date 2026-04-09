import os
import requests
import logging

# Step 30: Configure Telemetry/Logging
# Logs are written to the root nexus_ops.log file for DevOps auditing
logging.basicConfig(
    filename='nexus_ops.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [Thread: %(threadName)s] - %(message)s'
)

def send_telegram_briefing(payload: str) -> bool:
    """
    Interfaces with the Telegram Bot API to deliver the finalized intelligence brief.
    Uses secure environment variables for authentication.
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not token or not chat_id:
        logging.error("Transmission failed: Missing Telegram credentials in environment.")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": payload,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            logging.info(f"Transmission successful: HTTP {response.status_code}")
            return True
        else:
            logging.error(f"Transmission rejected: HTTP {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logging.error(f"Transmission exception: {str(e)}")
        return False