# Task 1: Email Extraction Enhancement
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Adapt the regex pattern to exclude email addresses from 'exclude.com'
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(pattern, text)

print("Valid Emails:")
for email in emails:
    print(f" - {email}")