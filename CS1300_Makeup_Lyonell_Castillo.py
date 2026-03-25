amount = float(input("Enter amount: "))
currency = input("Enter currency (USD/EUR/GBP): ")

if currency == "USD" or currency == "usd":
    print(f"{amount:.2f} USD = {amount * 0.92:.2f} EUR")
    print(f"{amount:.2f} USD = {amount * 0.79:.2f} GBP")

elif currency == "EUR" or currency == "eur":
    print(f"{amount:.2f} EUR = {amount * 1.09:.2f} USD")
    print(f"{amount:.2f} EUR = {amount * 0.86:.2f} GBP")

elif currency == "GBP" or currency == "gbp":
    print(f"{amount:.2f} GBP = {amount * 1.27:.2f} USD")
    print(f"{amount:.2f} GBP = {amount * 1.16:.2f} EUR")

else:
    print("Invalid currency")