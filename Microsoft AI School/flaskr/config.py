import os
from dotenv import load_dotenv

# 학습 당시에는 dotenv 사용 안 했음.
# SECRET_KEY 값 동일, SQLITE DB 파일명 다른 건 문제 소지 전혀 없음.
load_dotenv(verbose=True)
BASEDIR = os.path.dirname(__file__)
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE = os.getenv('DATABASE')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASEDIR, DATABASE)}'
