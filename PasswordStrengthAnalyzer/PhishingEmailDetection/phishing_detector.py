import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("Loading dataset...")

# Load dataset
df = pd.read_csv("dataset/emails.csv", encoding='latin-1')

# Keep only required columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

print("\nFirst 5 records:")
print(df.head())

# Convert labels
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

# Features and target
X = df['message']
y = df['label']

# Convert text into numbers
vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1,2),
    max_features=5000
)


X_features = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_features,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining model...")

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['Safe', 'Phishing'],
    yticklabels=['Safe', 'Phishing']
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.savefig("reports/confusion_matrix.png")
plt.show()

# Save model and vectorizer
joblib.dump(model, "models/phishing_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("\nModel saved successfully!")

# Test custom email
while True:

    print("\nEnter email text:")
    email = input()

    transformed_email = vectorizer.transform([email])

    prediction = model.predict(transformed_email)

    if prediction[0] == 1:
        print("\n⚠️ This Email is PHISHING")
    else:
        print("\n✅ This Email is SAFE")

    choice = input("\nCheck another email? (y/n): ")

    if choice.lower() != 'y':
        break

print("\nProgram Ended.")