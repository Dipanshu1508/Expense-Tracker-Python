import csv
from datetime import datetime

def add_expense(amount, category):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, datetime.now().strftime("%Y-%m-%d")])

def view_expenses():
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Amount: {row[0]}, Category: {row[1]}, Date: {row[2]}")

def total_spending():
    total = 0
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            total += float(row[0])
    print(f"Total spending: ${total:.2f}")

# Example usage
add_expense(15.50, "Food")
add_expense(29.99, "Shopping")
view_expenses()
total_spending()

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Total Spending\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        amount = float(input("Amount: $"))
        category = input("Category: ")
        add_expense(amount, category)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spending()
    elif choice == "4":
        break