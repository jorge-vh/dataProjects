import requests
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from urllib.parse import quote

# 📌 1. EXTRACT data from a public API (OpenWeatherMap)
API_KEY = "YOUR_API_KEY"  #You need to edit this line with your own API key
CITY = "Mexico City"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# 📌 2. TRANSFORM data using Pandas
weather = {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "description": data["weather"][0]["description"]
}

# Add the 'timestamp' column with the current date and time
weather["timestamp"] = pd.to_datetime("now")  # Assigns the current date and time

# Create the DataFrame
df = pd.DataFrame([weather])

# 📌 3. LOAD data into PostgreSQL
DB_URL = "postgresql://postgres:1234@localhost:5432/etl_project"
engine = create_engine(DB_URL)

# Cleaning the data (in case there are invalid characters)
df = df.map(lambda x: x.encode('utf-8', 'ignore').decode('utf-8') if isinstance(x, str) else x)

# Insert data into PostgreSQL table 'weather_data'
df.to_sql("weather_data", engine, if_exists="append", index=False)

print("✅ Data successfully inserted into PostgreSQL")
