import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os


def preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Remove Person ID
    if "Person ID" in df.columns:
        df.drop("Person ID", axis=1, inplace=True)

    # Handle missing values
    df.dropna(inplace=True)

    # Split Blood Pressure into Systolic and Diastolic
    bp = df["Blood Pressure"].str.split("/", expand=True)
    df["Systolic_BP"] = bp[0].astype(int)
    df["Diastolic_BP"] = bp[1].astype(int)

    # Remove original Blood Pressure column
    df.drop("Blood Pressure", axis=1, inplace=True)

    # Encode categorical columns
    categorical_columns = [
        "Gender",
        "Occupation",
        "BMI Category",
        "Sleep Disorder"
    ]

    label_encoders = {}

    for column in categorical_columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column].astype(str))
        label_encoders[column] = le

    # Features and Target
    X = df.drop("Quality of Sleep", axis=1)
    y = df["Quality of Sleep"]

    # Feature Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create model folder if not exists
    os.makedirs("model", exist_ok=True)

    # Save scaler
    joblib.dump(scaler, "model/scaler.pkl")

    # Save Label Encoders
    joblib.dump(label_encoders, "model/label_encoder.pkl")

    return X_scaled, y
