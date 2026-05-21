import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from scipy.sparse import csr_matrix, hstack

from utils.feature_extractor import extract_features

# Load dataset
df = pd.read_csv("phishing_emails.csv")

# Features and labels
X = df["text"]
y = df["label"]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

X_text = vectorizer.fit_transform(X)

# Custom feature extraction
extra_features = []

for text in X:
    features = extract_features(text)
    extra_features.append([
        features["url_count"],
        features["email_count"],
        features["special_char_count"],
        features["keyword_count"]
    ])

X_extra = csr_matrix(extra_features)

# Combine TF-IDF + custom features
X_combined = hstack([X_text, X_extra])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_combined,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LogisticRegression()

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model/phishing_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("\nModel saved successfully!")
