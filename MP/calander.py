from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def insert_event_in_google_calander(eventt):
    """
    Insert the event to google calendar
    """
    google_credentials = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            google_credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not google_credentials or not google_credentials.valid:
        if google_credentials and google_credentials.expired and google_credentials.refresh_token:
            google_credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            google_credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(google_credentials, token)

    service = build('calendar', 'v3', credentials=google_credentials)

    print(eventt)
    event = service.events().insert(calendarId='primary', body=eventt).execute()
    print('Event created: %s' % (event.get('htmlLink')))


def delete_event_in_google_calander(user_id, car_id, start_time):
    """
    Insert the event to google calendar
    """
    google_credentials = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            google_credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not google_credentials or not google_credentials.valid:
        if google_credentials and google_credentials.expired and google_credentials.refresh_token:
            google_credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            google_credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(google_credentials, token)

    service = build('calendar', 'v3', credentials=google_credentials)

    now = datetime.datetime.now().isoformat() + '+10:00'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime', timeZone='+10:00').execute()
    events = events_result.get('items', [])

    for event in events:
        event_start_time = event['start']['dateTime'].replace('T', ' ').split('+')[0]
        if event['description'] == f'userId:{user_id} and carId:{car_id}' and event_start_time == start_time:
            print('deleting event')
            service.events().delete(calendarId='primary', eventId=event['id']).execute()
            print('event deleted')
            return

    print('No future events found.')
