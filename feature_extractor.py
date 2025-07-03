import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # Feature 1: having_IP_Address
    if re.match(r"^(?:http[s]?://)?\d{1,3}(?:\.\d{1,3}){3}", url):
        features.append(1)
    else:
        features.append(-1)

    # Feature 2: URL_Length
    length = len(url)
    if length < 54:
        features.append(-1)
    elif 54 <= length <= 75:
        features.append(0)
    else:
        features.append(1)

    # Feature 3: Shortening_Service
    shortening_services = r"bit\.ly|tinyurl\.com|goo\.gl|ow\.ly|t\.co|bitly\.com"
    if re.search(shortening_services, url):
        features.append(1)
    else:
        features.append(-1)

    # Feature 4: having_At_Symbol
    if '@' in url:
        features.append(1)
    else:
        features.append(-1)

    # Feature 5: double_slash_redirecting
    if url.find('//') > 6:
        features.append(1)
    else:
        features.append(-1)

    # Feature 6: Prefix_Suffix
    if '-' in urlparse(url).netloc:
        features.append(1)
    else:
        features.append(-1)

    # Feature 7: having_Sub_Domain
    hostname = urlparse(url).hostname
    if hostname:
        dots = hostname.split('.')
        if len(dots) <= 2:
            features.append(-1)
        elif len(dots) == 3:
            features.append(0)
        else:
            features.append(1)
    else:
        features.append(1)

    # Feature 8: SSLfinal_State
    # Cannot check without requests or SSL cert, assuming -1
    features.append(-1)

    # Feature 9: Domain_registeration_length
    # Cannot check without WHOIS data, assuming 1 (short registration = phishing)
    features.append(1)

    # Feature 10: Favicon
    features.append(-1)  # Cannot check here, assuming safe

    # Feature 11: port
    if urlparse(url).port in [80, 443, None]:
        features.append(-1)
    else:
        features.append(1)

    # Feature 12: HTTPS_token
    if 'https' in urlparse(url).netloc:
        features.append(1)
    else:
        features.append(-1)

    # Feature 13: Request_URL
    features.append(-1)  # Needs webpage parsing, assuming safe

    # Feature 14: URL_of_Anchor
    features.append(-1)  # Needs HTML parsing

    # Feature 15: Links_in_tags
    features.append(-1)  # Needs HTML parsing

    # Feature 16: SFH
    features.append(-1)  # Needs HTML form parsing

    # Feature 17: Submitting_to_email
    features.append(-1)  # Needs HTML form parsing

    # Feature 18: Abnormal_URL
    features.append(1)  # Without WHOIS, assume abnormal

    # Feature 19: Redirect
    features.append(-1)  # Needs HTTP request

    # Feature 20: on_mouseover
    features.append(-1)  # Needs JS parsing

    # Feature 21: RightClick
    features.append(-1)  # Needs JS parsing

    # Feature 22: popUpWidnow
    features.append(-1)  # Needs JS parsing

    # Feature 23: Iframe
    features.append(-1)  # Needs HTML parsing

    # Feature 24: age_of_domain
    features.append(1)  # Without WHOIS, assume young domain

    # Feature 25: DNSRecord
    features.append(1)  # Without WHOIS, assume no record

    # Feature 26: web_traffic
    features.append(1)  # Without Alexa ranking, assume low traffic

    # Feature 27: Page_Rank
    features.append(1)  # Without rank data, assume low

    # Feature 28: Google_Index
    features.append(-1)  # Assume indexed

    # Feature 29: Links_pointing_to_page
    features.append(1)  # Without backlinks data, assume phishing

    # Feature 30: Statistical_report
    # Check if IP or suspicious domain
    suspicious_domains = ['phishingsite.com', 'malicious.com']
    if any(s in url for s in suspicious_domains):
        features.append(1)
    else:
        features.append(-1)

    return features
