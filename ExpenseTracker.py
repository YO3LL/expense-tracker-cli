''' Solo Project: Personal Expense and Budget Tracker '''

from datetime import datetime
import time

# Expense class
class Expense:
    # Constructor
    def __init__(self, amount: float, category: str, date: datetime, description: str):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
    # operator overloading (print):
    def __str__(self):
        return f"${self.amount:.2f} | {self.category} | {self.date.strftime('%Y-%m-%d')} | {self.description}"

# Welcome message
print("\tWelcome to your Personal Expense and Budget Tracker\n")
ContinueProgram = True # Decides when to terminate program

# Vector that holds all expenses
## expenses = [] for test
expenses = [
    Expense(12.50, "food", datetime(2026, 3, 25), "lunch"),
    Expense(45.00, "gas", datetime(2026, 3, 24), "fuel"),
    Expense(120.99, "groceries", datetime(2026, 3, 23), "weekly shopping"),
    Expense(9.99, "subscription", datetime(2026, 3, 22), "netflix"),
    Expense(60.00, "utilities", datetime(2026, 3, 21), "electricity bill"),
]

# Menu function
def menu():
    print("\tChoose an option (1-8)\t")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Save Data")
    print("6. Load Data")
    print("7. Calculate Total Expenses")
    print("8. Exit")
    while True:
        try:
            return int(input('\nEnter your choice: '))
        except ValueError:
            print('Invalid choice, enter a number from 1 to 8.\n')

# Add Expense Function
def add_expense():
    # Enter 'amount'
    while True:
        try:
            amount = float(input('Enter your amount: '))
            if amount <= 0:
                print('Amount must be greater than 0.')
                continue
            break
        except ValueError:
            print('Invalid amount, try again.')

    # Enter 'category' - Removes whitespaces
    category = input('Enter your category: ').strip()

    # Enter 'date' - Use string parse time to translate into a date type
    while True:
        date_str = input('Enter date (YYYY-MM-DD): ').strip()
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print('Invalid date, try again.')

    # Enter 'description' - Removes whitespaces
    description = input('Enter description: ').strip()

    # Creates a new Expense instance with 'amount', 'category', and 'date'
    newExpense = Expense(amount, category, date, description)
    # Adds the new expense to the database
    expenses.append(newExpense)

    print('Expense added successfully.\n')

# View Expense Function
def view_expense():
    if not expenses:
        print('\nNo expenses recorded.\n')
        time.sleep(1.5)
    else:
        print('\nExpenses:')
        for i, expense in enumerate(expenses, start=1):
            print(f'{i}. {expense}')
    print()  # \n

# Delete Expense Function
def delete_expense():
    if not expenses:
        print('No expenses recorded.\n')
        time.sleep(1.5)
    else:
        print('Select which expense number you would like to remove.')
        for i, expense in enumerate(expenses, start=1):
            print(f'{i}. {expense}')
        while True:
            try:
                deleteExpenseIndex = int(input('Remove: ')) - 1
                if 0 <= deleteExpenseIndex < len(expenses):
                    del expenses[deleteExpenseIndex]
                    print('Expense removed successfully.\n')
                    break
                else:
                    print('Invalid choice, try again. Please select a number from the item list.')
            except ValueError:
                print('Invalid choice, try again. Please select a number from the item list.')

# Update Expense Function
def update_expense():
    if not expenses:
        print('No expenses recorded.\n')
        time.sleep(1.5)
    else:
        print('Select which expense number you would like to update.')
        for i, expense in enumerate(expenses, start=1):
            print(f'{i}. {expense}')
        while True:
            try:
                updateExpenseIndex = int(input('Update: ')) - 1
                if 0 <= updateExpenseIndex < len(expenses):
                    while True:
                        print('Which field would you like to update?')
                        print('Fields: Amount | Category | Date | Description')
                        print(expenses[updateExpenseIndex])
                        valid_fields = ['Amount', 'Category', 'Date', 'Description']
                        field_to_update = str(input('Selection: ')).strip().lower()
                        if field_to_update in valid_fields:
                            if field_to_update == 'amount':
                                pass #### continue here. paste each part from add_expense()
                            elif field_to_update == 'category':
                                pass
                            elif field_to_update == 'date':
                                pass
                            elif field_to_update == 'description':
                                pass
                            else:
                                print('Default Error: update_expense()/ if field_to_update in valid_fields:/ final "else" reached')
                        else:
                            print(f'Invalid choice, try again. Please select a valid field {valid_fields}.')

                    print('Expense updated successfully.\n')
                    break
                else:
                    print('Invalid choice, try again. Please select a number from the item list.')
            except ValueError:
                print('Invalid choice, try again. Please select a number from the item list.')

while ContinueProgram:
    # Display menu
    choice = menu()


    if choice == 1:     # 1. Add Expense ✅
        add_expense()

    elif choice == 2:   # 2. View Expenses ✅
        view_expense()

    elif choice == 3:   # 3. Delete Expense ✅
        delete_expense()

    elif choice == 4:   # 4. Update Expense
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        ContinueProgram = False
    else:
        print("Invalid choice, try again.\n")




