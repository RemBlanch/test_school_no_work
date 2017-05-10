#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Google's OAuth 2.0 API

    Mover a base de datos:
        export GOOGLE_CLIENT_ID="123456789-jhkgljk2g34lkjg24.apps.googleusercontent.com"
        export GOOGLE_CLIENT_SECRET="SDfKsdflkSJDFSFDHhjsdfIUWER"
        export SECRET_KEY="SECRET_KEY_OF_YOUR_CHOOSING"
        ./google_login.py

        IMPORTANT: OAuth 2 requires HTTPS. This app will override that if DEBUG is set in
            the environment.
"""

from google.globalParameters import mail_URL

def deleteMessage(userID, mailID, google, filter = None):

    response = google.delete(
        mail_URL['ACTION_URL'] + userID + mail_URL['MESSAGES'] + '/%s' % mailID,
        params = args
    )
    return response

"""
    Gets the specified message.
        userID --> User profile ID.
        mailID --> Email ID.
        google --> OAuth2Session.
        filter --> Dictionary with query filters.
"""
def getMessage(userID, mailID, google, filter = None):

    response = google.get(
        mail_URL['ACTION_URL'] + userID + mail_URL['MESSAGES'] + '/%s' % mailID,
        params = filter
    )
    return response

def insertMessage():
    return NotImplemented

"""
    Lists the messages in the user's mailbox.
        userID --> User profile ID.
        google --> OAuth2Session.
        filter --> Dictionary with query filters.

"""
def listMessage(userID, google, filter = None):

    response = google.get(
        mail_URL['ACTION_URL']  + userID + mail_URL['MESSAGES'],
        params = filter
    )
    return response

def modifyMessage(userID, mailID, filter = None):

    response = google.post(
        mail_URL['ACTION_URL']  + userID + mail_URL['MESSAGES'] + '/{0}'.format(mailID) + mail_URL['MODIFY'],
        params = filter
    )
    return response

def email_import():
    return NotImplemented

def batchDelete():
    return NotImplemented

def batchModify():
    return NotImplemented
