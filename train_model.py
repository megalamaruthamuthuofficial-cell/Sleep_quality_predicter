from utils.preprocess import preprocess_data

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
import os


# Load and preprocess dataset
X, y = preprocess_data("dataset/Sleep_health_and_lifestyle_dataset.csv")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Random Forest Regressor
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("=" * 40)
print("Sleep Quality Predictor")
print("=" * 40)
print(f"R² Score : {r2:.4f}")
print(f"MAE      : {mae:.4f}")

# Create model folder if not exists
os.makedirs("model", exist_ok=True)

# Save trained model
joblib.dump(model, "model/sleep_model.pkl")

print("\nModel saved successfully!")
print("Location : model/sleep_model.pkl")
print("\nModel Training Completed Successfully!")
print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")