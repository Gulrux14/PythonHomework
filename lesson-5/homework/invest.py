def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"Year {year}: ${amount:.2f}")

principal = float(input("Enter initial amount: "))
rate = float(input("Enter annual rate (decimal, e.g., 0.05 for 5%): "))
years = int(input("Enter number of years: "))

invest(principal, rate, years)