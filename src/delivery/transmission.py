import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    filename='nexus_ops.log',
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
)

def send_telegram_briefing(payload_state):
    """
    Robust delivery module. Markdown parsing is explicitly disabled to 
    prevent Telegram HTTP 400 rejection from unescaped LLM characters.
    """
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not bot_token or not chat_id:
        logging.error("CRITICAL: Telegram credentials missing from environment.")
        return False

    message_text = ""
    if isinstance(payload_state, dict):
        if "finalized_draft" in payload_state and payload_state["finalized_draft"]:
            message_text = payload_state["finalized_draft"]
        elif "draft" in payload_state and payload_state["draft"]:
            message_text = payload_state["draft"]
        else:
            logging.error("Transmission Node could not locate a valid draft key.")
            return False
    elif isinstance(payload_state, str):
        message_text = payload_state
        
    message_text = message_text.strip()
    if not message_text:
        logging.error("Payload is empty. Aborting transmission.")
        return False
        
    if len(message_text) > 4000:
        message_text = message_text[:4000] + "\n\n[TRUNCATED: Payload exceeded network limits]"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    # REMOVED 'parse_mode' to guarantee delivery of raw text
    request_payload = {
        "chat_id": chat_id,
        "text": message_text
    }
    
    try:
        response = requests.post(url, json=request_payload, timeout=10)
        if response.status_code == 200:
            logging.info(f"Transmission successful: HTTP {response.status_code}")
            return True
        else:
            logging.error(f"Transmission failed: HTTP {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logging.error(f"Transmission network exception: {str(e)}")
        return False