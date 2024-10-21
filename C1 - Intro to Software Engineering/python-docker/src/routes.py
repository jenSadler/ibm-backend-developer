from flask import Flask
from functions import greet

def register_routes(app: Flask):

    @app.route('/')
    def homepage():
        return greet()