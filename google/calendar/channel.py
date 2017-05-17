#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's CALENDAR API

"""

def channelStop(google, resource):
    response = google.post(
        'https://www.googleapis.com/calendar/v3/channels/stop',
        params = resource
    )

    if response.status_code == 204:
        print 'Channel closed'
        return True
    else:
        print 'Channel error {}'.response.status_code
        return False

def FreeBusy(google, resource):
""" Returns free/busy information for a set of calendars. """
    response = google.post(
        'https://www.googleapis.com/calendar/v3/channels/stop',
        params = resource
    )
    if response.status_code == 200:
        print 'State of calendars retrieved'
        return response
    else:
        print 'State of calendars error {}'.response.status_code
        return False
