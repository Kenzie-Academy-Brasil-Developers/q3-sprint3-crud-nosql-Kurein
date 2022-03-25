from flask import Flask
from .posts_routes import posts_routes

def init_app(app: Flask):
    
    posts_routes(app)