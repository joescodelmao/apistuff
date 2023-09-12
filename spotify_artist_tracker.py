import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from difflib import get_close_matches

# Use your own credentials from your Spoitfy App
CLIENT_ID = '14f2a67334ad4727b8602de10e2ee3a0'
CLIENT_SECRET = '8f6960ecade6459386cce40a90d31867'

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
        
def suggest_similar_artists(artist_name):
    # Use difflib to suggest similar artist names
    artist_names = [artist['name'] for artist in sp.search(q='', type='artist')['artists']['items']]
    suggestions = get_close_matches(artist_name, artist_names)
    return suggestions

def get_top_tracks(artist_id):
    # Get the top tracks for the artist
    top_tracks = sp.artist_top_tracks(artist_id)
    return top_tracks['tracks']

def main():
    while True:
        artist_name = input("Enter the name of the artist (or 'exit' to quit): ")
        
        if artist_name.lower() == 'exit':
            break
        
        artist_id = get_artist_id(artist_name)

        if artist_id:
            top_tracks = get_top_tracks(artist_id)
            print(f"Top tracks by {artist_name}:")
            for track in top_tracks:
                print(f"{track['name']} - Popularity: {track['popularity']}")
        else:
            print(f"Artist '{artist_name}' not found on Spotify.")

if __name__ == "__main__":
    main()
