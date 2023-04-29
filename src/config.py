import os
from pathlib import Path
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

DEBUG = bool(os.environ.get('DEBUG'))
SECRET_KEY = os.environ.get('SECRET_KEY')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=36500)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads/')
BASE_DOWNLOAD_HOST = os.environ.get('BASE_DOWNLOAD_HOST')
MAX_CONTENT_LENGTH = 5 * 1024 * 1024