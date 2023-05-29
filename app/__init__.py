from flask import Flask
import sys

app = Flask(__name__)

if sys.platform != 'darwin':
# Windows pathing
    UPLOAD_FOLDER = 'app\static\images'
# Mac pathing
else:
    UPLOAD_FOLDER = 'app/static/images'
    
from app import routes