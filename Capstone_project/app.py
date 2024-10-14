from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('rf_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input from the request
        data = request.json

        # Extract the features from the input JSON and convert them into an array
        input_data = np.array([data['tenure'], data['MonthlyCharges'], data['TotalCharges']]).reshape(1, -1)

        # Make prediction using the loaded model
        prediction = model.predict(input_data)[0]

        # Return the prediction in JSON format
        return jsonify({'churn_prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
