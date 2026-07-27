from flask import Flask, render_template, request
from predict import predict_sleep_quality

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        gender = request.form["gender"]
        age = int(request.form["age"])
        occupation = request.form["occupation"]
        sleep_duration = float(request.form["sleep_duration"])
        physical_activity_level = int(request.form["physical_activity_level"])
        stress_level = int(request.form["stress_level"])
        bmi_category = request.form["bmi_category"]
        heart_rate = int(request.form["heart_rate"])
        daily_steps = int(request.form["daily_steps"])
        blood_pressure = request.form["blood_pressure"]
        sleep_disorder = request.form["sleep_disorder"]

        prediction = predict_sleep_quality(
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
            sleep_disorder
        )

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)