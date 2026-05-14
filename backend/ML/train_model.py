import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import joblib

# Load the dataset
data = pd.read_csv('backend/ML/cattle_health_monitoring.csv')

# Check for missing values and handle them if necessary
if data.isnull().sum().any():
    print("Missing values found in the dataset. Filling with mean values.")
    data.fillna(data.mean(), inplace=True)

# Define features and target variable
features = ['HeartRate_BPM', 'Activity_X', 'Activity_Y', 'Activity_Z', 'SkinTemp_Celsius']
X = data[features]
y = data['Health_Status'].map({'Healthy': 1, 'Unhealthy': 0})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Train XGBoost model
xgb_model = XGBClassifier(random_state=42)
xgb_model.fit(X_train, y_train)

# Export models and scaler
joblib.dump(rf_model, 'backend/ML/Plk/random_forest_model.pkl')
joblib.dump(xgb_model, 'backend/ML/Plk/xgboost_model.pkl')
joblib.dump(scaler, 'backend/ML/Plk/scaler.pkl')

print("Models and scaler have been saved successfully!")