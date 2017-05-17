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

def deleteCalendar(google, calendarID):
    response = google.delete(
        calendar_URL['ACTION_URL'] + calendar_URL['CALENDAR_LIST']
            + '/{}'.format(calendarID)
    )
    return NotImplemented

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
