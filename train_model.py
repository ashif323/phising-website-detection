import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv('phishing_dataset.csv')

# Drop 'id' if exists
if 'id' in data.columns:
    data = data.drop(['id'], axis=1)

# Features and target
X = data.drop('Result', axis=1)
y = data['Result']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and feature names
model_bundle = {
    'model': model,
    'features': X.columns.tolist()
}
joblib.dump(model_bundle, 'phishing_model.pkl')
print("✅ Model saved successfully as phishing_model.pkl")
