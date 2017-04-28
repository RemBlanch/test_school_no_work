#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's CALENDAR API

"""

from __future__ import (
  absolute_import,
  unicode_literals,
)

import os
import requests

from flask import (
    request,
    session,
)

from requests_oauthlib import OAuth2Session

event_URL = 'https://www.googleapis.com/calendar/v3/calendars/%s/events',

def deleteEvent(credentials, calendarID, eventID, params):
    """ Deletes an event. """
    google = OAuth2Session(
        credentials['CLIENT_ID'],
        token=session['oauth_token']
    )

    response = google.delete(
        event_URL + '/%s' % calendarID eventID,
        params
    )

    return response

def getEvent(credentials, calendarID, eventID, params):
    """ Get information of a single event """
    google = OAuth2Session(
        credentials['CLIENT_ID'],
        token=session['oauth_token']
    )

    response = google.get(
        event_URL + '/%s' % calendarID eventID,
        params
    )

    return response

def importEvent(credentials, calendarID, params):
    """ Imports an event. This operation is used to add a private copy of an
    existing event to a calendar. """
    google = OAuth2Session(
        credentials['CLIENT_ID'],
        token=session['oauth_token']
    )

    response = google.post(
        event_URL + '/%s' % calendarID eventID,
        params
    )

    return response

def insertEvent(credentials, calendarID, params):
    """ Creates an event.  """
    return NotImplemented

def instanceEvent():
    return NotImplemented

def listEvents(app, calendarID):
    """ Obtain list of calendar of a user """
    google = OAuth2Session(
        app.config['GOOGLE_CLIENT_ID'],
        token=session['oauth_token']
    )

    response = google.get(
        calendar_URL['ACTION_URL'] +
        calendar_URL['CALENDAR_EVENTS'] % calendarID
    )

    return response

def moveEvent():
    return NotImplemented

def patchEvent():
    return NotImplemented

def quickAddEvent(app, calendarID, description):
    google = OAuth2Session(
        app.config['GOOGLE_CLIENT_ID'],
        token=session['oauth_token']
    )

    response = google.get(
        calendar_URL['ACTION_URL'] +
        calendar_URL['CALENDAR_EVENTS'] +
        '/quickAdd' % calendarID,
        params={
            'text': description
        }
    )

    return response

def updateEvent():
    google = OAuth2Session(
        app.config['GOOGLE_CLIENT_ID'],
        token=session['oauth_token']
    )

    return response

def watchEvent():
    return NotImplemented
