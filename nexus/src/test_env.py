import os
from dotenv import load_dotenv

def verify_credentials():
    """
    Loads environment variables and verifies the presence of required keys
    without printing their actual values to standard output.
    """
    load_dotenv()
    
    required_keys = [
        "TAVILY_API_KEY",
        "GROQ_API_KEY",
        "TELEGRAM_BOT_TOKEN",
        "TELEGRAM_CHAT_ID"
    ]
    
    missing_keys = []
    for key in required_keys:
        value = os.getenv(key)
        if not value or value == "PLACEHOLDER":
            missing_keys.append(key)
            
    if missing_keys:
        print(f"[SECURITY ALERT] Missing or placeholder values detected for: {', '.join(missing_keys)}")
        print("Action Required: Populate the .env file with actual credentials.")
    else:
        print("[SYSTEM VERIFIED] All required security credentials successfully loaded into memory.")

if __name__ == "__main__":
    verify_credentials()