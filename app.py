from flask import Flask, render_template, request, jsonify, make_response
from ga_tsp import run_ga
import csv
import io
import requests

app = Flask(__name__)

# Replace with your real OpenRouteService API key
ORS_API_KEY = '5b3ce3597851110001cf624802571222ba2841548c50d590a4148c1e'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.json
    coords = data['points']
    result, dist = run_ga(coords)
    return jsonify({'route': result, 'distance': dist})

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

    first = points[route[0]]
    writer.writerow([len(route)+1, first[0], first[1]])

    output.seek(0)
    response = make_response(output.read())
    response.headers["Content-Disposition"] = "attachment; filename=route.csv"
    response.headers["Content-type"] = "text/csv"
    return response

@app.route('/roadroute', methods=['POST'])
def roadroute():
    data = request.json
    coordinates = data['coordinates']  # Format: [[lon, lat], [lon, lat], ...]
    headers = {
        'Authorization': ORS_API_KEY,
        'Content-Type': 'application/json'
    }
    body = {
        "coordinates": coordinates,
        "format": "geojson"
    }
    url = "https://api.openrouteservice.org/v2/directions/driving-car/geojson"
    response = requests.post(url, headers=headers, json=body)
    return response.json()

@app.route('/get_place_names', methods=['POST'])
def get_place_names():
    coords = request.json['coords']
    names = []

    for lat, lon in coords:
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
        res = requests.get(url, headers={"User-Agent": "SwiftRoute"})
        if res.status_code == 200:
            json_data = res.json()
            names.append(json_data.get("display_name", "Unknown"))
        else:
            names.append("Unknown")

    return jsonify(names)

@app.route('/nearby_places', methods=['POST'])
def nearby_places():
    data = request.json
    lat, lon = data['center']
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
      node["amenity"="hospital"](around:3000,{lat},{lon});
      node["tourism"="hotel"](around:3000,{lat},{lon});
      node["amenity"="fuel"](around:3000,{lat},{lon});
    );
    out center;
    """
    response = requests.post(overpass_url, data=query.encode("utf-8"))
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
