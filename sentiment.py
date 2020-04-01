# this pythonfile plays a song based on a emotion

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

def play_song_emotion(emotion, token):
    # takes as input a string from one of the emotions and token
    # returns None if emotion is not known
    # plays a song with that mood if emotion is known and prints text
    emotion = str(emotion).upper()  
    emotion_list = ["HAPPY", "SAD", "RELAX", "ANGRY", "SLEEP", "ENERGETIC"]
    
    if emotion not in emotion_list:
        return None
    
    else:
    
        sp = spotipy.Spotify(auth=token)
        options = {"HAPPY" : ("sp.start_playback(None, 'spotify:playlist:37i9dQZF1DWSf2RDTDayIx')", "What do you think of this song?")
                ,"SAD" : ("sp.start_playback(None, 'spotify:playlist:54ozEbxQMa0OeozoSoRvcL')", "What do you think of this song?")
                ,"RELAX" : ("sp.start_playback(None, 'spotify:playlist:0RD0iLzkUjrjFKNUHu2cle')", "What do you think of this song?")
                ,"ANGRY" : ("sp.start_playback(None, 'spotify:playlist:6ft4ijUITtTeVC0dUCDdvH')", "What do you think of this song?")
                ,"SLEEP" : ("sp.start_playback(None, 'spotify:playlist:37i9dQZF1DWStLt4f1zJ6I')", "What do you think of this song?")
                ,"ENERGETIC" : ("sp.start_playback(None, 'spotify:playlist:0gFLYrJoh1tLxJvlKcd5Lv')", "What do you think of this song?")
                }
        cmd, mess = options[emotion]
        print(mess)
        sp.shuffle(True, device_id=None)
        exec(cmd)
        return

def play_song_positiviy(score, token):
    score = float(score)
    sp = spotipy.Spotify(auth=token)
    if score < -0.9:
        mood = 'EXTREMELY NEGATIVE'
    if score > -0.9 and score <= -0.7:
        mood = 'VERY NEGATIVE'
    if score > -0.7 and score <= -0.5:
        mood = 'QUITE NEGATIVE'
    if score > -0.5 and score <= -0.3:
        mood =  'NEGATIVE'
    if score > -0.3 and score <= -0.1:
        mood = 'SOMEWHAT NEGATIVE'
    if score > -0.1 and score <= 0.1:
        mood = 'NEUTRAL'
    if score > 0.1 and score <= 0.3:
        mood = 'SOMEWHAT POSITIVE'
    if score > 0.3 and score <= 0.5:
        mood = 'POSITIVE'
    if score > 0.5 and score <= 0.7:
        mood = 'QUITE POSITIVE'
    if score > 0.7 and score <= 0.9:
        mood = 'VERY POSITIVE'
    if score > 0.9:
        mood = 'EXTREMELY POSITIVE'

    print('You seem {}'.format(mood))
    if score < 0:
        sp.shuffle(True, device_id=None)
        sp.start_playback(None, 'spotify:playlist:7HCXp5mTEkbwb9hYq2JTmO') # starts playing a song from a negative playlist
        print('What do you think about this? It is a song from a Sad-playlist')
    elif score > 0.1:
        sp.shuffle(True, device_id=None)
        sp.start_playback(None, 'spotify:playlist:37i9dQZF1DWUAZoWydCivZ') # starts playing a song from a positive
        print('What do you think about this? It is a song from a Positive-playlist')
    else:
        sp.shuffle(True, device_id=None)
        sp.start_playback(None, 'spotify:playlist:0RD0iLzkUjrjFKNUHu2cle') # starts playing a song from the Relax playlist
        print('What do you think about this? It is a song from a Relax-playlist')
    return

