# app.py

from flask import Flask 
from urllib.parse import quote 

def create_app():
    app = Flask(__name__)
    x=10
    y=10000
    z=38383

    @app.route('/')
    def home():
        return 'GFG 27th jan pipeline run 123'

    return app

def a():
    a()
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
