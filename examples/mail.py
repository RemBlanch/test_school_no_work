#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import email
import os
import sys
sys.path.append('../')
from requests_oauthlib import OAuth2Session
import google.gmail.messages as messages
import google.gmail.labels as labels
from bs4 import BeautifulSoup

try:
    from flask import (
      Flask,
      flash,
      redirect,
      render_template,
      request,
      session,
      url_for,
      jsonify,
    )

except ImportError:
    raise RuntimeError('Requirements not set up, see "Requirements":\n' + __doc__)


def listMail(app, Newparams = None):

    google = OAuth2Session(app.config['GOOGLE_CLIENT_ID'], token=session['oauth_token'])
    ownlabels = labels.listLabel(session['user']['id'], google).json()
    if Newparams == None:
        params = {
            "q": "!label: chat",
            "maxResults": 14
        }
    else:
        params = Newparams
    listMail = messages.listMessage(session['user']['id'], google, params).json()
    return setMainMail(google, ownlabels, listMail)

def setMainMail(google, ownlabels, listMail):

    emailList = []
    email = {}

    for item in listMail['messages']:
        email['id'] = item['id']
        params = {
            "fields": "id,labelIds,payload/headers,snippet,threadId"
        }
        get_email = messages.getMessage(session['user']['id'], item['id'], google, params).json()
        for header in get_email['payload']['headers']:
            if header['name'] == 'Subject':
                email['subject'] = header['value']
        email['labelID'] = get_email['labelIds']
        email['snippet'] = get_email['snippet']
        emailList.append(email.copy())

    return render_template('email_panel.html',
        user = session['user'],
        labels = ownlabels['labels'],
        emailList = emailList)

def getMailbyLabel(app, labelValue):

    google = OAuth2Session(app.config['GOOGLE_CLIENT_ID'], token=session['oauth_token'])
    ownlabels = labels.listLabel(session['user']['id'], google).json()
    params = {
        "q": "label: %s" % labelValue,
        "maxResults": 14
    }
    listMail = messages.listMessage(session['user']['id'], google, params).json()
    return setMainMail(google, ownlabels, listMail)

def getMail(myEmail, app):
    google = OAuth2Session(app.config['GOOGLE_CLIENT_ID'], token=session['oauth_token'])
    raw = { "format": "raw"}
    message_data = messages.getMessage(session['user']['id'], myEmail, google, raw).json()
    msg_str = base64.urlsafe_b64decode(message_data['raw'].encode('ASCII'))
    msg = email.message_from_string(msg_str)

    # MESSAGE HEADER
    header = {
        'FROM' : msg['From'],
        'TO': msg['To'],
        'CC': msg['Cc'],
        'SUBJECT': msg['Subject'],
        'Date': str(msg['Date']),
    }

    # ENCODE STRING
    code = ''
    # HTML STRING
    html = ''
    # TXT STRING
    txt = ''
    # IMG STRING
    img = {}

    for part in msg.walk():

        if part.get_content_type().startswith("text/"):

            if part.get_content_type().endswith('html'):
                code = part.get_content_charset()
                html = part.get_payload(decode=code)

            elif part.get_content_type().endswith('plain'):
                txt = part.get_payload(decode=code)

            elif part.get('Content-Disposition'):
                open('/home/rem/Documents/GMAILTEST/attachments/'+ myEmail + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))

        elif part.get_content_type().startswith("image/"):
            img[part.get('Content-ID')] = 'data:'+ part.get_content_type() + ';base64,' + part.get_payload()

            if part.get('Content-Disposition'):
                open('/home/rem/Documents/GMAILTEST/attachments/'+ myEmail + '/' + part.get('Content-ID'), 'wb').write(part.get_payload(decode=True))

    soup = BeautifulSoup(html)
    for image in soup.findAll('img'):
        try:
            if image['src'] and image['src'].startswith("cid:"):
                image['src'] = img['<' + image['src'][4:] + '>']
        except KeyError:
            print "KEY ERROR"
    html = str(soup)

    return render_template('email.html', headers=header, raw_data=html.decode('UTF-8'), txt_data=txt.decode('UTF-8'))

def listDraft(app):
    google = OAuth2Session(app.config['GOOGLE_CLIENT_ID'], token=session['oauth_token'])
    ownlabels = labels.listLabel(session['user']['id'], google).json()
    listMail = google.get('https://www.googleapis.com/gmail/v1/users/' +  session['user']['id'] + '/drafts?q=%22!in%3A+label%3Achats%22&maxResults=14').json()
    return setMainMail(google, ownlabels, listMail)
