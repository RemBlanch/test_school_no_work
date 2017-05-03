#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pformat
import os
import sys
sys.path.append('../')
#import google.google_authorization as google_auth
from google.google_authorization import google_auth
import google.calendar.calendar as calendar
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
    """"""
    return """
    <h1>Congratulations, you have obtained an OAuth 2 token!</h1>
    <h2>What would you like to do next?</h2>
    <ul>
        <li><a href="/profile"> Get account profile</a></li>
        <li><a href="/automatic_refresh"> Implicitly refresh the token</a></li>
        <li><a href="/manual_refresh"> Explicitly refresh the token</a></li>
        <li><a href="/validate"> Validate the token</a></li>
        <li><a href="/revoke"> Revoke the token</a></li>
        <li><a href="/calendar"> Go to Calendar example</a></li>
    </ul>

    <pre>
    """ + pformat(session['oauth_token'], indent=4) + """
    </pre>
    """

@app.route("/automatic_refresh", methods=["GET"])
def refresh():

    credentials = {
        'CLIENT_ID': app.config['GOOGLE_CLIENT_ID'],
        'CLIENT_SECRET': app.config['GOOGLE_CLIENT_SECRET']
    }
    google_auth().automatic_refresh_token(credentials)
    return jsonify(session['oauth_token'])

@app.route("/manual_refresh", methods=["GET"])
def manual_refresh():

    credentials = {
        'CLIENT_ID': app.config['GOOGLE_CLIENT_ID'],
        'CLIENT_SECRET': app.config['GOOGLE_CLIENT_SECRET']
    }
    google_auth().manual_refresh(credentials)
    return jsonify(session['oauth_token'])

@app.route("/validate", methods=["GET"])
def validate():

    response = google_auth().token_validate()
    return jsonify(response)

@app.route("/revoke", methods=["GET"])
def revoke():

    response = google_auth().token_revoke()
    if response:
        return demo()
    else:
        return """
        <h1>Fail to revoke token.</h1>"""

@app.route("/profile", methods=["GET"])
def profile():
    """Fetching a protected resource using an OAuth 2 token."""

    google = OAuth2Session(app.config['GOOGLE_CLIENT_ID'], token=session['oauth_token'])

    return jsonify(google.get(app.config['GOOGLE_OAUTH_USER_INFO']).json())

@app.route("/calendar")
def calendarList():
    """ Obtain list of user calendars """
    credentials = {
        'CLIENT_ID': app.config['GOOGLE_CLIENT_ID']
    }
    eventlist = calendar.listCalendar(credentials).json()
    return render_template('calendar.html', calendars = eventlist['items'])

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback

    app.secret_key = os.urandom(24)
    app.run(debug=True)
