#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's CALENDAR API

"""

import os
from __future__ import (
  absolute_import,
  unicode_literals,
)
from requests_oauthlib import OAuth2Session
from google.globalParameters import calendar_URL

################################# CALENDARLIST #################################

def deleteCalendarList(google, calendarID):
    response = google.delete(
        calendar_URL['ACTION_URL'] + calendar_URL['CALENDAR_LIST']
            + '/{}'.format(calendarID)
    )
    if response.status_code == 204:
        print 'Calendar %s has been deleted properly.'.format(calendarID)
        return True

    else:
        print 'Calendar {} deletion error.\n status_code {}.'.format(calendarID, response.status_code)
    return False

def getCalendarList(google, calendarID):
    response = google.get(
        calendar_URL['ACTION_URL'] + calendar_URL['CALENDAR_LIST']
            + '/{}'.format(calendarID)
    )

    if response.status_code == 200:
        print 'Calendar list retrieved'
        return response
    else:
        print 'Calendar list error {}.'.format(response.status_code)
    return False

def listCalendar(google, params=None):
    """ Obtain user's calendar list. """
    response = google.get(
        calendar_URL['ACTION_URL'] + calendar_URL['CALENDAR_LIST'],
        params = params
    )

    if response.status_code == 200:
        print 'List of calendars were successfully retrieved.'
        return response
    else:
        print 'List calendars retrieve error.\n status_code {}.'.format(response.status_code)
    return False

def insertCalendarList(google, params=None):
    response = google.post(
        calendar_URL['ACTION_URL'] + calendar_URL['CALENDAR_LIST'],
        params = params
    )

    if response.status_code == 200:
        print 'Insert calendar were successfully achieved.'
        return response
    else:
        print 'Insert calendar error.\n status_code {}.'.format(response.status_code)
    return False

def watchCalendar(google, params = None):
    """ Watch for changes to CalendarList resources. """
    google.post(
        calendar_URL['ACTION_URL'] + calendar_URL['CALENDAR_LIST'],
        params = params
    )

    return response

def updateCalendarList(google, calendarID, params = None):
    google.put(
        calendar_URL['ACTION_URL'] + calendar_URL['CALENDAR_LIST']
            + '/{}'.format(calendarID),
        params = params
    )

    return response
