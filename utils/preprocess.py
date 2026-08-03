import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Remove unwanted column
    if "ID" in df.columns:
        df.drop("ID", axis=1, inplace=True)

    # Convert Bedtime & Wakeup time into datetime
    df["Bedtime"] = pd.to_datetime(df["Bedtime"])
    df["Wakeup time"] = pd.to_datetime(df["Wakeup time"])

    # Convert time into hour format
    df["Bedtime"] = df["Bedtime"].dt.hour + df["Bedtime"].dt.minute / 60
    df["Wakeup time"] = df["Wakeup time"].dt.hour + df["Wakeup time"].dt.minute / 60

    # Encode categorical columns
    label_encoder = LabelEncoder()

    categorical_columns = [
        "Gender",
        "Smoking status"
    ]

    for col in categorical_columns:
        df[col] = label_encoder.fit_transform(df[col])

    # Input Features
    X = df.drop("Sleep efficiency", axis=1)

    # Target
    y = df["Sleep efficiency"]

    return X, y, label_encoder
