import requests
from config import MAILGUN_API_KEY, MAILGUN_DOMAIN, MAILGUN_POSTMASTER

MAILGUN_BASE_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}"


def send_email(to_email, subject, content):
    response = requests.post(
        f"{MAILGUN_BASE_URL}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"Mailgun Sandbox <{MAILGUN_POSTMASTER}>",
            "to": [to_email],
            "subject": subject,
            "text": content,
        }
    )

    if response.status_code == 200:
        print("✅ Email sent successfully!")
    else:
        print(f"❌ Failed to send email: {response.status_code} {response.text}")