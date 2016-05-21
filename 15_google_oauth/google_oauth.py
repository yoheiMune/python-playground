# -*- coding: utf-8 -*-
#
# Using Google API via OAuth 2.0, which is under a embedded system.
# This program is a sample for Google Bigquery.
import webbrowser
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage


def get_credentials():

    SCOPE = 'https://www.googleapis.com/auth/bigquery.readonly'
    flow = flow_from_clientsecrets('secret/oauth2.json',
                                   scope=SCOPE,
                                   redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    # STEP1
    auth_uri = flow.step1_get_authorize_url()
    webbrowser.open(auth_uri)


    # Get code.
    code = input("Input your code > ")


    # STEP2
    credentials = flow.step2_exchange(code)
    print(credentials)

    # Save
    CREDENTIALS_FILE = "./secret/credentials"
    Storage(CREDENTIALS_FILE).put(credentials)

    return credentials


if __name__ == "__main__":

    get_credentials()