import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

justin_uri = 'spotify:artist:1uNFoZAHBGtllmzznpCI3s'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='a538e36f54ab4e678b89e639ed5502c1',
                 client_secret='f077ad56247f4a4a80edb31d416b36d7'))

results = spotify.artist_albums(justin_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])