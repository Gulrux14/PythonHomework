from bs4 import BeautifulSoup

# Step 1: Load HTML File
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Step 2: Extract Weather Data
weather_data = []
rows = soup.find("tbody").find_all("tr")

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temperature = int(cols[1].text.replace("°C", ""))  # Convert to integer
    condition = cols[2].text
    weather_data.append({"day": day, "temperature": temperature, "condition": condition})

# Step 3: Display Weather Data
print("Weather Forecast:")
for data in weather_data:
    print(f"{data['day']}: {data['temperature']}°C, {data['condition']}")

# Step 4: Find the Highest Temperature Day
max_temp = max(weather_data, key=lambda x: x["temperature"])
print(f"\nHottest Day: {max_temp['day']} ({max_temp['temperature']}°C)")

# Step 5: Find Days with "Sunny" Condition
sunny_days = [data["day"] for data in weather_data if data["condition"] == "Sunny"]
print(f"Sunny Days: {', '.join(sunny_days)}")

# Step 6: Calculate Average Temperature
average_temp = sum(data["temperature"] for data in weather_data) / len(weather_data)
print(f"Average Temperature for the Week: {average_temp:.1f}°C")