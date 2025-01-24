import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    SPOTIFY_CLIENT_ID = os.getenv('db61f352fa944726851809d13da14d5a')
    SPOTIFY_CLIENT_SECRET = os.getenv('bc5760d001d341c68909dfd95573e878')
