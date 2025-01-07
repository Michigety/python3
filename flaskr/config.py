import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
BASEDIR = os.path.dirname(__file__)
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE = os.getenv('DATABASE')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASEDIR, DATABASE)}'
