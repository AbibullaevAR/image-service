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
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
BASE_DOWNLOAD_HOST = os.environ.get('BASE_DOWNLOAD_HOST')
MAX_CONTENT_LENGTH = 5 * 1024 * 1024
UPLOAD_LINK_LIFE_TIME = int(os.environ.get('UPLOAD_LINK_LIFE_TIME'))
DOWNLOAD_LINK_LIFE_TIME = int(os.environ.get('DOWNLOAD_LINK_LIFE_TIME'))
MAX_WIDTH_RESIZE = int(os.environ.get('MAX_WIDTH_RESIZE'))
MAX_HEIGHT_RESIZE = int(os.environ.get('MAX_HEIGHT_RESIZE'))