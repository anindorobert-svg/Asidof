import os
from twilio.rest import Client

def send_sms(message_text):
    # Fetching secrets from your GitHub Environment
    account_sid = os.getenv('TWILIO_SID')
    auth_token = os.getenv('TWILIO_TOKEN')
    from_number = os.getenv('TWILIO_NUMBER')
    to_number = os.getenv('MY_PHONE')

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_text,
            from_=from_number,
            to=to_number
        )
        print(f"SMS Sent successfully! SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Failed to send SMS: {e}")
        return False

if __name__ == "__main__":
    # This part runs when you test it via GitHub Actions
    send_sms("ASIDOF Check: Integration successful. Monitoring WLD OBI signals now.")
