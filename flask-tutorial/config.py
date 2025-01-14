import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE = os.getenv('DATABASE')
