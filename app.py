from flask import Flask, render_template, request
import joblib
import feature_extractor  # Your own script for extracting features
import pandas as pd

app = Flask(__name__)

# Load the model bundle (model + feature names)
model_bundle = joblib.load('model.pkl')
model = model_bundle['model']
expected_features = model_bundle['features']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    
    # Extract features using your custom function
    features = feature_extractor.extract_features(url)

    # Create a DataFrame with the correct feature order
    data = pd.DataFrame([features])

    # Align columns to expected features, fill missing ones with 0
    data = data.reindex(columns=expected_features, fill_value=0)

    # Predict using the trained model
    result = model.predict(data)[0]
    prediction = "Phishing Website 🚫" if result == 1 else "Legitimate Website ✅"

    return render_template('index.html', prediction=prediction, url=url)

if __name__ == '__main__':
    app.run(debug=True)
