import random
import string
import urllib
import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.utils.timezone import utc

from rest_framework import viewsets
import requests

from .models import User, Oauth2Token
from .utils import decode_b64
from goma.settings.base import * 

class UserViewSet(viewsets.ModelViewSet):
    model = User

def index(request):
    template = 'pages/app/accounts/index.html'

    return render(
        request,
        template,
        {}
    )


def portal(request):
    template = 'layouts/login_base.html'

    return render(
        request,
        template,
        {}
    )

# Generates the initial request
def oauth2login(request):
    # Todo
    # 1. generate state value
    state = ''.join(random.choice(string.ascii_uppercase+string.digits) for x in xrange(32))
    # 3. store state value to session (hope and pray the session stays the same)
    request.session['state'] = state
    # 4. redirect the user to https://accounts.google.com/o/oauth2/auth. with a GET request
    auth_url = "https://accounts.google.com/o/oauth2/auth?"
    auth_params = {
        'client_id'     : GOOGLE_CLIENT_ID,
        'response_type' : 'code',
        'scope'         : urllib.quote(GOOGLE_OAUTH_SCOPE),
        'redirect_uri'  : GOOGLE_REDIRECT_URI,
        'state'         : state,
        'access_type'   : 'offline',
    }

    full_url = auth_url + urllib.urlencode(auth_params)
    return redirect(full_url)
     # parameters for said request:
    
    # client_id
    # response_type=code
    # scope
    # redirect_uri
    # state

def oauth2callback(request):    
    # Todo
    # 1. Look for code in  the response_
    if 'state' not in request.session or \
       'state' not in request.GET:
        return HttpResponseBadRequest('State token missing')

    if request.session['state'] != request.GET['state']:
        return HttpResponseBadRequest('State token invalid')

    if 'code' not in request.GET:
        return HttpResponseBadRequest('Auth code missing')

    # 2. Make a request POST request with the client_id, client_secret, redirect_uri, access_type, and grant_type
    auth_code = request.GET['code']
    url = GOOGLE_TOKEN_URL
    payload = {
        'client_id'         : GOOGLE_CLIENT_ID,
        'client_secret'     : GOOGLE_CLIENT_SECRET,
        'code'              : auth_code,
        'grant_type'        : 'authorization_code',
        'redirect_uri'      : GOOGLE_REDIRECT_URI,
    }

    try:
        res = requests.post(url, data=payload)
    except Exception, e:
        print e
        return HttpResponseServerError('Could not get access codes from Google')

    contents = res.json()
    # 3. Parse response for access_token and refresh_token
    res.raise_for_status()

    current_time = datetime.datetime.now().replace(tzinfo=utc)
    expires_in = datetime.timedelta(seconds=contents['expires_in'])

    expiry_time = current_time+expires_in
    access_token = contents['access_token']
    if 'refresh_token' in contents:
        refresh_token = contents['refresh_token']

    # 4. Make requests for other info
    id_token_decoded = decode_b64(contents['id_token'].split('.')[1])
    id_data = json.loads(id_token_decoded)
    user_email = id_data['email']

    # 5. Log user in or register new user
    user, new_user = User.objects.get_or_create(email=user_email)

    # Get the user's OAuth Token object
    token, new_token = Oauth2Token.objects.get_or_create(User=user)
    token.access_token = access_token
    if 'refresh_token' in contents:
        token.refresh_token = refresh_token
    token.expiry_time = expiry_time
    token.save()

    response = {
        'user': user.id,
        'created_user': new_user,
        'token': token.id,
        'created_token': new_token,
        'access_token': token.access_token,
        'refresh_token': token.refresh_token,
        'expiry_time': str(token.expiry_time)
    }
    # 6. Last two steps can be done in the client

    template = 'pages/app/accounts/oauth2result_temp.html'

    return render(
        request,
        template,
        response
    )