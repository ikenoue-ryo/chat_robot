import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
GNAVI_API_KEY = os.environ.get("GNAVI_API_KEY")
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")