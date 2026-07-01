import requests

API_URL = "https://open.er-api.com/v6/latest/USD"

try:
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()

    if data["result"] != "success":
        print("Error fetching exchange rates.")
        exit()

    rates = data["rates"]

    print("=" * 50)
    print("        CURRENCY CONVERTER")
    print("=" * 50)

    print("\nAvailable Currencies:")
    print("USD  INR  EUR  GBP  JPY  AUD  CAD  CNY")

    from_currency = input("\nEnter From Currency: ").upper()
    to_currency = input("Enter To Currency: ").upper()

    amount = float(input("Enter Amount: "))

    if from_currency not in rates:
        print("Invalid source currency.")
        exit()

    if to_currency not in rates:
        print("Invalid target currency.")
        exit()

    # Convert source currency to USD
    amount_in_usd = amount / rates[from_currency]

    # Convert USD to target currency
    converted_amount = amount_in_usd * rates[to_currency]

    print("\n========== RESULT ==========")
    print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

except ValueError:
    print("Please enter a valid amount.")

except requests.exceptions.RequestException:
    print("Unable to connect to the currency server.")

except Exception as e:
    print("Unexpected Error:", e)