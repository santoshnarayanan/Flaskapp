from flask import Flask


class Config(object):
    pass


class ProdConfig(object):
    pass


class DevConfig(object):
    # SQLALCHEMY_ECHO = True
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Password123!@/DbFlaskApps"
     SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"