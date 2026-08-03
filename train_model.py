import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

from utils.preprocess import preprocess_data

# Load and preprocess dataset
X, y, label_encoder = preprocess_data("dataset/Sleep_Efficiency.csv")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scale features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Model Performance")
print("----------------------")
print("R2 Score :", r2_score(y_test, y_pred))
print("MAE      :", mean_absolute_error(y_test, y_pred))

# Create model folder if not exists
os.makedirs("model", exist_ok=True)

# Save files
joblib.dump(model, "model/sleep_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(label_encoder, "model/label_encoder.pkl")

print("\n✅ Model Trained Successfully!")
print("✅ sleep_model.pkl saved")
print("✅ scaler.pkl saved")
print("✅ label_encoder.pkl saved")
