import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CRSF_ENABLED = True
    SECRET_KEY = 'ed3795f5661a586680573a9d'
    #: For local or non-local databases.
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + 'stevenbennett:password@localhost/localdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'ratemymolecule@gmail.com'
    MAIL_PASSWORD = 'ratemymolecule123'
    ADMINS = ['ratemymolecule@gmail.com']


# class DockerConfig(object):
#     DEBUG = False
#     TESTING = False
#     CRSF_ENABLED = True
#     SECRET_KEY = 'ed3795f5661a586680573a9d'
#     #: For local or non-local databases.
#     SQLALCHEMY_DATABASE_URI = 'postgresql://' + 'stevenbennett:@localhost/localdb'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = 1
#     MAIL_USERNAME = 'ratemymolecule@gmail.com'
#     MAIL_PASSWORD = 'ratemymolecule123'
#     ADMINS = ['ratemymolecule@gmail.com']
#     # Database connection information.
#     user = os.environ['POSTGRES_USER']
#     password = os.environ['POSTGRES_PASSWORD']
#     host = os.environ['POSTGRES_HOST']
#     database = os.environ['POSTGRES_DB']
#     port = os.environ['POSTGRES_PORT']
#     SQLALCHEMY_DATABASE_URI = DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'