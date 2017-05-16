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
from time import time

""" REMEMBER
        We use the session as a simple DB for this example.
"""
from flask import (
    request,
    session,
)
from requests_oauthlib import OAuth2Session

calendar_URL = {
    'ACTION_URL': 'https://www.googleapis.com/calendar/v3',
    'CALENDAR_LIST': '/users/me/calendarList',
    'CALENDAR' '/calendars'
    'CALENDAR_WATCH': '/watch'
}

def deleteCalendar(credentials, calendarID, calendar_type, **extra):
    """ Deletes an entry on the general/user's calendar list.
    Returns empty content [204] if deletion was OK. """
    google = OAuth2Session(
        credentials['CLIENT_ID'],
        token = session['oauth_token']
    )

    response = google.delete(
        calendar_URL['ACTION_URL'] + calendar_type  + '/%s' % calendarID,
        params = extra
    )

    if response.status_code == 204:
        print 'Se ha eliminado el calendario %s correctamente' % calendarID
        return True

    else:
        print "Error en la elminación del calendario %s.\n status_code %d" % calendarID, response.status_code
    return False

def getCalendar(credentials, calendarID, calendar_type, **extra):
    """ Returns an entry on the general/user's calendar list """
    google = OAuth2Session(
        credentials['CLIENT_ID'],
        token = session['oauth_token']
    )

    response = google.get(
        calendar_URL['ACTION_URL'] + calendar_type  + '/%s' % calendarID,
        params = extra
    )

    return response

def insertCalendar(credentials, calendar_type, **extra):
    """ Adds an entry to the general/user's calendar list. """
    google = OAuth2Session(
        credentials['CLIENT_ID'],
        token = session['oauth_token']
    )

    response = google.insert(
        calendar_URL['ACTION_URL'] + calendar_type,
        params = extra
    )

    return response

def patchCalendar(credentials, calendarID, calendar_type, **extra):
    """ Updates an entry on the general/user's calendar list. This method
    supports patch semantics. """
    google = OAuth2Session(
        credentials['CLIENT_ID'],
        token = session['oauth_token']
    )

    response = google.patch(
        calendar_URL['ACTION_URL'] + calendar_type  + '/%s' % calendarID,
        params = extra
    )

    return response

def updateCalendar(credentials, calendarID, calendar_type, **extra):
    """ Updates an entry on the general/user's calendar list. """
    google = OAuth2Session(
        credentials['CLIENT_ID'],
        token = session['oauth_token']
    )

    response = google.put(
        calendar_URL['ACTION_URL'] + calendar_type  + '/%s' % calendarID,
        params = extra
    )

    return response

################################# CALENDARLIST #################################

def listCalendar(google, params=None):
    """ Obtain user's calendar list. """
    response = google.get(
        calendar_URL['ACTION_URL'] + calendar_URL['CALENDAR_LIST'],
        params = params
    )

    return response

def watchCalendar():
    """ Watch for changes to CalendarList resources. """
    return NotImplemented

############################### GENERAL CALENDAR ###############################

def clearCalendar():
    """ Clears a primary calendar. This operation deletes all events associated
    with the primary calendar of an account. """
    return NotImplemented
