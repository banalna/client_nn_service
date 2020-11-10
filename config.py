# -*- coding: utf-8 -*-

import os

# for local start
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Dev preferences
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    # App preferences
    LANGUAGES = ['en', 'ru']

    # For Heroku
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    DETECT_FACES_URL_MODELS = {
        'age_model': os.environ.get('AGE_MODEL'),
        'gender_model': os.environ.get('GENDER_MODEL'),
        'ethnicity_model': os.environ.get('ETHNICITY_MODEL')
    }

    ALLOWED_EXTENSIONS_PHOTO = {'png', 'jpg', 'jpeg', 'gif'}
    PROCESSING_API = os.environ.get('PROCESSING_API')
