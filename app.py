from flask import Flask, request, jsonify, send_from_directory, render_template, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests from frontend

# Dummy location pricing dictionary (you can replace with real data or ML model)
location_price_map = {
    "banashankari": 7500,
    "banashankari 2nd stage": 8500,
    "banashankari 3rd stage": 7800,
    "banjara hills": 9500,  # Not in Bangalore – may be Hyderabad?
    "basavanagudi": 9000,
    "bellandur": 7500,
    "bilekahalli": 7200,
    "brookfield": 8000,
    "btm layout": 7800,
    "bakersfield": 7000,  # Assuming as placeholder

    "church street": 12000,
    "cv raman nagar": 7200,
    "cunningham road": 11000,

    "doddakannalli": 7000,

    "electronic city": 5500,
    "electronic city phase 1": 5800,

    "garudachar palya": 7200,

    "hebbal": 7600,
    "hebbal industrial area": 7000,
    "hebbal kempapura": 7400,
    "hsr layout": 8500,

    "jayanagar": 9500,
    "jpnagar": 8000,

    "kammanahalli": 6800,
    "kanakapura road": 6500,
    "kengeri": 5500,
    "koramangala": 10000,
    "kr puram": 6000,
    "kumaraswamy layout": 6500,

    "lavelle road": 12000,

    "malleshwaram": 9500,
    "marathahalli": 7000,
    "murugeshpalya": 7200,

    "neelasandra": 7500,

    "pattandur agrahara": 7000,

    "rajajinagar": 8800,
    "rajiv gandhi nagar": 6200,
    "rangaswamy layout": 6400,
    "rajaji nagar": 8800,

    "sarjapur road": 7800,
    "sanjay nagar": 7600,
    "somasundara palya": 6900,

    "ulsoor": 8500,

    "vrindavan layout": 6800,

    "whitefield": 7800,
    "whitefield east": 7500,

    "yelahanka": 6700,
    "yelahanka new town": 6800
}


@app.route('/predict', methods=['POST'])

@app.route('/')
def home():
    return render_template('index.html')

def predict():
    try:
        data = request.get_json()
        
        bedrooms = int(data.get('bedrooms', 0))
        bathrooms = int(data.get('bathrooms', 0))
        living_area = float(data.get('living_area', 0))
        location = data.get('location', '').strip().lower()
        
        price_per_sqft = location_price_map.get(location, 7000)
        
        base_price = living_area * price_per_sqft
        room_adjustment = bedrooms * 150000 + bathrooms * 100000
        
        predicted_price = base_price + room_adjustment
        predicted_price = round(predicted_price, -3)  # rounded to nearest 1000
        
        return jsonify({"predicted_price": predicted_price})

    except Exception as e:
        return jsonify({"error": "Invalid input or server error", "message": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
