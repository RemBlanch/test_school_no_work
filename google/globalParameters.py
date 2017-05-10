#!/usr/bin/env python
# -*- coding: utf-8 -*-

########## URL TOKEN OAUTH ##########

GOOGLE_OAUTH_URL = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_TOKEN_INFO = 'https://www.googleapis.com/oauth2/v1/tokeninfo?'
GOOGLE_OAUTH_REVOKE = 'https://accounts.google.com/o/oauth2/revoke?'
GOOGLE_OAUTH_USER_INFO = 'https://www.googleapis.com/oauth2/v1/userinfo'

USER_MAIL_ACCESS = 'https://www.googleapis.com/auth/userinfo.email'
USER_PROFILE_ACCESS = 'https://www.googleapis.com/auth/userinfo.profile'
USER_GMAIL_READ = 'https://www.googleapis.com/auth/gmail.readonly'
USER_CALENDAR_READ = 'https://www.googleapis.com/auth/calendar.readonly'
USER_CONTACTS_READ = 'https://www.googleapis.com/auth/contacts.readonly'

########## URL GMAIL ##########

thread_URL = {
    'ACTION_URL': 'https://www.googleapis.com/gmail/v1/users/',
    'THREADS': '/threads',
    'MODIFY': '/modify',
    'TRASH': '/trash',
    'UNTRASH': '/untrash',
    'LABELS': '/labels'
}

mail_URL = {
    'ACTION_URL': 'https://www.googleapis.com/gmail/v1/users/',
    'MESSAGES': '/messages',
    'MODIFY': '/modify',
    'SEND': '/send'
}
