#!/usr/bin/env python3
"""
Flask module to run the api
"""

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
