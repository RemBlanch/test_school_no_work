#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import json
import grequests
sys.path.append('../')
from pprint import pformat
import google.gmail.messages as messages
from requests_oauthlib import OAuth2Session
from google.google_authorization import google_auth

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

os.environ['GOOGLE_CLIENT_ID'] = "1087046004082-2q1diuuse89rt6ahu6mma050jqidmsdu.apps.googleusercontent.com"
os.environ['GOOGLE_CLIENT_SECRET'] = "2k1nKdYteKu_yTJuvuduKvO-"
os.environ['SECRET_KEY'] = "CHECK_MATE"
os.environ['DEBUG'] = '1'

app = Flask(__name__)
app.config.update({
  'DEBUG': bool(os.environ.get('DEBUG')),
  'SECRET_KEY': os.environ.get('SECRET_KEY', 'CHANGEME'),
  'GOOGLE_CLIENT_ID': os.environ.get('GOOGLE_CLIENT_ID'),
  'GOOGLE_CLIENT_SECRET': os.environ.get('GOOGLE_CLIENT_SECRET'),
})

myScope = [
            'https://www.googleapis.com/auth/userinfo.email',
            'https://www.googleapis.com/auth/userinfo.profile',
            'https://www.googleapis.com/auth/gmail.readonly',
            'https://www.googleapis.com/auth/calendar.readonly',
            'https://www.googleapis.com/auth/contacts.readonly'
]

if app.debug:
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

if not app.config['GOOGLE_CLIENT_ID'] or not app.config['GOOGLE_CLIENT_SECRET']:
    raise RuntimeError('Environment not set up, see "Running":\n' + __doc__)

###############################################################################

@app.route("/")
def demo():
    global google
    url_to_redirect = url_for('retrieve', _external=True)
    google = google_auth().getSession(
        app.config['GOOGLE_CLIENT_ID'],
        url_to_redirect,
        myScope
    )
    url, state = google_auth().authorization(google)
    session['oauth_state'] = state
    return redirect(url)

@app.route("/callback", methods=["GET"])
def retrieve():
    url_to_redirect = url_for('retrieve', _external=True)
    session['oauth_token'] = google_auth().retrieve_token(app.config['GOOGLE_CLIENT_SECRET'], google)
    return redirect(url_for('.menu'))

@app.route("/menu", methods=["GET"])
def menu():
    session['user'] = google.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    return """
    <h1>Congratulations, you have obtained an OAuth 2 token!</h1>
    <h2>What would you like to do next?</h2>
    <ul>
        <li><a href="/profile"> Get account profile</a></li>
        <li><a href="/emailprofile"> Get gmail profile </a></li>
        <li><a href="/gmail"> Go to Gmail example</a></li>
        </ul>
    <pre>
    """ + pformat(session['oauth_token'], indent=4) + """
    </pre>
    """

@app.route("/gmail", methods=["GET"])
def getMail():
    params = {
        "q": "!label: chat",
        "maxResults": 30
    }
    listMail = messages.listMessage(session['user']['id'], google, params).json()

    emailList = []
    test = []
    email = {}
    params = {
        "fields": "id,labelIds,payload/headers,snippet,threadId",
    }
    for item in listMail['messages']:
        emailList.append('https://www.googleapis.com/gmail/v1/users/' + session['user']['id'] + '/messages/' + item['id'])
    to_fetch = (grequests.get(url, params=params, session=google) for url in emailList)
    response = []
    for mail in grequests.map(to_fetch):
        get_email = mail.json()
        for header in get_email['payload']['headers']:
            if header['name'] == 'Subject':
                email['subject'] = header['value']
        email['labelID'] = get_email['labelIds']
        email['snippet'] = get_email['snippet']
        test.append(email.copy())
    #return json.dumps(test)
    return render_template('email_panel.html', user = session['user'], emailList = test)

@app.route("/emailprofile", methods=["GET"])
def getGmailProfile():
    response = google.get('https://www.googleapis.com/gmail/v1/users/' + session['user']['id'] + '/profile').json()
    session['last_check'] = response['historyId']
    return jsonify(response)

@app.route("/refresh")
def refreshGmail():
    params = {"startHistoryId": session['last_check']}
    response = google.get(
        'https://www.googleapis.com/gmail/v1/users/' + session['user']['id'] + '/history',
        params = params
    ).json()
    session['last_check'] = response['historyId']
    if 'messages' in response:
        return getMail()
    print "Nothing to Update"
    return getMail()

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    app.secret_key = os.urandom(24)
    app.run(debug=True)
