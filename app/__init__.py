from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

# load environment variables .env file
load_dotenv()


# load screet key from environment variable
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


# load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)





from app.routes.root import *
from app.routes.admin import *
from app.models.user import *
from app.models.admin import *