from flask import Flask, render_template_string, request
import joblib
from scipy.sparse import hstack, csr_matrix

from utils.feature_extractor import extract_features

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Phishing Email Detector</title>
    <style>
        body{
            font-family: Arial;
            background:#111827;
            color:white;
            text-align:center;
            padding:40px;
        }

        textarea{
            width:80%;
            height:200px;
            padding:15px;
            border-radius:10px;
            border:none;
            font-size:16px;
        }

        button{
            margin-top:20px;
            padding:12px 25px;
            font-size:18px;
            background:#2563eb;
            color:white;
            border:none;
            border-radius:10px;
            cursor:pointer;
        }

        .result{
            margin-top:30px;
            font-size:28px;
            font-weight:bold;
        }
    </style>
</head>
<body>

<h1>Phishing Email Detection</h1>

<form method="POST">
    <textarea name="email_text" placeholder="Paste email content here..."></textarea>
    <br>
    <button type="submit">Detect</button>
</form>

{% if result %}
<div class="result">
    Result: {{ result }}
</div>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        email_text = request.form["email_text"]

        # TF-IDF feature
        text_vector = vectorizer.transform([email_text])

        # Custom features
        features = extract_features(email_text)

        extra = csr_matrix([[
            features["url_count"],
            features["email_count"],
            features["special_char_count"],
            features["keyword_count"]
        ]])

        combined = hstack([text_vector, extra])

        prediction = model.predict(combined)[0]

        if prediction == "phishing":
            result = "⚠️ Phishing Email"
        else:
            result = "✅ Safe Email"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
