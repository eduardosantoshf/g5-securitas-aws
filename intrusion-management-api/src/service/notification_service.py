import os.path
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64
from email.message import EmailMessage

SCOPES = ['https://mail.google.com/']
SENDER = 'g5securtias.ua@gmail.com'


def trigger_notification(to, camera_id):
    
    send_email(get_credentials(), to, camera_id)

def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        #print('Credentials loaded from file')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../../gmail_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            #print('Token saved to file')
    return creds
        
def send_email(creds, to, camera_id):
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()
        
        message['To'] = to
        message['From'] = SENDER
        message['Subject'] = 'Intrusion Detected - G5 Security'
        
        message.set_content(f'Hello,\n\n' \
            + f'An Intrusion have been detected on camera {camera_id}.\n\n\n' \
            + 'For more information, please visit your account on our website.\n\n\n'
            + 'Best regards,\n' \
            + 'G5 Security Team\n')

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {
            'raw': encoded_message
        }
        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
        
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
        return send_message
    
if __name__ == '__main__':
    get_credentials()