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

def deleteEvent(google, calendarID, eventID, params = None):
    """ Deletes an event. """
    response = google.delete(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['EVENTS'] + '/{}'.format(eventID),
        params = params
    )

    if response.status_code == 204:
        print 'Event {} in calendar {} has been deleted properly.'.format(eventID, calendarID)
        return True
    else:
        print 'Event {} in calendar {} delete error.\n status_code {}.'.format(eventID, calendarID, response.status_code)
    return False

def getEvent(google, calendarID, eventID, params = None):
    """ Get information of a single event """
    response = google.get(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['EVENTS'] + '/{}'.format(eventID),
        params = params
    )
    if response.status_code == 200:
        print 'Event {} in calendar {} has been retrieved properly.'.format(eventID, calendarID)
        return response
    else:
        print 'Event {} in calendar {} retrieving error.\n status_code {}.'.format(eventID, calendarID, response.status_code)
    return False

def importEvent(google, calendarID, params = None):
    """ Imports an event. This operation is used to add a private copy of an
    existing event to a calendar. """

    response = google.post(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['EVENTS'] + '/{}'.format(eventID),
        params = params
    )

    if response.status_code == 200:
        print 'Event {} in calendar {} was successfully imported.'.format(eventID, calendarID)
        return response
    else:
        print 'Event {} in calendar {} import error.\n status_code {}.'.format(eventID, calendarID, response.status_code)
    return False

def insertEvent(google, calendarID, params = None):
    """ Creates an event.  """
    response = google.post(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['EVENTS'] + '/{}'.format(eventID),
        params = params
    )

    if response.status_code == 200:
        print 'Event {} in calendar {} was successfully inserted.'.format(eventID, calendarID)
        return response
    else:
        print 'Event {} in calendar {} insert error.\n status_code {}.'.format(eventID, calendarID, response.status_code)
    return False

def instanceEvent(google, calendarID, params = None):
    response = google.get(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['EVENTS'] + '/{}'.format(eventID)
            + calendar_URL['INSTANCE'],
        params = params
    )

    if response.status_code == 200:
        print 'Instance of event {} in calendar {} has been retrieved properly.'.format(eventID, calendarID)
        return response
    else:
        print 'Instance of event {} in calendar {} retrieve error.\n status_code {}.'.format(eventID, calendarID, response.status_code)
    return False

def listEvents(google, calendarID, params = None):
    """ Obtain list of calendar of a user """

    response = google.get(
        calendar_URL['ACTION_URL'] + '{}'.format(calendarID)
            + calendar_URL['CALENDAR_EVENTS'],
        params = params
    )

    if response.status_code == 200:
        print 'List of event in calendar {} were successfully retrieved.'.format(calendarID)
        return response
    else:
        print 'List of event in calendar {} retrie error.\n status_code {}.'.format(calendarID, response.status_code)
    return False

def moveEvent(google, calendarID, params = None):
    response = google.post(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['EVENTS'] + '/{}'.format(eventID)
            + '/move',
        params = params
    )

    if response.status_code == 200:
        print 'Event {} in calendar {} was successfully imported.'.format(eventID, calendarID)
        return response
    else:
        print 'Event {} in calendar {} import error.\n status_code {}.'.format(eventID, calendarID, response.status_code)
    return False

def patchEvent(google, calendarID, params = None):
    response = google.patch(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['EVENTS'] + '/{}'.format(eventID),
        params = params
    )

    if response.status_code == 200:
        print 'Event {} in calendar {} has been updated properly.'.format(eventID, calendarID)
        return response
    else:
        print 'Event {} in calendar {} update error.\n status_code {}.'.format(eventID, calendarID, response.status_code)
    return False

def quickAddEvent(google, calendarID, params = None):
    response = google.get(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['CALENDAR_EVENTS'] + calendar_URL['QUICK_ADD']
        params = params
    )

    if response.status_code == 200:
        print 'Event {} in calendar {} has been added properly.'.format(eventID, calendarID)
        return response
    else:
        print 'Event {} in calendar {} add error.\n status_code {}.'.format(eventID, calendarID, response.status_code)
    return False

def updateEvent(google, calendarID, eventID, params = None):
    response = google.put(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['EVENTS'] + '/{}'.format(eventID),
        params = params
    )

    if response.status_code == 200:
        print 'Event {} in calendar {} has been updated properly.'.format(eventID, calendarID)
        return response
    else:
        print 'Event {} in calendar {} update error.\n status_code {}.'.format(eventID, calendarID, response.status_code)
    return False

def watchEvent(google, calendarID, params = None):
    response = google.post(
        calendar_URL['ACTION_URL'] + '/{}'.format(calendarID)
            + calendar_URL['EVENTS'] + calendar_URL['WATCH'],
        params = params
    )

    if response.status_code == 200:
        print 'Watch events in calendar {}.'.format(calendarID)
        return response
    else:
        print 'Watch events in calendar {} error.\n status_code {}.'.format(calendarID, response.status_code)
    return False
