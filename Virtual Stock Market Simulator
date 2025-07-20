import random
stocks = {
    'AAPL': 100.0,
    'GOOG': 150.0,
    'TSLA': 80.0,
    'AMZN': 120.0
}

portfolio = {}
balance = 1000.0
transaction_history = []

# --- Helper Functions ---

def show_stocks():
    print("\nCurrent Stock Prices:")
    for stock, price in stocks.items():
        print(f"{stock}: ₹{price:.2f}")

def update_prices():
    for stock in stocks:
        change_percent = random.uniform(-5, 5)  # +/-5% fluctuation
        stocks[stock] *= (1 + change_percent / 100)
        stocks[stock] = round(stocks[stock], 2)

def buy_stock():
    global balance
    symbol = input("Enter stock symbol to buy: ").upper()
    if symbol not in stocks:
        print("Stock not found.")
        return

    try:
        quantity = int(input("Enter quantity to buy: "))
    except ValueError:
        print("Invalid quantity.")
        return

    total_cost = quantity * stocks[symbol]
    if total_cost > balance:
        print(f"Insufficient balance. You need ₹{total_cost - balance:.2f} more.")
        return

    balance -= total_cost
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    transaction_history.append(f"Bought {quantity} of {symbol} at ₹{stocks[symbol]:.2f}")
    print(f"Bought {quantity} shares of {symbol}.")

def sell_stock():
    global balance
    symbol = input("Enter stock symbol to sell: ").upper()
    if symbol not in portfolio or portfolio[symbol] == 0:
        print("You don’t own this stock.")
        return

    try:
        quantity = int(input("Enter quantity to sell: "))
    except ValueError:
        print("Invalid quantity.")
        return

    if quantity > portfolio[symbol]:
        print(f"You only have {portfolio[symbol]} shares.")
        return

    total_gain = quantity * stocks[symbol]
    balance += total_gain
    portfolio[symbol] -= quantity
    transaction_history.append(f"Sold {quantity} of {symbol} at ₹{stocks[symbol]:.2f}")
    print(f"Sold {quantity} shares of {symbol}.")

def show_portfolio():
    print("\n--- Your Portfolio ---")
    print(f"Cash Balance: ₹{balance:.2f}")
    for symbol, qty in portfolio.items():
        if qty > 0:
            print(f"{symbol}: {qty} shares (₹{stocks[symbol]:.2f} each)")
    print()

def show_history():
    print("\n--- Transaction History ---")
    if not transaction_history:
        print("No transactions yet.")
    else:
        for entry in transaction_history:
            print(entry)

def main():
    print("Welcome to the Virtual Stock Market Simulator!")
    while True:
        print("\nOptions:")
        print("1. Show stock prices")
        print("2. Buy stocks")
        print("3. Sell stocks")
        print("4. View portfolio")
        print("5. View transaction history")
        print("6. Simulate price changes")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            show_stocks()
        elif choice == '2':
            buy_stock()
        elif choice == '3':
            sell_stock()
        elif choice == '4':
            show_portfolio()
        elif choice == '5':
            show_history()
        elif choice == '6':
            update_prices()
            print("Prices updated with random fluctuations.")
        elif choice == '7':
            print("Thank you for playing the Virtual Stock Market!")
            break
        else:
            print("Invalid choice. Try again.")

main()
