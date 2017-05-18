#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's CALENDAR API

"""

from google.globalParameters import acl_URL

def delete(google, calendarID, ruleID):
    """ """
    response = google.delete(
        acl_URL['ACTION_URL'] + '{}'.format(calendarID)
            + acl_URL['ACL'] + '/{}'.format(ruleID)
    )
    if response.status_code == 204:
        print 'ACL {} has been cleaned properly.'.format(calendarID)
        return True
    else:
        print 'ACL {} cleanup error.\n status_code {}.'.format(calendarID, response.status_code)
    return False

def get(google, calendarID, ruleID):
    response = google.get(
        acl_URL['ACTION_URL'] + '{}'.format(calendarID)
            + acl_URL['ACL'] + '/{}'.format(ruleID)
    )
    if response.status_code == 200:
        print 'ACL {} was successfully extracted.'.format(calendarID)
        return response
    else:
        print 'ACL {} get error.\n status_code {}.'.format(calendarID, response.status_code)
    return None

def insert(google, calendarID, params = None):
    response = google.post(
        acl_URL['ACTION_URL'] + '{}'.format(calendarID)
            + acl_URL['ACL'],
        params = params
    )
    if response.status_code == 200:
        print 'ACL {} was successfully created.'.format(calendarID)
        return response
    else:
        print 'ACL {} creation error.\n status_code {}.'.format(calendarID, response.status_code)
    return None

def list(google, calendarID):
    response = google.post(
        acl_URL['ACTION_URL'] + '{}'.format(calendarID) + acl_URL['ACL']
    )
    if response.status_code == 200:
        print 'List of ACLs were successfully retrieved.'
        return response
    else:
        print 'List ACLs retrieve error.\n status_code {}.'.format(response.status_code)
    return False

def patch(google, calendarID, ruleID, params = None):
    response = google.patch(
        acl_URL['ACTION_URL'] + '{}'.format(calendarID)
            + acl_URL['ACL'] + '/{}'.format(ruleID),
        params = params
    )
    if response.status_code == 200:
        print 'ACL {} was successfully pathed.'.format(calendarID)
        return response
    else:
        print 'ACL {} patch error.\n status_code {}.'.format(calendarID, response.status_code)
    return None

def update(google, calendarID, ruleID, params = None):
    response = google.put(
        acl_URL['ACTION_URL'] + '{}'.format(calendarID)
            + acl_URL['ACL'] + '/{}'.format(ruleID),
        params = params
    )
    if response.status_code == 200:
        print 'ACL {} was successfully updated.'.format(calendarID)
        return response
    else:
        print 'ACL {} update error.\n status_code {}.'.format(calendarID, response.status_code)
    return None

def watch(google, calendarID, params = None):
    response = google.post(
        acl_URL['ACTION_URL'] + '{}'.format(calendarID)
            + acl_URL['ACL'] + '/watch',
        params = params
    )
    return NotImplemented
