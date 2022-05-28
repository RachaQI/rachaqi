import environ

from rachaqi.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASE_URL = 'postgres://oulutkwdvivxjo:d7a9da3c929be9381cce2d52b51052eb84c12402ca6a580f4b6bbc07b3cbf0c1@ec2-52-204' \
               '-195-41.compute-1.amazonaws.com:5432/d2pg7ih5b7tugt '
