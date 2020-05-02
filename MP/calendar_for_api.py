#!/usr/bin/env python3 --noauth_local_webserver
# pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client httplib2

# Reference: https://developers.google.com/calendar/quickstart/python
# Documentation: https://developers.google.com/calendar/overview

# Be sure to enable the Google Calendar API on your Google account by following the reference link above and
# download the credentials.json file and place it in the same directory as this file.

from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = "https://www.googleapis.com/auth/calendar"
store = file.Storage("token.json")
creds = store.get()

if(not creds or creds.invalid):
    flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
    creds = tools.run_flow(flow, store)

service = build("calendar", "v3", http=creds.authorize(Http()))


def insert(event):
    event = service.events().insert(calendarId = "primary", body = event).execute()


def delete(user_id, car_id, begin_time):
    # Get a list of events from the current time
    now = datetime.datetime.now().isoformat() + '+10:00'
    events = service.events().list( calendarId='primary', 
                                    timeMin=now,
                                    maxResults=10, 
                                    singleEvents=True,
                                    orderBy='startTime', 
                                    timeZone='+10:00').execute()
    events = events.get("items", [])

    # Search for the right event and delete
    for event in events:
        event_start_time    = event['start']['dateTime'].replace('T', ' ').split('+')[0] # '2020-05-02T10:00:00+10:00'
        begin_time          = begin_time + ":00"

        if event['description'] == f'userId: {user_id} and carId: {car_id}' and event_start_time == begin_time:
            service.events().delete(calendarId='primary', 
                                    eventId=event['id']).execute() # Deletion
            return
