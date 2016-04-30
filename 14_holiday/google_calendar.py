# -*- coding: utf-8 -*-
from datetime import date
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http

# Ref: https://developers.google.com/google-apps/calendar/quickstart/python

# Authentication.
json_file = 'secret/yoheim-labo-3178ee6fa5bf.json'
scopes = ['https://www.googleapis.com/auth/calendar.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scopes=scopes)
http_auth = credentials.authorize(Http())
service = apiclient.discovery.build("calendar", "v3", http=http_auth)


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

events = events_results.get('items', [])
for event in events:
    print("%s\t%s" % (event["start"]["date"], event["summary"]))
"""
2016-01-01  元日
2016-01-11  成人の日
2016-02-11  建国記念の日
2016-03-20  春分の日
2016-03-21  春分の日 振替休日
2016-04-29  昭和の日
2016-05-03  憲法記念日
2016-05-04  みどりの日
2016-05-05  こどもの日
2016-07-18  海の日
2016-08-11  山の日
2016-09-19  敬老の日
2016-09-22  秋分の日
2016-10-10  体育の日
2016-11-03  文化の日
2016-11-23  勤労感謝の日
2016-12-23  天皇誕生日
"""


