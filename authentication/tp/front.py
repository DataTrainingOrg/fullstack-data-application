import logging

from flask import Flask, g, request, make_response, session, redirect
import json
from flask_oidc import OpenIDConnect

from os.path import join, dirname, realpath
import requests

UPLOADS_PATH = join(dirname(realpath(__file__)), 'client_secrets.json')
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

print(UPLOADS_PATH)
app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': UPLOADS_PATH,
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'master',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})


oidc = OpenIDConnect(app)

@app.before_request
def before_request():
    if oidc.user_loggedin:
        pass
    else:
        g.user = None


@app.route('/')
def hello_world():
    if oidc.user_loggedin:
        return ('Hello, %s, <a href="/private">See private</a> '
                '<a href="/logout">Log out</a>') % \
            oidc.user_getfield('preferred_username')
    else:
        return 'Welcome anonymous, <a href="/private">Log in</a>'


@app.route('/private')
@oidc.require_login
def hello_me():
    """Example for protected endpoint that extracts private information from the OpenID Connect id_token.
       Uses the accompanied access_token to access a backend service.
    """

    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])

    username = info.get('preferred_username')
    email = info.get('email')
    user_id = info.get('sub')

    if user_id in oidc.credentials_store:
        try:
            from oauth2client.client import OAuth2Credentials
            access_token = OAuth2Credentials.from_json(oidc.credentials_store[user_id]).access_token
            headers = {'Authorization': 'Bearer %s' % (access_token)}
            # YOLO
            greeting = requests.get('http://127.0.0.1:1235/protected', headers=headers).text
        except:
            greeting = "Hello %s" % username


    return ("""%s your email is %s and your user_id is %s!
               <ul>
                 <li><a href="/">Home</a></li>
                 <li><a href="//localhost:8080/auth/realms/master/account?referrer=flask-app&referrer_uri=http://localhost:5000/private&">Account</a></li>
                </ul>""" %
            (greeting, email, user_id))


@app.route('/logout')
def logout():
    """Performs local logout by removing the session cookie."""

    res = make_response('Hi, you have been logged out! <a href="/">Return</a>')
    session.clear()
    oidc.logout()
    requests.get("http://localhost:8080/auth/realms/master/protocol/openid-connect/logout")
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)