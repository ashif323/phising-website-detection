from flask import Flask, render_template, request
import joblib
import numpy as np
from feature_extractor import extract_features

app = Flask(__name__)

# Load model bundle
model_bundle = joblib.load('phishing_model.pkl')
model = model_bundle['model']
features_list = model_bundle['features']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = extract_features(url)

    if len(features) != len(features_list):
        return render_template('result.html', prediction="Feature extraction mismatch. Expected {} features, got {}.".format(len(features_list), len(features)))

    features_np = np.array([features])
    prediction = model.predict(features_np)[0]

    if prediction == 1:
        result = "⚠️ Phishing Website Detected"
    else:
        result = "✅ Legitimate Website"

    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
