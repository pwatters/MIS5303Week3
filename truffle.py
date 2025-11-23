"""
trufflehog_trigger.py

This file **intentionally** contains FAKE SECRETS for testing secret scanners
such as trufflehog, gitleaks, detect-secrets, etc.

DO NOT REUSE THESE VALUES IN ANY REAL SYSTEM.
"""

# --- AWS-style credentials (fake, but pattern-valid) ---

AWS_ACCESS_KEY_ID = "AKIA1234567890ABCD"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# --- GitHub Personal Access Token (fake pattern) ---

GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnoprstuvwx"

# --- Stripe live key style (fake) ---

STRIPE_SECRET_KEY = "sk_live_51JEXAMPLE1234567890abcdefghijklmn"

# --- Slack Bot Token (fake) ---

SLACK_BOT_TOKEN = "xoxb-123456789012-1234567890123-abcdefghijkl"

# --- Generic high-entropy API keys (fake) ---

GOOGLE_API_KEY = "AIzaSyA-FAKE-GOOGLE-API-KEY-1234567890abc"
INTERNAL_API_KEY = "pk_live_9a8s7d6f5g4h3j2k1l0ZyXWVUTSRQPON"

# --- JWT-like token (fake) ---

FAKE_JWT = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJ1c2VyX2lkIjoiMTIzNDU2Iiwicm9sZSI6ImFkbWluIn0."
    "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
)


def main():
    # This is just so the file is runnable and looks "normal"
    print("This file contains ONLY fake secrets for scanner testing.")
    print("AWS key:", AWS_ACCESS_KEY_ID[:8] + "...")
    print("GitHub token starts with:", GITHUB_TOKEN[:4])


if __name__ == "__main__":
    main()
