'''
This python code demonstrates one method of gathering spotify songs and features. 
The output is a demo_audio_features.csv file, containing spotify songs and featurse.
Due to computational time, this code creates a small version of the dataset. 
The dataset used in the project can be found in the /dataset folder.

based on: https://levelup.gitconnected.com/extracting-and-analysing-spotify-tracks-with-python-d1466fc1dfee
spotify API:  https://developer.spotify.com/dashboard/
'''

#importing modules 
import spotipy #spotify web API wrapper for python
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd #Dataframe
import time #pause execution of loops

#assinging client and secret key to a cariable auth_manager
auth_manager = SpotifyClientCredentials(client_id = '37b046d6f2434a7db5c4abf3b2b5b837',
                                        client_secret = '2b097e6db94f47249f32650fbf7ce7ed')
sp = spotipy.Spotify(auth_manager=auth_manager)


# opening file containing spotify genres
my_file = open("spotify_genres.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text when newline ('\n') is seen.
genres = data.split("\n,")
print(genres)
my_file.close()

#selecting one speficic genre 
genre = genres[0] 

#HELPER FUNCTIONS
#function that obtain track IDs for each song in playlist
def getTrackIDs(user, playlist_id):
  track_ids = []
  
  playlist = sp.user_playlist(user, playlist_id)
    
  for item in playlist['tracks']['items']:
    track = item['track']
    track_ids.append(track['id'])
    
  return track_ids



    

#function that allows us to get features of the tracks in the playlist 
def getTrackFeatures(genre, id):
  track_info = sp.track(id)

  track_features = sp.audio_features(id)
    
  #track info
  genre = genre
  name = track_info['name']
  album = track_info['album']['name']
  artist = track_info['album']['artists'][0]['name']
  release_date = track_info['album']['release_date']
  length = track_info['duration_ms']
  popularity = track_info['popularity'] #calculated based on total number of plays and how recent those plays are

  #track features
  acousticness = track_features[0]['acousticness']
  danceability = track_features[0]['danceability']
  energy = track_features[0]['energy']
  instrumentalness = track_features[0]['instrumentalness']
  key = track_features[0]['key']
  liveness = track_features[0]['liveness']
  loudness = track_features[0]['speechiness']
  mode = track_features[0]['mode']
  speechiness = track_features[0]['speechiness']
  tempo = track_features[0]['tempo']
  time_signature = track_features[0]['time_signature']
  valence = track_features[0]['valence']

  track_data = [genre, name, album, artist, release_date, length,  popularity, acousticness, 
                danceability, energy, instrumentalness, key, liveness, loudness, mode,
                speechiness, tempo, time_signature, valence]
  return track_data    
 
# list to store playlists
playlist_list = []
# getting one playlist 
playlists = sp.search(q=genre, type='playlist', market = 'US', limit=1)
total_playlists = playlists['playlists']['items']
for play in total_playlists:
  items = playlists['playlists']['items']
  playlist_items = items[0]
  playlist_id = playlist_items['id']
  data = [genre, playlist_id]
    
playlist_list.append(data)

# getting track ids for all songs in the playlist
track_ids = []
for elem in playlist_list:
  time.sleep(.3)
  genre = elem[0]
  play_id = elem[1]
  try:
    tracks = getTrackIDs('spotify', play_id)
    for track_id in tracks:
      data = genre, track_id
      [track_ids.append(data) for x in data if x not in track_ids]
  except:
    pass
    
#getting track features 
track_list = []

for elem in track_ids:
  try:
    time.sleep(.3)
    genre = elem[0]
    track_id = elem[1]
    track_data = getTrackFeatures(genre, track_id)
    data = genre, track_data
    [track_list.append(track_data) for x in track_data if x not in track_list]
  except:
    pass 

# generating dataframe
playlist = pd.DataFrame(track_list, columns = 
                                  ['Genre', 'Name', 'Album', 'Artist', 'Release_date', 'Length',  
                                   'Popularity', 'Acousticness', 'Danceability', 'Energy', 
                                   'Instrumentalness', 'Key', 'Liveness', 'Loudness', 'Mode', 
                                   'Speechiness', 'Tempo', 'Time_signature', 'Valence'])
#remove duplicates
playlist = playlist.drop_duplicates()


#writing dataframe to csv file 
playlist.to_csv("original_dataset_demo.csv")


