import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'this-is-a-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'mssql+pyodbc://@localhost/CustodialFrameworkV3?driver=SQL+Server;Trusted_Connection=Yes',
        'sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
