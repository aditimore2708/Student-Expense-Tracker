import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    print("\n--- Add Expense ---")

    title = input("Expense name: ").strip()

    if not title:
        print("❌ Expense name cannot be empty.")
        return

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("❌ Please enter a valid amount.")
        return

    if amount <= 0:
        print("❌ Amount must be greater than 0.")
        return

    category = input("Category: ").strip()

    if not category:
        category = "Other"

    expense = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("\n✅ Expense added successfully!")
    print(f"₹{amount:.2f} spent on {title}")


def view_expenses():
    expenses = load_expenses()

    print("\n" + "=" * 70)
    print("                        EXPENSE HISTORY")
    print("=" * 70)

    if not expenses:
        print("No expenses found.")
        print("=" * 70)
        return

    print(
        f"{'No.':<5}"
        f"{'Date':<15}"
        f"{'Expense':<20}"
        f"{'Category':<15}"
        f"{'Amount':>10}"
    )

    print("-" * 70)

    total = 0

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<5}"
            f"{expense['date']:<15}"
            f"{expense['title']:<20}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:>8.2f}"
        )

        total += expense["amount"]

    print("-" * 70)
    print(f"Total Expenses: {len(expenses)}")
    print(f"Total Spending: ₹{total:.2f}")
    print("=" * 70)


def main():
    while True:
        print("\n==============================")
        print("   STUDENT EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("\nGoodbye! 👋")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()