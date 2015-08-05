from flask import render_template
from app import app
import json
from app.news import *

@app.route('/')
@app.route('/index')
def index():
    results = create_geojson()
    return render_template('map.html', dumps=results)

