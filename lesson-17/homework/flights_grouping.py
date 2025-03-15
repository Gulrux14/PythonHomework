import pandas as pd

# Flights ma'lumotlarini yuklash
flights_df = pd.read_parquet("flights.parquet")

# Yil va oy bo‘yicha guruhlash
grouped_flights = flights_df.groupby(["Year", "Month"]).agg(
    Total_Flights=("FlightNum", "count"),
    Average_Arrival_Delay=("ArrDelay", "mean"),
    Max_Departure_Delay=("DepDelay", "max")
).reset_index()

# Natijani chiqarish
print("\n--- FLIGHTS: Yil va oy bo‘yicha guruhlangan statistikalar ---")
print(grouped_flights.head())