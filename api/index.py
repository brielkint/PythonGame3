from flask import Flask, render_template, request, jsonify, url_for
import random
import os
from pathlib import Path

app = Flask(__name__, static_url_path='/static')

# Create a function to get static file paths
def get_static_file(filename):
    static_folder = Path(__file__).parent.parent / 'static'
    return str(static_folder / filename)

# ... rest of your app.py code ...

# Change this part
if __name__ == '__main__':
    app.run() 