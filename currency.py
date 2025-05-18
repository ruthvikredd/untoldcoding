import requests
from datetime import datetime
import socket
import time
import json

# Fallback exchange rates (update these periodically)
FALLBACK_RATES = {
    'USD_EUR': 0.93,
    'USD_GBP': 0.80,
    'EUR_USD': 1.07,
    'GBP_USD': 1.25,
    # Add more pairs as needed
}

def check_internet():
    """Check internet connection"""
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except OSError:
        return False

def get_exchange_rate(base, target):
    """Try multiple methods to get exchange rate"""
    # Method 1: Free CurrencyAPI
    try:
        response = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{base.lower()}/{target.lower()}.json")
        if response.status_code == 200:
            data = response.json()
            return float(data[target.lower()])
    except:
        pass

    # Method 2: Fallback rates
    pair = f"{base}_{target}"
    if pair in FALLBACK_RATES:
        return FALLBACK_RATES[pair]

    # Method 3: Reciprocal calculation if reverse pair exists
    reverse_pair = f"{target}_{base}"
    if reverse_pair in FALLBACK_RATES:
        return 1 / FALLBACK_RATES[reverse_pair]

    return None

def currency_converter():
    print("\n" + "=" * 40)
    print("💵 RELIABLE CURRENCY CONVERTER".center(40))
    print("=" * 40)
    
    while True:
        try:
            print("\nAvailable commands:")
            print("1. Convert currencies")
            print("2. Exit")
            
            choice = input("Enter choice (1/2): ").strip()
            
            if choice == "2":
                print("\nThank you for using the converter. Goodbye! 👋")
                break
                
            if choice != "1":
                print("⚠️ Please enter 1 or 2")
                continue
                
            if not check_internet():
                print("\n⚠️ Working in offline mode (using fallback rates)")
                
            base = input("From currency (3 letters, e.g., USD): ").upper().strip()
            target = input("To currency (3 letters, e.g., EUR): ").upper().strip()
            
            if len(base) != 3 or len(target) != 3:
                print("⚠️ Currency codes must be 3 letters")
                continue
                
            try:
                amount = float(input("Amount to convert: "))
            except ValueError:
                print("⚠️ Please enter a valid number")
                continue
                
            print("\n⏳ Fetching exchange rate...")
            start_time = time.time()
            
            rate = get_exchange_rate(base, target)
            
            if rate is None:
                print("\n❌ Could not get exchange rate for this pair")
                print("Please try another currency pair")
                continue
                
            converted = amount * rate
            elapsed = time.time() - start_time
            
            print(f"\n💱 Conversion Result ({datetime.now().strftime('%Y-%m-%d %H:%M')})")
            print(f"{amount:.2f} {base} = {converted:.2f} {target}")
            print(f"Exchange Rate: 1 {base} = {rate:.6f} {target}")
            print(f"Processed in {elapsed:.2f} seconds")
            
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    currency_converter()