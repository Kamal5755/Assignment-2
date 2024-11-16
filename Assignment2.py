from datetime import datetime

def add_expense(expenses):
    
    category = input("Enter expense category (e.g., Food, Rent): ")
    amount = float(input("Enter expense amount: "))
    date = datetime.now().strftime("%Y-%m-%d")  # Get current date in YYYY-MM-DD format
    expenses.append({"category": category, "amount": amount, "date": date})
    print(f"Added {amount} to {category} on {date}.")

def view_expenses(expenses, budget):
    
    total_expense = sum(expense["amount"] for expense in expenses)
    print("\n--- Expense Summary ---")
    for expense in expenses:
        print(f"{expense['date']}: {expense['category']} - ${expense['amount']:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Remaining Budget: ${budget - total_expense:.2f}")

def main():
    
    print("Welcome to the Expense Tracker with Date Logging!")
    budget = float(input("Enter your total monthly budget: $"))
    expenses = []
    
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses, budget)
        elif choice == "3":
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
