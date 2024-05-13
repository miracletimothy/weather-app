from flask import jsonify, render_template, request
from . import app
from .scraper import get_weather_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    if request.method == 'GET':
        location = request.args.get('location')
        if location:
            # Call the scraper function to get weather data
            weather_data = get_weather_data(location)
            return jsonify(weather_data)
        else:
            return jsonify({'error': 'No location provided'}), 400
    return render_template('index.html')
