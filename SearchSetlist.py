import pprint
import sys

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

import requests
import os
import json

import SpotifyPlaylist

#Get the MusicBrainz ID for the artist
def getArtistID(header, name):
    #Replace any spaces with %20.
    artist = name.replace(" ", "%20")
    url = "https://api.setlist.fm/rest/1.0/search/artists?artistName=" + artist + "&p=1&sort=relevance"
    response = requests.get(url, headers=header, verify=True)
    data = response.json()
    for key in data['artist']:
        return key['mbid']

#Get the MusicBrainz ID for the venue
def getCityID(header):
    venue = raw_input('Enter the venue name: ')
    #Replace any spaces with %20.
    city = venue.replace(" ", "%20")
    url = "https://api.setlist.fm/rest/1.0/search/venues?venueName=" + venue + "&p=1&sort=relevance"
    response = requests.get(url, headers=header, verify=True)
    data = response.json()
    for key in data['city']:
        return key['mbid']

#Get a setlist
def getArtistSetlist(artistID, header):
    url = "https://api.setlist.fm/rest/1.0/artist/" + artistID + "/setlists"
    response = requests.get(url, headers=header, verify=True)
    data = response.json()
    if(response.ok):
        #TODO: put in for loop to go through the pages so to get the full data of setlists
        for key in data['setlist']:
            #Get the first setlist that contains more than 0 songs so to not get back a list of a not performed concert yet
            if len(key.get('sets').get('set')) > 0:
                return key
    else:
        return response

def getVenueSetlist(cityID, header):
    url = "https://api.setlist.fm/rest/1.0/search/venue/" + cityID + "/setlists"
    response = requests.get(url, headers=header, verify=True)
    data = response.json()
    if(response.ok):
        for key in data['setlist']:
            #Get the first setlist that contains more than 0 songs so to not get back a list of a not performed concert yet
            if len(key.get('sets').get('set')) > 0:
                return key
    else:
        return response