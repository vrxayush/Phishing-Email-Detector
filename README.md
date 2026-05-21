# 📧 Phishing Email Detection Model

A Machine Learning based Phishing Email Detection System built using Python, Flask, and Scikit-learn that identifies whether an email is phishing or legitimate based on textual content and suspicious URL patterns.

---

## 🚀 Features

- 📩 Detect phishing and legitimate emails  
- 🔍 Analyze URLs, keywords, and suspicious patterns  
- 🧠 Machine Learning based classification  
- 📊 Displays model accuracy and confusion matrix  
- ⚠️ Detects phishing keywords and malicious links  
- 🌐 Simple Flask web interface for testing emails  
- 💾 Saves trained model using Joblib  

---

## 🧠 How It Works

1. User enters or pastes email content  
2. System extracts:
   - URLs
   - Email addresses
   - Special characters
   - Phishing keywords  
3. TF-IDF converts text into numerical vectors  
4. Machine Learning model analyzes patterns  
5. Email is classified as:
   - Phishing
   - Safe  
6. Accuracy and confusion matrix are generated after training  

---

## 🛠️ Tech Stack

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- NumPy  
- HTML  
- CSS  

---

## 📁 Project Structure

```bash
phishing_email_detector/
│
├── app.py
├── train_model.py
├── requirements.txt
├── phishing_emails.csv
│
├── model/
│   ├── phishing_model.pkl
│   └── vectorizer.pkl
│
└── utils/
    └── feature_extractor.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/vrxayush/phishing-email-detector.git

cd phishing-email-detector
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

#### Windows

```bash
.\venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Train the Model

```bash
python train_model.py
```

### 6️⃣ Run Flask App

```bash
python app.py
```

---

## 🌐 Open in Browser

```bash
http://127.0.0.1:5000
```

---

## 📊 Model Evaluation

The system provides:

- ✅ Accuracy Score  
- 📉 Confusion Matrix  
- 📄 Classification Report  

Example:

```text
Accuracy: 95%
```

---

## 🔑 Example Emails

### ⚠️ Phishing Email

```text
URGENT: Your account has been suspended.
Click here immediately to verify:
http://fake-bank-login.com
```

### ✅ Safe Email

```text
Hello Team,

Please find attached the project report.

Regards,
Raju
```

---

## ⚠️ Important Notes

- Model accuracy depends on dataset quality  
- Larger datasets improve detection performance  
- Always verify suspicious links manually  
- Avoid clicking unknown URLs in real emails  

---

## 📈 Future Improvements

- 🤖 Deep Learning integration (LSTM/BERT)  
- 📧 Gmail API integration  
- 🔗 Live URL reputation checking  
- 🗄️ Database logging system  
- 🌙 Dark mode dashboard  
- 📂 Email file (.eml) support  
- ☁️ Deployment on cloud platforms  

---

## 🎯 Use Case

This project demonstrates:

- Machine Learning classification  
- Natural Language Processing (NLP)  
- Cyber Security concepts  
- Email threat detection  
- Flask web development  
- Feature extraction and vectorization  

---

## 👨‍💻 Author

Ayush Shah  
Computer Science Engineering Student  
Interest: Cyber Security, AI, IoT & Software Development
