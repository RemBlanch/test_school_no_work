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
from numintec.calendar import Calendar
from requests_oauthlib import OAuth2Session
from google.globalParameters import calendar_URL

############################### GENERAL CALENDAR ###############################
class gCalendar(Calendar):

    def clearCalendar(google, calendarID):
        """ Clears a primary calendar. This operation deletes all events associated
        with the primary calendar of an account. """
        response = google.post(
            calendar_URL['ACTION_URL'] + '/{}'.format(calendarID) + calendar_URL['CLEAR']
        )

        if response.status_code == 204:
            print 'Calendar {} has been cleaned properly.'.format(calendarID)
            return True
        else:
            print 'Calendar {} cleanup error.\n status_code {}.'.format(calendarID, response.status_code)
        return False

    def deleteCalendar(google, calendarID):
        """ Deletes an entry on the general/user's calendar list.
        Returns empty content [204] if deletion was OK. """
        response = google.delete(
            calendar_URL['ACTION_URL'] + '/{}'.format(calendarID) + calendar_URL['DELETE']
        )

        if response.status_code == 204:
            print 'Calendar %s has been deleted properly.'.format(calendarID)
            return True

        else:
            print 'Calendar {} deletion error.\n status_code {}.'.format(calendarID, response.status_code)
        return False

    def getCalendar(google, calendarID, params = None):
        """ Returns an entry on the general/user's calendar list """
        response = google.get(
            calendar_URL['ACTION_URL'] + '/{}'.format(calendarID),
            params = params
        )

        if response.status_code == 200:
            print 'Calendar {} was successfully extracted.'.format(calendarID)
            return response
        else:
            print 'Calendar {} get error.\n status_code {}.'.format(calendarID, response.status_code)
        return None

    def insertCalendar(google, params = None):
        """ Adds an entry to the general/user's calendar list. """
        response = google.insert(
            calendar_URL['ACTION_URL'] + '/{}'.format(calendarID),
            params = params
        )

        if response.status_code == 200:
            print 'Calendar {} was successfully created.'.format(calendarID)
            return response
        else:
            print 'Calendar {} creation error.\n status_code {}.'.format(calendarID, response.status_code)
        return None

    def patchCalendar(google, calendarID, params = None):
        """ Updates an entry on the general/user's calendar list. This method
        supports patch semantics. """
        response = google.patch(
            calendar_URL['ACTION_URL'] + '/{}'.format(calendarID),
            params = params
        )

        if response.status_code == 200:
            print 'Calendar {} was successfully pathed.'.format(calendarID)
            return response
        else:
            print 'Calendar {} patch error.\n status_code {}.'.format(calendarID, response.status_code)
        return None


    def updateCalendar(google, calendarID, params = None):
        """ Updates an entry on the general/user's calendar list. """
        response = google.put(
            calendar_URL['ACTION_URL'] + '/{}'.format(calendarID),
            params = params
        )

        if response.status_code == 200:
            print 'Calendar {} was successfully updated.'.format(calendarID)
            return response
        else:
            print 'Calendar {} update error.\n status_code {}.'.format(calendarID, response.status_code)
        return None
