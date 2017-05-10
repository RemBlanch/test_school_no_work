#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's GMAIL API

"""

from google.globalParameters import thread_URL

"""
    Creates a new label.
        userID  -->     User profile ID.
        google  -->     OAuth2Session
        extra   -->     Dictionary with extra data.
"""
def createLabel(userID, google, extra=None):

    response = google.post(
        thread_URL['ACTION_URL']  + userID + thread_URL['LABELS'],
        params = extra
    )
    return response

"""
    Immediately and permanently deletes the specified label and removes it from
    any messages and threads that it is applied to.
        userID  -->     User profile ID.
        labelID -->     Label ID.
        google  -->     OAuth2Session.
"""
def deleteLabel(userID, labelID, google):

    response = google.delete(
        thread_URL['ACTION_URL'] + userID + thread_URL['LABELS'] + '/%s' % labelID,
        params = extra
    )

    return response

"""
    Lists all labels in the user's mailbox.
        userID  -->     User profile ID.
        google  -->     OAuth2Session.
"""
def listLabel(userID, google):

    response = google.get(
        thread_URL['ACTION_URL']  + userID + thread_URL['LABELS'],
        params = extra
    )

    return response

"""
    Updates the specified label.
        userID  -->     User profile ID.
        labelID -->     Label ID.
        google  -->     OAuth2Session.
        extra   -->     Dictionary with extra data.
"""
def updateLabel(userID, labelID, google, extra):

    response = google.put(
        thread_URL['ACTION_URL']  + userID + thread_URL['LABELS'] + '/%s' % labelID,
        params = extra
    )

    return response

"""
    Updates the specified label.
        userID  -->     User profile ID.
        labelID -->     Label ID.
        google  -->     OAuth2Session.
        extra   -->     Dictionary with extra data.
"""
def getLabel(userID, labelID, google, extra):

    response = google.get(
        thread_URL['ACTION_URL'] + userID + thread_URL['LABELS'] + '/%s' % labelID,
        params = extra
    )

    return response

"""
    Updates the specified label. This method supports patch semantics.
        userID  -->     User profile ID.
        labelID -->     Label ID.
        google  -->     OAuth2Session.
        extra   -->     Dictionary with extra data.
"""
def patchLabel(userID, labelID, google, extra):

    response = google.patch(
        thread_URL['ACTION_URL']  + userID + thread_URL['LABELS'] + '/%s' % labelID,
        params = extra
    )

    return response
