from flask import *
import pickle
import os
from flask_cors import CORS

# LOAD THE TRAINED MODEL
# This ensures portability across systems
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')

# Load the model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

print(f"Model loaded successfully from {MODEL_PATH}")

app = Flask(__name__)
CORS(app)

@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json()
    # validate the input
    required_fields = ['BMI','BloodPressure']
    for field in required_fields:
        if not data or field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400
        
    # extract and prepare inputs
    bmi=float(data['BMI'])
    bp=float(data['BloodPressure'])

    input_values=[bmi,bp]
    prediction = (model.predict([input_values]))


    # expert rules
    if prediction > 125:
        risk='high'
        risk_msg='you may be at a very high risk of having diabetes, consult a healthcare provider'
    elif prediction >100:
        risk='moderate'
        risk_msg='you classified as moderate risk,concider making lifestyle adjustment and monitor your health regularly'
    else:
        risk='low'
        risk_msg="this suggests a low risk.Keep mainataining a healthy life style"

    return jsonify({"prediction":prediction,"risk":risk,"risk_msg":risk_msg}),200

