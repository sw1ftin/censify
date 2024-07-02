from lyrics import *
from badwords import *

import configparser
import re
import spotipy
from icecream import ic
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

config = configparser.ConfigParser()
config.read("config.ini")
client = {
    "spotify": {
        "id": config.get("spotify", "client_id"),
        "secret": config.get("spotify", "client_secret"),
    }
}

client_credentials_manager = SpotifyClientCredentials(client_id=client["spotify"]["id"],
                                                      client_secret=client["spotify"]["secret"])
scope = "playlist-modify-private playlist-modify-public"
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                     auth_manager=SpotifyOAuth(client_id=client["spotify"]["id"],
                                               client_secret=client["spotify"]["secret"],
                                               redirect_uri='http://localhost:8888/callback',
                                               scope=scope))

get_badwords()

for file in os.listdir("badwords"):
    with open(os.path.join("badwords", file), "r", encoding='utf-8') as f:
        profanity.add_censor_words(f.readlines())


def extract_playlist_id(playlist_url: str) -> str:
    match = re.search(r'playlist/([a-zA-Z0-9]+)', playlist_url)
    return match.group(1) if match else None


def get_tracklist(playlist_url: str) -> dict:
    ic(sp.playlist_items(extract_playlist_id(playlist_url))['total'])
    raw_tracklist = sp.playlist_items(extract_playlist_id(playlist_url))
    tracklist = raw_tracklist['items']
    for part in range(100, raw_tracklist['total'], 100):
        tracklist += sp.playlist_items(extract_playlist_id(playlist_url), offset=part)['items']
    ic(len(tracklist))
    return tracklist


def get_playlist(playlist_url: str) -> list[list]:
    tracklist = get_tracklist(playlist_url)
    return [[', '.join([artist['name'] for artist in item['track']['artists']]),
             item['track']['name'],
             item['track']['explicit'],
             item['track']['album']['name'],
             item['track']['duration_ms'] // 1000,
             item['track']['uri']] for item in tracklist]


def check_playlist(playlist_url: str):
    for song in get_playlist(playlist_url):
        yield [check_song(song), song[5]]


def make_playlist(name: str, playlist_url: str, public: bool = False):
    new_playlist = sp.user_playlist_create(sp.me()['id'], name, public=public)
    for position, result in enumerate(check_playlist(playlist_url)):
        ic(position, result)
        if result[0]:
            sp.playlist_add_items(new_playlist['id'], [result[1]])
            ic(f'ADDED SONG {result}')
    return new_playlist


if __name__ == '__main__':
    make_playlist(name="Test",
                  playlist_url="https://open.spotify.com/playlist/3EOQoQ6GZLMFTWwXfD5Clh?si=b6560977567d4ecf",
                  public=True)
