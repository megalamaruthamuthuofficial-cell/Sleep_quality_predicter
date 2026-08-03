import joblib
import pandas as pd
from datetime import datetime


# Load saved files
model = joblib.load("model/sleep_model.pkl")
scaler = joblib.load("model/scaler.pkl")


# Manual Encoding
gender_mapping = {
    "Male": 0,
    "Female": 1
}


smoking_mapping = {
    "No": 0,
    "Yes": 1,

    # Alternative dataset values
    "Never": 0,
    "Former": 1,
    "Current": 2
}



# Convert HH:MM time into decimal hours
def convert_time(time_str):

    t = datetime.strptime(time_str, "%H:%M")

    return t.hour + (t.minute / 60)



def predict_sleep(
    age,
    gender,
    bedtime,
    wakeup_time,
    sleep_duration,
    rem_sleep,
    deep_sleep,
    light_sleep,
    awakenings,
    caffeine,
    alcohol,
    smoking_status,
    exercise_frequency
):

    # Encode categorical values
    gender = gender_mapping[gender]
    smoking_status = smoking_mapping[smoking_status]


    # Convert time into decimal hours
    bedtime = convert_time(bedtime)
    wakeup_time = convert_time(wakeup_time)


    # Create input dataframe
    input_data = pd.DataFrame([{

        "Age": age,
        "Gender": gender,
        "Bedtime": bedtime,
        "Wakeup time": wakeup_time,
        "Sleep duration": sleep_duration,
        "REM sleep percentage": rem_sleep,
        "Deep sleep percentage": deep_sleep,
        "Light sleep percentage": light_sleep,
        "Awakenings": awakenings,
        "Caffeine consumption": caffeine,
        "Alcohol consumption": alcohol,
        "Smoking status": smoking_status,
        "Exercise frequency": exercise_frequency

    }])


    # Scale input data
    input_scaled = scaler.transform(input_data)


    # Predict Sleep Efficiency
    prediction = model.predict(input_scaled)[0]


    # Convert to percentage
    sleep_efficiency = round(prediction * 100, 2)


    # Sleep Quality
    if prediction >= 0.85:

        sleep_quality = "Excellent 😴"

    elif prediction >= 0.75:

        sleep_quality = "Average 🙂"

    else:

        sleep_quality = "Poor 😟"



    return {

        "sleep_efficiency": sleep_efficiency,
        "sleep_quality": sleep_quality

    }
