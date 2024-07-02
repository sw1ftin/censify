import json
import os.path
import urllib.request as url


def get_badwords() -> None:
    badwords_links = json.load(open('badwords_links.json'))
    for language in badwords_links.keys():
        if not os.path.exists(f"badwords/{language}.txt"):
                url.urlretrieve(
                    badwords_links[language],
                    f"badwords/{language}.txt"
                )


if __name__ == "__main__":
    get_badwords()
