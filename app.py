from flask import Flask, render_template, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Spotify client
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=app.config['db61f352fa944726851809d13da14d5a'],
        client_secret=app.config['bc5760d001d341c68909dfd95573e878']
    )
)

def get_track_info(track_url):
    try:
        # Extract track ID from URL
        track_id = track_url.split('/')[-1].split('?')[0]
        
        # Get track information
        track = spotify.track(track_id)
        
        return {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'cover_url': track['album']['images'][0]['url'],
            'preview_url': track['preview_url'],
            'duration': track['duration_ms'] // 1000
        }
    except Exception as e:
        return {'error': str(e)}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/downloader')
def downloader():
    return render_template('downloader.html')

@app.route('/get-track-info', methods=['POST'])
def process_url():
    spotify_url = request.form.get('spotify_url')
    if not spotify_url:
        return jsonify({'error': 'No URL provided'})
    
    track_info = get_track_info(spotify_url)
    return jsonify(track_info)

if __name__ == '__main__':
    app.run(debug=True)
