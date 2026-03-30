import pandas as pd

def load_data():
    data = {
        "day": list(range(1, 31)),
        "temperature": [
            18,19,20,21,22,23,24,25,26,27,
            26,25,24,23,22,21,20,19,18,17,
            18,19,20,21,22,23,24,25,26,27
        ],
        "humidity": [
            60,62,64,66,68,70,72,74,76,78,
            75,73,71,69,67,65,63,61,59,58,
            60,62,64,66,68,70,72,74,76,78
        ],
        "rainfall": [
            0,0,2,0,5,0,0,3,0,0,
            1,0,0,4,0,0,2,0,0,0,
            0,1,0,3,0,0,2,0,0,1
        ],
        "wind_speed": [
            8,9,10,11,12,13,14,15,16,17,
            16,15,14,13,12,11,10,9,8,7,
            8,9,10,11,12,13,14,15,16,17
        ]
    }
    return pd.DataFrame(data)

def compute_metrics(data):
    return {
        "avg_temp": data["temperature"].mean(),
        "recent_temp": data["temperature"].tail(5).mean(),
        "avg_humidity": data["humidity"].mean(),
        "recent_humidity": data["humidity"].tail(5).mean(),
        "recent_rain": data["rainfall"].tail(5).mean(),
        "avg_wind": data["wind_speed"].mean()
    }

def predict_base(metrics):
    base_temp = 0.6 * metrics["recent_temp"] + 0.4 * metrics["avg_temp"]
    base_humidity = 0.6 * metrics["recent_humidity"] + 0.4 * metrics["avg_humidity"]
    return base_temp, base_humidity

def rain_probability(rain_data):
    rainy_days = 0
    for r in rain_data:
        if r > 0:
            rainy_days += 1
    return round((rainy_days / len(rain_data)) * 100)

def get_range(value, variation):
    return (round(value - variation), round(value + variation))

def extreme_weather(temp, humidity, rain, wind):
    if temp > 30:
        return "Heatwave Risk"
    elif rain > 2:
        return "Heavy Rain Risk"
    elif wind > 15:
        return "Strong Wind Risk"
    elif humidity > 80:
        return "Extreme Humidity"
    else:
        return "Normal Conditions"

def scenario_predictions(base_temp):
    return {
        "Normal": get_range(base_temp, 1),
        "Rainy": get_range(base_temp - 3, 1),
        "Heatwave": get_range(base_temp + 5, 2),
        "Cloudy": get_range(base_temp - 2, 1),
        "Windy": get_range(base_temp - 1, 1)
    }

def predict_future_weather(base_temp, days):
    if days == 1:
        return base_temp
    elif days <= 3:
        return base_temp + 0.5
    elif days <= 7:
        return base_temp + 1.5
    else:
        return base_temp + 2.5

def user_inputs():
    print("\nUser Input Section\n")

    location = input("Enter your exact location in Joshimath: ")

    print("\nSelect your task type:")
    print("1. Travelling")
    print("2. Event Planning")
    print("3. Tourism Visit")
    print("4. Farming Activity")

    try:
        task_choice = int(input("Enter option (1-4): "))
    except:
        task_choice = 0

    task_map = {
        1: "Travelling",
        2: "Event",
        3: "Tourism",
        4: "Farming"
    }

    task = task_map.get(task_choice, "General")

    print("\nWhen will you perform the task?")
    print("1. Next Day")
    print("2. In 3 Days")
    print("3. In One Week")
    print("4. In Two Weeks")

    try:
        time_choice = int(input("Enter option (1-4): "))
    except:
        time_choice = 1

    days_map = {
        1: 1,
        2: 3,
        3: 7,
        4: 14
    }

    days = days_map.get(time_choice, 1)

    description = input("Describe your task briefly: ")

    return location, task, days, description

def decision_system(task, alert, rain_prob):
    if task == "Travelling":
        if "Risk" in alert:
            return "Not Suitable due to weather risk"
        else:
            return "Suitable for travelling"

    elif task == "Event":
        if rain_prob > 50:
            return "Not Suitable due to rain"
        else:
            return "Suitable for event"

    elif task == "Tourism":
        if "Heatwave" in alert or "Rain" in alert:
            return "Not Suitable for tourism"
        else:
            return "Suitable for visit"

    elif task == "Farming":
        if rain_prob > 40:
            return "Good for farming"
        else:
            return "Not ideal due to low rainfall"

    return "General conditions apply"

def display_results(base_temp, rain_prob, scenarios, alert, future_temp, decision,
                    location, task, days, description):

    print("\n===== Weather Prediction System =====\n")

    print("Location:", location)
    print("Task:", task)
    print("Task after:", days, "days")
    print("Details:", description, "\n")

    print("Base Temperature:", round(base_temp, 2), "°C")
    print("Predicted Temperature:", round(future_temp, 2), "°C")
    print("Rain Probability:", rain_prob, "%\n")

    print("--- Scenario Predictions ---")
    for key in scenarios:
        print(key + ":", scenarios[key], "°C")

    print("\n--- Extreme Weather Forecast ---")
    print(alert)

    print("\n--- Decision for Your Task ---")
    print(decision)

    print("\n--- Summary ---")
    print("Expected Temperature Range:", get_range(base_temp, 2))

def main():
    data = load_data()
    metrics = compute_metrics(data)

    base_temp, base_humidity = predict_base(metrics)
    rain_prob = rain_probability(data["rainfall"])

    location, task, days, description = user_inputs()

    future_temp = predict_future_weather(base_temp, days)

    alert = extreme_weather(
        future_temp,
        base_humidity,
        metrics["recent_rain"],
        metrics["avg_wind"]
    )

    scenarios = scenario_predictions(base_temp)

    decision = decision_system(task, alert, rain_prob)

    display_results(base_temp, rain_prob, scenarios, alert, future_temp, decision,
                    location, task, days, description)

main()
