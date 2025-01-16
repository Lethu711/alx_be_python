# main-0.py

import argparse
import sys
import os

# Verify if 'bank_account.py' exists in the current directory
script_dir = os.getcwd()
bank_account_path = os.path.join(script_dir, 'bank_account.py')

if not os.path.isfile(bank_account_path):
    print("Warning: 'bank_account.py' is missing in the current directory. Some operations may not work.")
else:
    try:
        from bank_account import BankAccount
    except ModuleNotFoundError as e:
        print(f"Error importing BankAccount: {e}. Ensure 'bank_account.py' is correctly named and in the same directory as 'main-0.py'.")
        BankAccount = None

def main():
    parser = argparse.ArgumentParser(description="Simple Bank Account Operations")
    parser.add_argument("operation", choices=["deposit", "withdraw", "balance"], nargs="?", help="Banking operation")
    parser.add_argument("amount", nargs="?", type=float, help="Amount for deposit or withdrawal")
    args = parser.parse_args()

    if args.operation is None:
        parser.print_help()
        return  # Changed from sys.exit(0) to return for graceful handling

    if args.operation in ["deposit", "withdraw"] and args.amount is None:
        parser.error(f"The '{args.operation}' operation requires an amount.")

    if 'BankAccount' not in globals() or BankAccount is None:
        print("Bank operations are unavailable due to missing 'BankAccount' class.")
        return

    account = BankAccount()

    if args.operation == "deposit":
        account.deposit(args.amount)
    elif args.operation == "withdraw":
        account.withdraw(args.amount)
    elif args.operation == "balance":
        account.display_balance()

if __name__ == "__main__":
    main()

