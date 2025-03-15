import pandas as pd

# Flights ma'lumotlarini yuklash
flights_df = pd.read_parquet("flights.parquet")

# 1. Kechikishi 30 minutdan ortiq bo‘lganlarni filtrlash
def filter_delayed_flights(df):
    return df[df["DepDelay"] > 30]

# 2. Yangi ustun qo‘shish: Delay_Per_Hour
def add_delay_per_hour(df):
    df["Delay_Per_Hour"] = df["DepDelay"] / df["AirTime"]
    return df

# Pipeline qo‘llash
flights_processed = (flights_df
                     .pipe(filter_delayed_flights)
                     .pipe(add_delay_per_hour))

# Natijani chiqarish
print("\n--- FLIGHTS PIPELINE: Yangi ma'lumotlar ---")
print(flights_processed[["DepDelay", "AirTime", "Delay_Per_Hour"]].head())