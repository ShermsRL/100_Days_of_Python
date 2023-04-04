from bs4 import BeautifulSoup
import requests
import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# Get access token
# sp = spotipy.SpotifyOAuth(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri="http://example.com")
# sp.get_auth_response()
# sp.get_cached_token()
# print(sp.get_access_token())

# Get user ID
# sp = spotipy.Spotify("-")
# print(sp.current_user())


SPOTIFY_ID = "-"
SPOTIFY_SECRET = "-"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")
top_100_link = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/#")
soup = BeautifulSoup(top_100_link.text, "html.parser")

song_title = [song.get_text() for song in soup.find_all(id="title-of-a-story")]
song_title = song_title[6:403:4]
song_title = [song[14:-5] for song in song_title]

scope = "playlist-modify-private"

authentications = spotipy.oauth2.SpotifyOAuth(
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_SECRET,
    scope=scope,
    redirect_uri="http://example.com"
)

sp = spotipy.Spotify(client_credentials_manager=authentications)

# sp.user_playlist_create(
#     user='bef55w1srhur81zv042gqtbda',
#     name=f"{date} Billboard 100",
#     public="False",
#     collaborative="False"
# )

playlist_id = sp.user_playlists(user= '-')['items'][0]['external_urls']['spotify'][34:]

song_uri = [[sp.search(q=f"{song}", type="track", limit=1)['tracks']['items'][0]['uri'][14:]] for song in song_title]

for uri in song_uri:
    sp.playlist_add_items(playlist_id=playlist_id, items=uri, position=None)

# How to get it to work regardless of rate limit?

