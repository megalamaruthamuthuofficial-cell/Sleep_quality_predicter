from flask import Flask, render_template, request
from predict import predict_sleep

from utils.tips import get_sleep_tips
from utils.quotes import get_random_quote
from utils.bedtime import recommend_bedtime


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Numeric Inputs
        age = int(request.form["age"])
        sleep_duration = float(request.form["sleep_duration"])

        rem_sleep = float(request.form["rem_sleep"])
        deep_sleep = float(request.form["deep_sleep"])
        light_sleep = float(request.form["light_sleep"])

        awakenings = int(request.form["awakenings"])

        caffeine = float(request.form["caffeine"])
        alcohol = float(request.form["alcohol"])

        exercise_frequency = int(request.form["exercise_frequency"])


        # Categorical Inputs
        gender = request.form["gender"]
        smoking_status = request.form["smoking_status"]


        # Time Inputs (HH:MM format)
        bedtime = request.form["bedtime"]
        wakeup_time = request.form["wakeup_time"]


        # Predict
        result = predict_sleep(
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
        )


        # Extra Sleep Features

        # Generate sleep tips
        tips = get_sleep_tips(
            result["sleep_efficiency"]
        )


        # Generate random quote
        quote = get_random_quote()


        # Recommend bedtime
        recommended_bedtime = recommend_bedtime(
            wakeup_time,
            sleep_duration
        )


        return render_template(
            "result.html",
            sleep_efficiency=result["sleep_efficiency"],
            sleep_quality=result["sleep_quality"],
            tips=tips,
            quote=quote,
            recommended_bedtime=recommended_bedtime
        )


    except Exception as e:
        return f"Error: {e}"



if __name__ == "__main__":
    app.run(debug=True)
