#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's GMAIL API

"""

from google.globalParameters import thread_URL

def getThread(google, userID, threadID, extra):

    response = google.get(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['THREADS'] + '/%s' % userID, threadID
        params = extra
    )

    return response

def listThread(google, userID, extra):

    response = google.get(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['THREADS'] % userID
        params = extra
    )
    return response

def modifyThread(google, userID, threadID, extra):

    response = google.post(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['THREADS'] + '/%s'  + '/modify' % userID, threadID
        params = extra
    )

    return response

def deleteThread(google, userID, threadID, extra):

    response = google.delete(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['THREADS'] + '/%s' % userID, threadID
        params = extra
    )

    return response

def trashThread(google, userID, threadID, extra):

    response = google.post(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['THREADS'] + '/%s'  + '/trash' % userID, threadID
        params = extra
    )

    return response

def untrashThread(google, userID, threadID, extra):

    response = google.post(
        thread_URL['ACTION_URL']  + '/%s' + thread_URL['THREADS'] + '/%s'  + '/untrash' % userID, threadID
        params = extra
    )

    return response
