import re
import joblib
import socket
from urllib.parse import urlparse
import requests

# Load features list from model.pkl
model_bundle = joblib.load('model.pkl')
ALL_FEATURES = model_bundle['features']

def has_dns_record(domain):
    try:
        socket.gethostbyname(domain)
        return 1
    except:
        return -1

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc or parsed.path

    # 1. IP Address in URL
    having_ip = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else -1

    # 2. URL Length
    url_length = len(url)

    # 3. Shortening service
    shortening = 1 if re.search(r'bit\.ly|tinyurl\.com|goo\.gl', url) else -1

    # 4. Abnormal URL (Check if domain not in URL)
    abnormal_url = -1 if domain in url else 1

    # 5. DNS record existence
    dns_record = has_dns_record(domain)

    # 6. Domain registration length (Stubbed logic, needs WHOIS API for real implementation)
    domain_registration_length = -1  # assume phishing (very short reg)

    # 7. Favicon from external domain
    try:
        response = requests.get(url, timeout=2)
        if 'favicon' in response.text:
            favicon = 1 if domain in response.text else -1
        else:
            favicon = -1
    except:
        favicon = -1

    # 8. Google Index (real check needs web scraping or API, here stubbed)
    google_index = 1 if "https://www.google.com/search?q=site:" + domain else -1

    # Fill initial extracted values
    extracted = {
        'having_IP_Address': having_ip,
        'URL_Length': url_length,
        'Shortining_Service': shortening,
        'Abnormal_URL': abnormal_url,
        'DNSRecord': dns_record,
        'Domain_registeration_length': domain_registration_length,
        'Favicon': favicon,
        'Google_Index': google_index,
    }

    # Fill missing features with 0 to match model training
    for feature in ALL_FEATURES:
        if feature not in extracted:
            extracted[feature] = 0

    return extracted
