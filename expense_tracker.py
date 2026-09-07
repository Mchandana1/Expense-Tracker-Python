import csv


def load_expenses():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            expenses = []

            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)

            return expenses

    except FileNotFoundError:
        return []


def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["amount", "category", "description", "date"]
        )

        writer.writeheader()
        writer.writerows(expenses)


expenses = load_expenses()


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n========== EXPENSES ==========")
    print(
        f"{'No.':<5}"
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Amount':<12}"
        f"{'Description'}"
    )
    print("-" * 65)

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:<11.2f}"
            f"{expense['description']}"
        )


def total_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total expenses: ₹{total:.2f}")


def category_summary():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n========== CATEGORY SUMMARY ==========")

    for category, amount in categories.items():
        print(f"{category:<15} ₹{amount:.2f}")


def delete_expense():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter the expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        removed = expenses.pop(number - 1)
        save_expenses()

        print("Expense deleted successfully!")
        print("Deleted:", removed)

    except ValueError:
        print("Please enter a valid number.")

def search_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return


    category = input("Enter category to search: ")
    found = False

    print("\n========== SEARCH RESULTS ==========")
    print(
        f"{'No.':<5}"
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Amount':<12}"
        f"{'Description'}"
    )
    print("-" * 65)

    for i, expense in enumerate(expenses, start=1):
     if expense["category"].lower() == category.lower():
              print(
                f"{i:<5}"
                f"{expense['date']:<15}"
                f"{expense['category']:<15}"
                f"₹{expense['amount']:<11.2f}"
                f"{expense['description']}"
            )
              found = True

    if not found:
        print("No expenses found for this category.")


while True:

    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Search Expenses")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
     delete_expense()

    elif choice == "6":
          search_expenses()

    elif choice == "7":
     print("Thank you for using Expense Tracker!")
    break