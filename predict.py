import joblib
import pandas as pd

# Load model
model = joblib.load("model/sleep_model.pkl")
scaler = joblib.load("model/scaler.pkl")
label_encoders = joblib.load("model/label_encoder.pkl")


def encode_value(column, value):
    """Safely encode categorical values"""
    le = label_encoders[column]

    # If value not found in encoder, use first available class
    if value not in le.classes_:
        print(f"Warning: '{value}' not found for {column}. Using '{le.classes_[0]}'")
        value = le.classes_[0]

    return le.transform([value])[0]


def predict_sleep_quality(
    gender,
    age,
    occupation,
    sleep_duration,
    physical_activity_level,
    stress_level,
    bmi_category,
    heart_rate,
    daily_steps,
    blood_pressure,
    sleep_disorder,
):

    systolic_bp, diastolic_bp = map(int, blood_pressure.split("/"))

    gender = encode_value("Gender", gender)
    occupation = encode_value("Occupation", occupation)
    bmi_category = encode_value("BMI Category", bmi_category)
    sleep_disorder = encode_value("Sleep Disorder", sleep_disorder)

    input_data = pd.DataFrame([[
        gender,
        age,
        occupation,
        sleep_duration,
        physical_activity_level,
        stress_level,
        bmi_category,
        heart_rate,
        daily_steps,
        sleep_disorder,
        systolic_bp,
        diastolic_bp
    ]], columns=[
        "Gender",
        "Age",
        "Occupation",
        "Sleep Duration",
        "Physical Activity Level",
        "Stress Level",
        "BMI Category",
        "Heart Rate",
        "Daily Steps",
        "Sleep Disorder",
        "Systolic_BP",
        "Diastolic_BP"
    ])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    return round(prediction[0], 2)


if __name__ == "__main__":

    print("Available Sleep Disorder values:")
    print(label_encoders["Sleep Disorder"].classes_)
    print()

    result = predict_sleep_quality(
        gender="Male",
        age=27,
        occupation="Engineer",
        sleep_duration=7.5,
        physical_activity_level=45,
        stress_level=5,
        bmi_category="Normal",
        heart_rate=72,
        daily_steps=8000,
        blood_pressure="120/80",
        sleep_disorder="No Disorder"
    )

    print("Predicted Quality of Sleep:", result)