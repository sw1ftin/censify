import time
import requests
from icecream import ic
from json import loads
from urllib.parse import quote_plus
from better_profanity import profanity

with open('banned_artists.txt', 'r') as f:
    banned_artists = [i.replace('\n', '') for i in f.readlines() if not i.startswith('#')]


def get_lyrics(song: list[str, bool, int]) -> str:
    name = quote_plus(song[0])
    track = quote_plus(song[1])
    album = quote_plus(song[3])
    duration = quote_plus(str(song[4]))
    link = f"https://lrclib.net/api/get?artist_name={name}&track_name={track}&album_name={album}&duration={duration}"
    while True:
        try:
            request_link = loads(requests.get(link).text)
            break
        except requests.exceptions.ConnectionError:
            ic("ERROR WITH CONNECTION, RETRYING IN 5 SECONDS")
            time.sleep(5)
    return request_link.get("plainLyrics")


def check_song(song: list[str, bool, int]) -> bool:
    ic(song)
    if song[2]:
        return False
    lyrics = get_lyrics(song)
    if lyrics is not None:
        if song[0] in banned_artists:
            return False
        if not profanity.contains_profanity(lyrics):
            return True
    return False
