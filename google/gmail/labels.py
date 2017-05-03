#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's GMAIL API

"""

from google.globalParameters import thread_URL

def createLabel(google, userID, extra):

    response = google.post(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['LABELS'] % userID
        params = extra
    )

    return response

def deleteLabel(google, userID, labelID, extra):

    response = google.delete(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['LABELS'] + '/%s' % userID, labelID
        params = extra
    )

    return response

def listLabel(google, userID, extra):

    response = google.get(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['LABELS'] % userID
        params = extra
    )

    return response

def updateLabel(google, userID, labelID, extra):

    response = google.put(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['LABELS'] + '/%s' % userID, labelID
        params = extra
    )

    return response

def getLabel(google, userID, labelID, extra):

    response = google.get(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['LABELS'] + '/%s' % userID, labelID
        params = extra
    )

    return response

def patchLabel(google, userID, labelID, extra):

    response = google.patch(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['LABELS'] + '/%s' % userID, labelID
        params = extra
    )

    return response
