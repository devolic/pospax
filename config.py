DEBUG = True

SECRET_KEY = 'arq@lzy0qzs0^n9w#fnczm7x78s5m++azuw^zrafs&mg6gi6y+'

BABEL_DEFAULT_LOCALE = 'th'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'pospax@gmail.com'
MAIL_PASSWORD = ''

BLUEPRINTS = [
]

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/pospax'
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_TRACK_MODIFICATIONS = False
