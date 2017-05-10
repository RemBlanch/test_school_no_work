#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Google's OAuth 2.0 API

    Mover a base de datos:
        export GOOGLE_CLIENT_ID="123456789-jhkgljk2g34lkjg24.apps.googleusercontent.com"
        export GOOGLE_CLIENT_SECRET="SDfKsdflkSJDFSFDHhjsdfIUWER"
        export SECRET_KEY="SECRET_KEY_OF_YOUR_CHOOSING"
        ./google_login.py

        IMPORTANT: OAuth 2 requires HTTPS. This app will override that if DEBUG
        is set in the environment.
"""

from google.globalParameters import draft_URL

"""
    Creates a new draft with the DRAFT label.
    This method supports an /upload URI and accepts uploaded media with the
    following characteristics:
        Maximum file size: 35MB
        Accepted Media MIME types: message/rfc822
"""
def createDraft(userID, google, extra=None):

    response = google.post(
        draft_URL['ACTION_URL'] + userID + draft_URL['DRAFTS'],
        params = extra
    )
    return response

"""
    Immediately and permanently deletes the specified draft. Does not simply
    trash it.
"""
def deleteDraft(userID, draftID, google, extra=None):

    response = google.delete(
        draft_URL['ACTION_URL'] + userID + draft_URL['DRAFTS'] + '/%s' % draftID,
        params = extra
    )
    return response

"""
    Gets the specified draft.
"""
def getDraft(userID, draftID, google, extra=None):
    response = google.get(
        draft_URL['ACTION_URL'] + userID + draft_URL['DRAFTS'] + '/%s' % draftID,
        params = extra
    )
    return response

def listDraft(userID, google):
    response = google.get(
        draft_URL['ACTION_URL'] + userID + draft_URL['DRAFTS']
    )
    return response

"""
    Replaces a draft's content.
    This method supports an /upload URI and accepts uploaded media with the
    following characteristics:
    Maximum file size: 35MB
    Accepted Media MIME types: message/rfc822

"""
def updateDraft(userID, draftID, google, extra=None):
    response = google.put(
        draft_URL['ACTION_URL'] + userID + draft_URL['DRAFTS'] + '/%s' % draftID,
        params = extra
    )
    return response

"""
    Sends the specified, existing draft to the recipients in the To, Cc, and
    Bcc headers. This method supports an /upload URI and accepts uploaded media
    with the following characteristics:
    Maximum file size: 35MB
    Accepted Media MIME types: message/rfc822
"""
def sendDraft(userID, google, extra=None):
    response.post(
        draft_URL['ACTION_URL'] + userID + draft_URL['DRAFTS'] + draft_URL['SEND']
        params = extra
    )
    return response
