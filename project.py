import datetime
import csv

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Ensure the file exists with headers
try:
    with open(EXPENSE_FILE, "x") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])
except FileExistsError:
    pass

# Function to add an expense
def add_expense(amount, category, description):
    date = datetime.date.today().strftime("%Y-%m-%d")
    with open(EXPENSE_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    print("Expense added successfully.")

# Function to view all expenses
def view_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                print(f"Date: {row[0]}, Amount: ${row[1]}, Category: {row[2]}, Description: {row[3]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to calculate total expenses
def total_expenses():
    total = 0.0
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                total += float(row[1])
    except FileNotFoundError:
        print("No expenses recorded yet.")
    print(f"Total expenses: ${total:.2f}")

# Function to summarize expenses by category
def summary_by_category():
    categories = {}
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                category = row[2]
                amount = float(row[1])
                categories[category] = categories.get(category, 0) + amount
    except FileNotFoundError:
        print("No expenses recorded yet.")
    print("Expense Summary by Category:")
    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")

# Main menu
def main_menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Expense Summary by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (e.g., Food, Transport, etc.): ")
                description = input("Enter description: ")
                add_expense(amount, category, description)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            summary_by_category()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main_menu()
