#Note: The currencies' value are not necessarily realistic.
#Note: This project can be done using a GUI
#Note: The following dictionary assigns a value to each currency give usd as the base currency.
currency_dict = {"kwd":  0.3,
                 "usd":  1,
                 'tr': 8.13,
                 'eur':  0.85,
                 'aed':  3.67}

first_prompt = "Please enter the starting currency \n Kuwaite Dinar: kwd \n US Dollar: usd \n Turkish Lira: tr \n Euro: eur \n UAE Dirham: aed \n"

starting_currency = input(first_prompt)
money_amount = float(input("Please enter the amount of the money"))
final_currency = input("Please enter the output currency: ")

# This will get equivalent amount in the last currency
result_amount = round(money_amount / currency_dict[starting_currency] * currency_dict[final_currency], 3)

print(f"{money_amount} {starting_currency} equal {result_amount} {final_currency}")
