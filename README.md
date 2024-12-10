# Censify

Censify is a utility tool for censoring tracks from a Spotify playlist. It allows you to create a new playlist using censorship.

> [!NOTE]  
> https://github.com/censify-app/censify-app

## Getting Started

To use Censify, you need to create a Spotify Developer App and set up your `config.ini` file. Additionally, make sure to add `http://localhost:8888/callback` to the list of authorized redirect URIs in your app settings.

1. Create a Spotify Developer App:
   - Go to [https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard/) and create a new app.
   - Add `http://localhost:8888/callback` to the list of authorized redirect URIs in your app settings.
   - Note down your `client_id` and `client_secret` for the app.

2. Configure your `config.ini`:
   - In the `config.ini` file, add your Spotify app credentials:
     ```
     [spotify]
     client_id = YOUR_CLIENT_ID
     client_secret = YOUR_CLIENT_SECRET
     ```

3. Install dependencies by running `pip install -r requirements.txt`.
4. Add the unwanted artists to the `banned-artists.txt` file.
5. Run the script `censify.py` to censor the playlist.

## Configuration

In the `banned-artists.txt` file, add the names of artists you want to censor, each on a new line.

## Dependencies

- Python 3.x
- Spotipy
- configparser
- requests

## Author

Created by [sw1ftin](https://github.com/sw1ftin)

## License

This project is licensed under the [MIT License](LICENSE).
