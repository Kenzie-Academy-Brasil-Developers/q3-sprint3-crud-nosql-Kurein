from flask import Flask
from app.routes import init_app

import pymongo
import datetime
import os

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client[os.getenv("DB_NAME")]

def create_app():
    app = Flask(__name__)

    init_app(app)

    return app