# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

# Number of stocks
n = int(input("Enter the number of stocks: "))

# Get stock details
for i in range(n):
    stock = input("Enter Stock Name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

# Display Portfolio
print("\n===== STOCK PORTFOLIO =====")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} : {quantity} shares × ${price} = ${investment}")

print("----------------------------")
print("Total Investment = $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("===== STOCK PORTFOLIO =====\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} : {quantity} shares x ${price} = ${investment}\n")

    file.write("----------------------------\n")
    file.write(f"Total Investment = ${total_investment}")

print("\nPortfolio saved successfully to portfolio.txt")
