import os
from dotenv import load_dotenv

# importing env variables
load_dotenv()

MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN")
MAILGUN_POSTMASTER = os.environ.get("MAILGUN_POSTMASTER")

print(f"MAILGUN_API_KEY: {MAILGUN_API_KEY}")
print(f"MAILGUN_DOMAIN: {MAILGUN_DOMAIN}")
print(f"MAILGUN_POSTMASTER: {MAILGUN_POSTMASTER}")
