#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's GMAIL API

"""

from google.globalParameters import thread_URL

def getThread(userID, threadID, google, extra):

    response = google.get(
        thread_URL['ACTION_URL']  + userID + thread_URL['THREADS'] + '/%s' % threadID,
        params = extra
    )
    return response

def listThread(userID, google, extra):

    response = google.get(
        thread_URL['ACTION_URL'] + userID + thread_URL['THREADS'],
        params = extra
    )
    return response

def modifyThread(userID, threadID, google, extra):
    response = google.post(
        thread_URL['ACTION_URL'] + userID + thread_URL['THREADS'] + '/{0}'.param(threadID)  + '/modify',
        params = extra
    )
    return response

def deleteThread(userID, threadID, google, extra):

    response = google.delete(
        thread_URL['ACTION_URL']  + userID + thread_URL['THREADS'] + '/%s' % threadID,
        params = extra
    )
    return response

def trashThread(google, userID, threadID, extra):

    response = google.post(
        thread_URL['ACTION_URL'] + userID + thread_URL['THREADS'] + '/{0}'.param(threadID) + '/trash',
        params = extra
    )
    return response

def untrashThread(google, userID, threadID, extra):

    response = google.post(
        thread_URL['ACTION_URL'] + userID + thread_URL['THREADS'] + '/{0}'.param(threadID) + '/untrash',
        params = extra
    )
    return response
