import re

phishing_keywords = [
    "verify",
    "password",
    "bank",
    "urgent",
    "click",
    "login",
    "free",
    "winner",
    "reset",
    "account suspended"
]

def extract_features(text):
    text = text.lower()

    url_count = len(re.findall(r'http[s]?://', text))
    email_count = len(re.findall(r'\S+@\S+', text))
    special_char_count = len(re.findall(r'[!$#%]', text))

    keyword_count = sum(keyword in text for keyword in phishing_keywords)

    return {
        "url_count": url_count,
        "email_count": email_count,
        "special_char_count": special_char_count,
        "keyword_count": keyword_count
    }
