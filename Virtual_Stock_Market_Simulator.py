import random

# --- Initial Setup ---
stocks = {
    'AAPL': 100.0,
    'GOOG': 150.0,
    'TSLA': 80.0,
    'AMZN': 120.0
}

portfolio = {}  # Stores owned stock quantities
balance = 1000.0  # Starting cash
transaction_history = []

# --- Helper Functions ---

def show_stocks():
    print("\n📈 Current Stock Prices:")
    for symbol, price in stocks.items():
        print(f"{symbol}: ₹{price:.2f}")

def update_prices():
    for symbol in stocks:
        change_percent = random.uniform(-5, 5)  # Random fluctuation -5% to +5%
        new_price = stocks[symbol] * (1 + change_percent / 100)
        stocks[symbol] = round(new_price, 2)
    print("✅ Stock prices updated.\n")

def buy_stock():
    global balance
    symbol = input("Enter stock symbol to buy: ").upper()
    if symbol not in stocks:
        print("❌ Stock symbol not found.")
        return

    try:
        quantity = int(input(f"Enter quantity to buy of {symbol}: "))
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            return
    except ValueError:
        print("❌ Invalid quantity.")
        return

    cost = stocks[symbol] * quantity
    if cost > balance:
        print(f"❌ Not enough balance. You need ₹{cost - balance:.2f} more.")
        return

    balance -= cost
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    transaction_history.append(f"Bought {quantity}x {symbol} @ ₹{stocks[symbol]:.2f}")
    print(f"✅ Bought {quantity} shares of {symbol} for ₹{cost:.2f}")

def sell_stock():
    global balance
    symbol = input("Enter stock symbol to sell: ").upper()
    if symbol not in portfolio or portfolio[symbol] == 0:
        print("❌ You do not own this stock.")
        return

    try:
        quantity = int(input(f"Enter quantity to sell of {symbol}: "))
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            return
    except ValueError:
        print("❌ Invalid quantity.")
        return

    if quantity > portfolio[symbol]:
        print(f"❌ You only own {portfolio[symbol]} shares.")
        return

    earnings = stocks[symbol] * quantity
    balance += earnings
    portfolio[symbol] -= quantity
    transaction_history.append(f"Sold {quantity}x {symbol} @ ₹{stocks[symbol]:.2f}")
    print(f"✅ Sold {quantity} shares of {symbol} for ₹{earnings:.2f}")

def show_portfolio():
    print("\n💼 Your Portfolio:")
    print(f"Cash Balance: ₹{balance:.2f}")
    has_stocks = False
    for symbol, qty in portfolio.items():
        if qty > 0:
            print(f"{symbol}: {qty} shares (₹{stocks[symbol]:.2f} each)")
            has_stocks = True
    if not has_stocks:
        print("You do not own any stocks yet.")

def show_history():
    print("\n🧾 Transaction History:")
    if not transaction_history:
        print("No transactions made yet.")
    else:
        for entry in transaction_history:
            print("-", entry)

# --- Main Menu Loop ---

def main():
    print("📊 Welcome to the Virtual Stock Market Simulator 📊")
    while True:
        print("\n--- MENU ---")
        print("1. Show Stock Prices")
        print("2. Buy Stocks")
        print("3. Sell Stocks")
        print("4. View Portfolio")
        print("5. View Transaction History")
        print("6. Simulate Price Change")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            show_stocks()
        elif choice == '2':
            show_stocks()
            buy_stock()
        elif choice == '3':
            show_portfolio()
            sell_stock()
        elif choice == '4':
            show_portfolio()
        elif choice == '5':
            show_history()
        elif choice == '6':
            update_prices()
        elif choice == '7':
            print("👋 Exiting simulator. Thanks for playing!")
            break
        else:
            print("❌ Invalid choice. Please enter 1 to 7.")

# Run the simulator
main()