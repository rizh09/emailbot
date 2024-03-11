import os
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


# Authenticate with Gmail API
def authenticate():
    credentials = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/gmail.readonly',
                                                                              'https://www.googleapis.com/auth/gmail.send'])
    service = build('gmail', 'v1', credentials=credentials)
    return service


# Fetch unread emails from Gmail
def fetch_emails(service):
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()
    messages = results.get('messages', [])
    emails = []
    if messages:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            emails.append(msg)
    return emails


# Send reply email
def send_reply(service, email, reply_text):
    msg = create_reply_message(email, reply_text)
    raw_message = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')
    service.users().messages().send(userId='me', body={'raw': raw_message}).execute()


# Create reply message
def create_reply_message(email, reply_text):
    subject = email['subject']
    sender = email['from']
    reply = f"Dear {sender},\n\n{reply_text}"
    message = f"Subject: Re: {subject}\nTo: {sender}\n\n{reply}"
    return message


def main():
    # Authenticate and fetch unread emails
    service = authenticate()
    emails = fetch_emails(service)

    for email in emails:
        subject = email['subject']
        sender = email['from']
        print(f"Received email from {sender} with subject: {subject}")

        # Generate reply text
        reply_text = "Thank you for your email. I will get back to you soon."

        # Send reply email
        send_reply(service, email, reply_text)
        print("Reply sent successfully.")

    print("Email processing completed.")


if __name__ == '__main__':
    main()