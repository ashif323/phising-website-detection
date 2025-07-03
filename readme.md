# Phishing Website Detection

## 🔍 Overview
This project detects whether a given website URL is **phishing or legitimate** using machine learning (Random Forest Classifier).

## 📂 Dataset
- **Source:** https://archive.ics.uci.edu/dataset/327/phishing+websites
- **Features:** URL length, presence of '@', prefix-suffix in domain, HTTPS token, subdomains, SSL certificate validity, etc.
- **Target:** 1 (Phishing), -1 (Legitimate)

## ⚙️ Libraries Used
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib
- flask (for web integration)

## 💻 Running the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/ashif323/phising-website-detection.git
    cd phising-website-detection
    ```

2. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Jupyter notebook to train model.

4. For web app:
    ```bash
    python app.py
    ```

## 🚀 Future Work
- Integrate dynamic URL feature extraction.
- Deploy on Heroku/Render for public use.

## 👤 Author
- **Mohammad Ashif Iqbal**
