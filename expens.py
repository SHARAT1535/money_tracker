import csv
import os
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

# Constants
DATA_FILE = 'expenses.csv'
CATEGORIES = ['Food', 'Transportation', 'Utilities', 'Entertainment', 'Healthcare', 'Other']

# Functions

def init_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])

def add_expense(date, amount, category, description):
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

def view_expenses():
    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"Date: {row[0]}, Amount: {row[1]}, Category: {row[2]}, Description: {row[3]}")

def analyze_expenses():
    expenses = defaultdict(float)
    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            expenses[row[2]] += float(row[1])

    for category, total in expenses.items():
        print(f"Category: {category}, Total: {total}")
    
    # Visualize data
    categories = list(expenses.keys())
    amounts = list(expenses.values())
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title('Expense Distribution')
    plt.show()

def main():
    init_data_file()

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            try:
                amount = float(input("Enter the amount: "))
                if amount <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid amount. Please enter a positive number.")
                continue

            print("Select category:")
            for i, category in enumerate(CATEGORIES, 1):
                print(f"{i}. {category}")
            category_choice = input("Enter category number: ")
            try:
                category = CATEGORIES[int(category_choice) - 1]
            except (IndexError, ValueError):
                print("Invalid category choice.")
                continue

            description = input("Enter a description: ")
            add_expense(date, amount, category, description)
            print("Expense added successfully!")

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            analyze_expenses()

        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
