from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Setup DB connection
    mongo.init_app(app, "mongodb://localhost:27017/chat-db")

    from . import api
    app.register_blueprint(api.bp)

    return app