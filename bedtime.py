from datetime import datetime, timedelta


def recommend_bedtime(wakeup_time, sleep_duration):

    """
    wakeup_time : HH:MM (Example: 06:30)
    sleep_duration : Hours (Example: 8)
    """

    wake_time = datetime.strptime(wakeup_time, "%H:%M")

    recommended_time = wake_time - timedelta(hours=sleep_duration)

    return recommended_time.strftime("%I:%M %p")