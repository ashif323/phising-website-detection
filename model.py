# model.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv('phishing_dataset.csv')

# Features and target
X = df.drop(['Result'], axis=1)  # 'Result' is the target label
y = df['Result']

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model and feature names together
model_bundle = {
    'model': model,
    'features': X.columns.tolist()
}
joblib.dump(model_bundle, 'model.pkl')
print("Model and features saved successfully to 'model.pkl'")
