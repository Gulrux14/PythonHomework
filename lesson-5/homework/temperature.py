def convert_cel_to_far(celsius):
    """Convert Celsius to Fahrenheit."""
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return round((fahrenheit - 32) * 5/9, 2)

# Prompt user for Fahrenheit temperature and convert to Celsius
f_temp = float(input("Enter a temperature in degrees F: "))
celsius = convert_far_to_cel(f_temp)
print(f"{f_temp} degrees F = {celsius} degrees C")

# Prompt user for Celsius temperature and convert to Fahrenheit
c_temp = float(input("Enter a temperature in degrees C: "))
fahrenheit = convert_cel_to_far(c_temp)
print(f"{c_temp} degrees C = {fahrenheit} degrees F")