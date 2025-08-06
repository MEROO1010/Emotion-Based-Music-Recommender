import streamlit as st
import cv2
from deepface import DeepFace
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-library-read"
))

st.title("🎵 Emotion-Based Music Recommender")

# Webcam capture
run = st.checkbox("Start Webcam")
FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    
    # Emotion detection & playlist recommendation
    try:
        emotion = DeepFace.analyze(frame, actions=['emotion'])['dominant_emotion']
        playlist_id = EMOTION_PLAYLISTS[emotion]
        playlist = sp.playlist(playlist_id)
        st.success(f"🎶 Recommended Playlist: {playlist['name']}")
    except:
        pass

cap.release()
