# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 200,
    "MSFT": 300
}

total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stocks:
        value = stocks[name] * quantity
        total_investment += value
        print(name, "Investment:", value)
    else:
        print("Stock not available")

print("Total Investment:", total_investment)

# Save result in a text file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment: " + str(total_investment))

print("Portfolio saved successfully.")