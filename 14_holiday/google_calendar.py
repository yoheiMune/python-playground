# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from pprint import pprint
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http


# Authentication.
# Ref: https://developers.google.com/google-apps/calendar/quickstart/python
json_file = 'secret/yoheim-labo-3178ee6fa5bf.json'
scopes = ['https://www.googleapis.com/auth/calendar.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scopes=scopes)
http_auth = credentials.authorize(Http())
service = apiclient.discovery.build("calendar", "v3", http=http_auth)



"""
eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
"""

# now = datetime.utcnow().isoformat() + 'Z'
# print(now)

calendar_id = "ja.japanese#holiday@group.v.calendar.google.com"
dtfrom      = date(year=2016, month=1, day=1).isoformat() + "T00:00:00.000000Z"
dtto        = date(year=2016, month=12, day=31).isoformat() + "T00:00:00.000000Z"

events_results = service.events().list(
        calendarId = calendar_id,
        timeMin = dtfrom,
        timeMax = dtto,
        maxResults = 50,
        singleEvents = True,
        orderBy = "startTime"
    ).execute()
# pprint(events_results)
events = events_results.get('items', [])
for event in events:
    print("%s\t%s" % (event["start"]["date"], event["summary"]))


