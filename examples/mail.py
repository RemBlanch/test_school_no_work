#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import email
from bs4 import BeautifulSoup
import os
from requests_oauthlib import OAuth2Session

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

def getMail(myEmail, app):
    google = OAuth2Session(app.config['GOOGLE_CLIENT_ID'], token=session['oauth_token'])
    message_data = google.get('https://www.googleapis.com/gmail/v1/users/' +  session['user']['id'] + '/messages/'+ myEmail + '/?format=raw').json()

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
        if image['src'].startswith("cid:"):
            image['src'] = img['<' + image['src'][4:] + '>']
    html = str(soup)

    return render_template('email.html', headers=header, raw_data=html.decode('UTF-8'), txt_data=txt.decode('UTF-8'))
