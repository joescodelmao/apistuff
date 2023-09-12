import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = 'f29007bf5afe4b219f8c5e6f268925c9'
CLIENT_SECRET = '5963bd086f584705a246d8a22ba60245'

# Initialize the Spotify API client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_artist_id(artist_name):
    # Search for the artist and return their ID
    result = sp.search(q=artist_name, type='artist')
    if result['artists']['items']:
        return result['artists']['items'][0]['id']
    else:
        return None

def get_top_tracks(artist_id):
    # Get the top tracks for the artist
    top_tracks = sp.artist_top_tracks(artist_id)
    return top_tracks['tracks']

def main():
    artist_name = 'Drake'
    artist_id = get_artist_id(artist_name)

    if artist_id:
        top_tracks = get_top_tracks(artist_id)
        print(f"Top tracks by {artist_name}:")
        for track in top_tracks:
            print(f"{track['name']} - Popularity: {track['popularity']}")

if __name__ == "__main__":
    main()
