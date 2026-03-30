# Weather Prediction and Decision Support System

## 📌 Overview
This project is a Python-based Weather Prediction and Decision Support System. It analyzes historical weather data such as temperature, humidity, rainfall, and wind speed to predict future conditions. The system also takes user inputs and provides personalized recommendations based on the selected task and time frame.

---

## 🎯 Objectives
- Predict future weather conditions using past data
- Provide scenario-based forecasts
- Detect extreme weather conditions
- Assist users in decision-making for planned activities

---

## ⚙️ Features
- Historical data analysis (30-day dataset)
- Temperature prediction using weighted averages
- Rain probability calculation
- Scenario-based forecasting (Normal, Rainy, Heatwave, etc.)
- Extreme weather detection (Heatwave, Heavy Rain, Wind)
- User input system for personalization
- Time-based prediction (Next day, 3 days, 1 week, 2 weeks)
- Task-based recommendations (Travel, Event, Tourism, Farming)

---

## 🧠 How It Works
1. Loads a dataset of past weather conditions
2. Calculates average and recent weather trends
3. Predicts base temperature and humidity
4. Adjusts predictions based on selected time frame
5. Identifies extreme weather conditions
6. Takes user input for task type and timing
7. Provides a decision on whether the task is suitable

---

## 🛠️ Technologies Used
- Python
- Pandas (for data handling)

---

## 📥 Installation

1. Install Python (if not already installed)
2. Install required library:
   ```bash
   pip install pandas
