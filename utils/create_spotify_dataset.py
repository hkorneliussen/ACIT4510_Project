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
my_file = open("/content/gdrive/MyDrive/Colab Notebooks/ACIT/4510 - statistical learning/spotify_genres.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
genres = data.split("\n,")
print(genres)
my_file.close()
