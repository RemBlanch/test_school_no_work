#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('../')
from pprint import pformat
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth2Session
import google.calendar.calendar as calendar
import google.calendar.events as events
from google.google_authorization import google_auth
import datetime
import requests

try:
    from flask import (
      Flask,
      redirect,
      render_template,
      request,
      session,
      url_for,
      jsonify,
    )

except ImportError:
    raise RuntimeError('Requirements not set up, see 'Requirements':\n' + __doc__)

os.environ['GOOGLE_CLIENT_ID'] = '1087046004082-2q1diuuse89rt6ahu6mma050jqidmsdu.apps.googleusercontent.com'
os.environ['GOOGLE_CLIENT_SECRET'] = '2k1nKdYteKu_yTJuvuduKvO-'
os.environ['SECRET_KEY'] = 'CHECK_MATE'
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
            'https://www.googleapis.com/auth/calendar.readonly'
]

if app.debug:
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

@app.route('/')
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

@app.route('/callback', methods=['GET'])
def retrieve():
    url_to_redirect = url_for('retrieve', _external=True)
    session['oauth_token'] = google_auth().retrieve_token(app.config['GOOGLE_CLIENT_SECRET'], google)
    return redirect(url_for('.menu'))

@app.route('/menu', methods=['GET'])
def menu():

    session['user'] = google.get('https://www.googleapis.com/oauth2/v1/userinfo').json()

    return '''
    <h1>Congratulations, you have obtained an OAuth 2 token!</h1>
    <h2>What would you like to do next?</h2>
    <ul>
        <li><a href='/listCalendar'>List Calendar</a></li>
        <li><a href='/listCalendarEvents'>List Events from Calendar</a></li>
        <li><a href='/checkState'>Am i free ?</a></li>
    </ul>

    <pre>
    ''' + pformat( session['oauth_token'], indent=4 ) + '''
    </pre>
    <pre>
    ''' + pformat( session['user'], indent=4 ) + '''
    </pre>
    '''

@app.route('/listCalendar')
def list():
    response = calendar().listCalendar(google).json()
    return jsonify(response)

@app.route('/listCalendarEvents')
def listCalendarEvents():
    params = {
        'fields': 'items(id,summary),nextPageToken,nextSyncToken'
    }
    response = calendar().listCalendar(google, params).json()
    return render_template('calendar.html', calendars = response['items'])

@app.route('/mEvents/<url_action>/<calendarId>', methods=['GET'])
def listEventsFromCalendar(url_action, calendarId):
    response = events.listEvents(google, calendarId).json()
    if url_action == 'list':
        return jsonify(response)

    elif url_action == 'delete':
        print 'delete'

    elif url_action == 'create' :
        print 'create'

    else:
        print 'update'

    return jsonify(response)

@app.route('/checkState')
def freeBusy():
    now = datetime.datetime.now().isoformat() + 'Z'
    time = datetime.datetime.now() + datetime.timedelta(minutes=5)
    now2 = time.isoformat() + 'Z'
    data ={
        'timeMin': now,
        'timeMax': now2,
        'timeZone':'Europe/Madrid',
        'items':[
            {
                'id': 'rem.blanch@invoxcontact.com'
            }
        ]
    }
    response = google.post(
        'https://www.googleapis.com/calendar/v3/freeBusy',
        json = data
    )
    return jsonify(response.json())

@app.route('/watcher')
def watcher():

    data = {
        'id': '0123456789-9876543210',
        'type': 'web_hook',
        'address': string,
    }

    response = google.post(
        'https://www.googleapis.com/calendar/v3/users/me/calendarList/watch',
        json = data
    )
    return response.json()

if __name__ == '__main__':
    # This allows us to use a plain HTTP callback
    app.secret_key = os.urandom(24)
    app.run(debug=True)
