from flask import Flask, render_template, request, jsonify
from ga_tsp import run_ga

from flask import Flask, render_template, request, jsonify, make_response
import csv
import io


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Loads the web page

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.json              # Get JSON from frontend
    coords = data['points']         # Extract coordinates
    result, dist = run_ga(coords)   # Run Genetic Algorithm
    return jsonify({'route': result, 'distance': dist})  # Send result back




@app.route('/export', methods=['POST'])
def export_csv():
    data = request.json
    points = data['points']
    route = data['route']
    distance = data['distance']

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Stop Number', 'Latitude', 'Longitude'])

    for i, index in enumerate(route):
        lat, lon = points[index]
        writer.writerow([i+1, lat, lon])

    # Optionally add the return to starting point
    first = points[route[0]]
    writer.writerow([len(route)+1, first[0], first[1]])

    output.seek(0)
    response = make_response(output.read())
    response.headers["Content-Disposition"] = "attachment; filename=route.csv"
    response.headers["Content-type"] = "text/csv"
    return response


if __name__ == '__main__':
    app.run(debug=True)
