import pprint
import sys

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

import requests
import json

#spotify API
spotCONSUMER_KEY = '3817588cd345435c86c9a60e6c0cb70a'
spotCONSUMER_SECRET = 'ce6c55f9f3c343bb919d917257661a3b'
spotREDIRECT_URL = 'SpotifyTestApp://callback'

#Header for Spotify
username = ""
token = util.prompt_for_user_token(
    username,
    scope = 'playlist-modify-private playlist-modify-public',
    #Enter Spotify API ID
    client_id ='3817588cd345435c86c9a60e6c0cb70a',
    #Enter Spotify API Secret
    client_secret ='ce6c55f9f3c343bb919d917257661a3b',
    #Enter Spotify API Redirect URI
    redirect_uri='SpotifyTestApp://callback'
)

#Create a session token for spotipy
def createSpotifyToken(token):
    spotify = spotipy.Spotify(auth=token)
    return spotify

def searchTermsArtist(name):
    results = spotipy.search(q='artist:' + name, type='artist')
    print results
