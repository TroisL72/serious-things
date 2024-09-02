import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = 'dd2d1fa01f334bca967eb8d848fb5de3'
client_secret = '6697b93cfa1c412da35947475287c22d'
redirect_uri = 'https://congnghe.com/'
scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

time_range = 'short_term'  # Options: 'short_term', 'medium_term', 'long_term'
results = sp.current_user_top_tracks(limit=10, time_range=time_range)
tracks = results['items']


with open('Top tracks.txt', 'w', encoding='utf-8') as file:
    for idx, track in enumerate(tracks):
        track_name = track['name']
        artist_names = [artist['name'] for artist in track['artists']]
        album_name = track['album']['name']
        track_url = track['external_urls']['spotify']
        file.write(f'Rank: {idx + 1}\n')
        file.write(f'Track: {track_name}\n')
        file.write(f'Artists: {", ".join(artist_names)}\n')
        file.write(f'Album: {album_name}\n')
        file.write(f'Track URL: {track_url}\n')
        file.write('---\n')

print("Complete !")