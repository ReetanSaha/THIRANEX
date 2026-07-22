import joblib

model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

email = "Click this link to verify your bank account"

email_vector = vectorizer.transform([email])

prediction = model.predict(email_vector)

if prediction[0] == 1:
    print("Phishing")
else:
    print("Safe")