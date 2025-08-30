import sys
import pickle
import os
import re

def is_suspicious(url: str) -> bool:
    """
    Rule-based checks for obvious phishing patterns
    """
    # Too many dots in the URL (subdomain tricks)
    if url.count('.') > 3:
        return True

    # Contains @ symbol (redirect trick)
    if '@' in url:
        return True

    # Hyphen in domain (often used in phishing)
    domain_match = re.search(r"https?://([^/]+)", url)
    if domain_match and '-' in domain_match.group(1):
        return True

    # Suspicious keywords
    suspicious_keywords = ["secure", "login", "account", "update", "verify"]
    for word in suspicious_keywords:
        if word in url.lower():
            return True

    return False

def main():
    # Check if URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python predictor.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Rule-based check first
    if is_suspicious(url):
        print(1)  # Phishing
        return
    
    # Get current script directory
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, '..', 'phishing_model.pkl')
    model_path = os.path.abspath(model_path)

    # Load the saved model and vectorizer
    with open(model_path, 'rb') as f:
        classifier, vectorizer = pickle.load(f)

    # Vectorize the input URL
    url_vector = vectorizer.transform([url])

    # Predict using the loaded model
    prediction = classifier.predict(url_vector)

    # Print 0 for Legit, 1 for Phishing
    print(int(prediction[0]))

if __name__ == "__main__":
    main()
