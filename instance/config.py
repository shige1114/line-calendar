from instance.postgres import SQLALCHEMY_DATABASE_URI as URI

DEBUG = True
# SECRET_KEY is generated by os.urandom(24).
SECRET_KEY = 'aaaa'
STRIPE_API_KEY = 'aaaaa'

SQLALCHEMY_DATABASE_URI = URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
