import configparser
import re

import lyricsgenius
import requests
import spotipy
from better_profanity import profanity
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

config = configparser.ConfigParser()
config.read("config.ini1")
client = {
    "spotify": {
        "id": config.get("spotify", "client_id"),
        "secret": config.get("spotify", "client_secret")
    },
    "genius": {
        "access_token": config.get("genius", "access_token")
    }
}

genius = lyricsgenius.Genius(client['genius']['access_token'])
client_credentials_manager = SpotifyClientCredentials(client_id=client["spotify"]["id"],
                                                      client_secret=client["spotify"]["secret"])
scope = "playlist-modify-private playlist-modify-public"
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                     auth_manager=SpotifyOAuth(client_id=client["spotify"]["id"],
                                               client_secret=client["spotify"]["secret"],
                                               redirect_uri='http://localhost:8888/callback',
                                               scope=scope))

badwords = requests.get("https://raw.githubusercontent.com/bars38/Russian_ban_words/master/words.txt")
profanity.add_censor_words(badwords.text.split('\n'))


def get_lyrics(song: list) -> str:
    artist, title = song
    song = genius.search_song(title, artist)
    return song.lyrics if song else "Lyrics not found"


def extract_playlist_id(playlist_url: str) -> str:
    match = re.search(r'playlist/([a-zA-Z0-9]+)', playlist_url)
    return match.group(1) if match else None


def get_tracklist(playlist_url: str) -> dict:
    return sp.playlist_items(extract_playlist_id(playlist_url))['items']


def get_playlist(playlist_url: str) -> list[list]:
    return [[', '.join([artist['name'] for artist in item['track']['artists']]), item['track']['name'],
             item['track']['uri']] for item in get_tracklist(playlist_url)]


def check_song(song: list[str]) -> bool:
    lyrics = get_lyrics(song[:2])
    if lyrics != 'Lyrics not found':
        if not profanity.contains_profanity(lyrics):
            return True
    return False


def check_playlist(playlist_url: str) -> list[list]:
    return [song for song in get_playlist(playlist_url) if check_song(song)]


def make_playlist(name: str, playlist: str, public: bool = False) -> list[str]:
    new_playlist = sp.user_playlist_create(sp.me()['id'], name, public=public)
    song_list = check_playlist(playlist_url=playlist)
    for song in song_list:
        sp.playlist_add_items(new_playlist['id'], song[2])
    return new_playlist
