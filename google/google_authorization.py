#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's OAuth 2.0 API TOKEN AUTHORIZATION

    IMPORTANT: OAuth 2 requires HTTPS. This app will override that if DEBUG is
    set in the environment.
"""

from __future__ import (
  absolute_import,
  unicode_literals,
)

import os
import requests
from time import time
from authorization import token_authorization
import google.globalParameters as url_authorization

""" REMEMBER
        We use the session as a simple DB for this example.
"""
from flask import (
    request,
    session,
)
from requests_oauthlib import OAuth2Session

class google_auth(token_authorization):

    def authorization(self, google):
        """ Redirect the user/resource owner to the OAuth provider using
        an URL with the few key OAuth parameters. """

        authorization_url, state = google.authorization_url(
            url_authorization.GOOGLE_OAUTH_URL,
            # offline for refresh token
            access_type="offline"
        )

        # Return authorization_url and actual status
        return authorization_url, state

    def retrieve_token(self, client_secret, google):
        """ The user has been redirected back from the provider to callback URL.
        With this redirection comes an authorization code included in the redirect
        URL. Now --> Obtain token. """

        token = google.fetch_token(
            url_authorization.GOOGLE_TOKEN_URL,
            client_secret = client_secret,
            authorization_response = request.url
        )

        return token

    def automatic_refresh_token(self, app):
        """ Refreshing an 0Auth2 token using a refresh token. """
        token = session['oauth_token']

        # We force an expiration by setting expired at in the past.
        # This will trigger an automatic refresh next time we interact with
        # Googles API.

        token['expires_at'] = time() - 10

        extra = {
            'client_id': app['CLIENT_ID'],
            'client_secret': app['CLIENT_SECRET']
        }

        def token_updater(token):
            session['oauth_token'] = token

        google = OAuth2Session(
            app['CLIENT_ID'],
            token=token,
            auto_refresh_kwargs=extra,
            auto_refresh_url=url_authorization.GOOGLE_TOKEN_URL,
            token_updater=token_updater
        )

        # Trigger the automatic refresh
        google.get(url_authorization.GOOGLE_OAUTH_USER_INFO)

    def manual_refresh(self, app):
        """Refreshing an OAuth 2 token using a refresh token."""
        token = session['oauth_token']

        extra = {
            'client_id': app['CLIENT_ID'],
            'client_secret': app['CLIENT_SECRET'],
        }

        google = OAuth2Session(app['CLIENT_ID'], token=token)
        session['oauth_token'] = google.refresh_token(url_authorization.GOOGLE_TOKEN_URL, **extra)

    def token_validate(self):
        """ Validate a token with OAuth provider Google."""
        token = session['oauth_token']

        # Defined at https://developers.google.com/accounts/docs/OAuth2LoginV1#validatingtoken
        response = requests.get(
            url_authorization.GOOGLE_TOKEN_INFO,
            params={
                'access_token': token['access_token']
            }
        )

        if response.status_code == 200:
            print('Token validate OK', 'info')
        else:
            print('Could not validate token: {}'.format(response.content), 'danger')

        # No OAuth2Session is needed, just a plain GET request
        return response.json()

    def token_revoke(self):
        """Revoking an OAuth 2 token using a refresh token."""
        token = session['oauth_token']

        response = requests.get(
            url_authorization.GOOGLE_OAUTH_REVOKE,
            params={
                'token': token['access_token']
            }
        )

        if response.status_code == 200:
            print('Authorization revoked', 'warning')
        else:
            print('Could not revoke token: {}'.format(response.content), 'danger')
            return False

        return True

    def getSession(self, client_id, url_to_redirect, scope):
        """ Generate user authorization session """
        return OAuth2Session(
            client_id,
            scope = scope,
            redirect_uri = url_to_redirect
        )
