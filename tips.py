def get_sleep_tips(sleep_efficiency):

    if sleep_efficiency >= 85:

        return [
            "🎉 Great job! Keep following your current sleep schedule.",
            "💧 Stay hydrated throughout the day.",
            "🏃 Continue exercising regularly.",
            "📵 Avoid excessive screen time before bed."
        ]

    elif sleep_efficiency >= 75:

        return [
            "😴 Try to sleep at the same time every day.",
            "☕ Reduce caffeine intake in the evening.",
            "🧘 Practice relaxation before sleeping.",
            "📱 Avoid using mobile phones 30 minutes before bedtime."
        ]

    else:

        return [
            "⚠️ Your sleep quality needs improvement.",
            "🌙 Sleep at least 7–8 hours daily.",
            "☕ Avoid caffeine after 6 PM.",
            "🛌 Maintain a consistent bedtime.",
            "👨‍⚕️ Consult a doctor if poor sleep continues."
        ]