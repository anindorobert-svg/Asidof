import os
from twilio.rest import Client

# Fetching secrets from GitHub Environment
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')
my_phone = os.getenv('MY_PHONE')

def check_crypto_and_alert():
    # --- INSERT ASIDOF LOGIC HERE ---
    # Example: if price > threshold:
    
    client = Client(account_sid, auth_token)
    client.messages.create(
        body="ASIDOF Alert: BTC has hit your target! Check the charts.",
        from_='+1234567890', # Your Twilio Number
        to=my_phone
    )

if __name__ == "__main__":
    check_crypto_and_alert()