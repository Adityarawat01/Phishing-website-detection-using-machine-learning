import re
import numpy as np
import joblib
from urllib.parse import urlparse

# Function to extract features from a URL
def extract_features(url):
    features = []

    # Length of the URL
    features.append(len(url))  # length_url

    # Number of dots (.) in the domain
    domain = urlparse(url).netloc
    features.append(len(domain))    
    features.append(domain.count('.'))  # nb_dots
    # Number of hyphens (-) in the URL
    features.append(url.count('-'))  # nb_hyphens

    # Count of '?' (query parameters) in the URL
    features.append(url.count('?'))  # nb_qm

    # Count of '&' (and) in the URL
    features.append(url.count('&'))  # nb_and

    # Count of '=' (equal sign) in the URL
    features.append(url.count('='))  # nb_eq

    # Count of underscores (_) in the URL
    features.append(url.count('_'))  # nb_underscore

    # Count of tilde (~) in the URL
    features.append(url.count('~'))  # nb_tilde

    # Count of percent signs (%) in the URL
    features.append(url.count('%'))  # nb_percent

    # Count of slashes (/) in the URL
    features.append(url.count('/'))  # nb_slash

    # Count of asterisks (*) in the URL
    features.append(url.count('*'))  # nb_star

    # Count of colons (:) in the URL
    features.append(url.count(':'))  # nb_colon

    # Count of commas (,) in the URL
    features.append(url.count(','))  # nb_comma

    # Count of semicolons (;) in the URL
    features.append(url.count(';'))  # nb_semicolumn

    # Count of dollar signs ($) in the URL
    features.append(url.count('$'))  # nb_dollar

    # Count of spaces in the URL
    features.append(url.count(' '))  # nb_space

    # Check if 'www' is in the URL
    features.append(1 if 'www' in url else 0)  # nb_www

    # Check if '.com' is in the URL
    features.append(1 if '.com' in url else 0)  # nb_com

    # Check for double slashes (//)
    features.append(1 if '//' in url else 0)  # nb_dslash

    # Check if 'http' is in the URL path (for path anomalies)
    features.append(1 if 'http' in urlparse(url).path else 0)  # http_in_path

    # Check if 'https' is in the URL (HTTPS token)
    features.append(1 if 'https' in url else 0)  # https_token

    # Calculate ratio of digits in the URL (ratio_digits_url)
    digits = sum(c.isdigit() for c in url)
    features.append(digits / len(url) if len(url) > 0 else 0)  # ratio_digits_url

    # Count number of subdomains (nb_subdomains)
    subdomain_count = domain.split('.')[0].count('.')
    features.append(subdomain_count)  # nb_subdomains

    # Check for suspicious TLDs (top-level domains)
    suspicious_tlds = ['.xyz', '.top', '.club', '.online']  # Add more suspicious TLDs
    features.append(1 if any(tld in domain for tld in suspicious_tlds) else 0)  # suspecious_tld
    print(features)
    # Return the features as a numpy array (in the same format the model was trained on)
    return np.array(features).reshape(1, -1)

# Function to classify the URL using a trained model
def classify_url(url, model):
    features = extract_features(url)
    prediction = model.predict(features)
    return "Legitimate" if prediction == 1 else "Phishing"

# Load the trained model (make sure you have a trained model saved)
model = joblib.load('rf_model.joblib')

# User input for URL
test_url = input("Please enter a URL to check: ")

# Classify the URL
result = classify_url(test_url, model)
print(f"The URL '{test_url}' is classified as: {result}")
