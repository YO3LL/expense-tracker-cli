''' Solo Project: Personal Expense and Budget Tracker '''
import csv
from datetime import datetime

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
continue_program = True # Decides when to terminate program

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

# Helper function - display expenses
def display_expenses_helper(expenses):
    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i:<5} | "
            f"${expense.amount:>9.2f} | "
            f"{expense.category:<12} | "
            f"{expense.date.strftime('%Y-%m-%d')} | "
            f"{expense.description:<20}"
        )

def display_header_helper():
    print(f"{'No.':<5} | {'Amount':>10} | {'Category':<12} | {'Date':<10} | {'Description':<20}")
    print("-" * 70)

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
    new_expense = Expense(amount, category, date, description)
    # Adds the new expense to the database
    expenses.append(new_expense)

    print('Expense added successfully.\n')

# View Expense Function
def view_expense():
    if not expenses:
        print('\nNo expenses recorded.\n')
        input("Press enter to continue...\n")
    else:
        print('\nExpenses:')
        # Header
        display_header_helper()        

        # Rows
        display_expenses_helper(expenses)

    print()  # \n

# Delete Expense Function
def delete_expense():
    if not expenses:
        print('No expenses recorded.\n')
        input("Press enter to continue...\n")
    else:
        print('Select which expense number you would like to remove.')
        # Header
        display_header_helper()        
        display_expenses_helper(expenses)
        while True:
            try:
                delete_expense_index = int(input('Remove: ')) - 1
                if 0 <= delete_expense_index < len(expenses):
                    del expenses[delete_expense_index]
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
        input("Press enter to continue...\n")
    else:
        print('Select which expense number you would like to update.')
        # Header
        display_header_helper()        
        # Rows
        display_expenses_helper(expenses)

        while True:
            try:
                update_expense_index = int(input('Update: ')) - 1
                if 0 <= update_expense_index < len(expenses):
                    print('\nWhich field would you like to update?')
                    print('Amount | Category | Date | Description')

                    expense = expenses[update_expense_index]

                    display_header_helper()                    
                    print(
                        f"{update_expense_index + 1:<5} | "
                        f"${expense.amount:>9.2f} | "
                        f"{expense.category:<12} | "
                        f"{expense.date.strftime('%Y-%m-%d')} | "
                        f"{expense.description:<20}"
                    )

                    valid_fields = ['amount', 'category', 'date', 'description']
                    field_to_update = str(input('Selection: ')).strip().lower()
                    if field_to_update in valid_fields:
                        if field_to_update == 'amount':
                            while True:
                                try:
                                    amount = float(input('Enter your amount: '))
                                    if amount <= 0:
                                        print('Amount must be greater than 0.')
                                        continue
                                    break
                                except ValueError:
                                    print('Invalid amount, try again.')
                            expenses[update_expense_index].amount = amount
                            print('Expense updated successfully.\n')
                            break
                        elif field_to_update == 'category':
                            category = input('Enter your category: ').strip()
                            expenses[update_expense_index].category = category
                            print('Expense updated successfully.\n')
                            break
                        elif field_to_update == 'date':
                            while True:
                                date_str = input('Enter date (YYYY-MM-DD): ').strip()
                                try:
                                    date = datetime.strptime(date_str, "%Y-%m-%d")
                                    break
                                except ValueError:
                                    print('Invalid date, try again.')
                            expenses[update_expense_index].date = date
                            print('Expense updated successfully.\n')
                            break
                        elif field_to_update == 'description':
                            description = input('Enter your description: ').strip()
                            expenses[update_expense_index].description = description
                            print('Expense updated successfully.\n')
                            break
                    else:
                        print(f'Invalid choice, try again. Please select a valid field {valid_fields}.') # Checks valid field (Amount | Category | Date | Description)
                else:
                    print('Invalid choice, try again. Please select a number from the item list.') # Checks valid index for budget item in expenses[]
            except ValueError:
                print('Invalid choice, try again. Please select a number from the item list.') # Checks valid index TYPE for budget item in expenses[]

# Save/Load Data Functions
def save_data(expenses):
    try:
        with open('expenses.txt', 'w') as file:
            for expense in expenses:
                file.write(
                    f"{expense.amount},"
                    f"{expense.category},"
                    f"{expense.date.strftime('%Y-%m-%d')},"
                    f"{expense.description}\n"
                )
        print('Save successful.\n')
    except Exception:
        print('An error occurred while saving data.\n')

def load_data(expenses):
    pass
    # PICK UP HERE #

# MAIN
while continue_program:
    # Display menu
    choice = menu()

    if choice == 1:     # 1. Add Expense (Progressive Goal: Layer 1 - Functional Minimal)
        add_expense()
        input("Press enter to continue...\n")

    elif choice == 2:   # 2. View Expenses (Progressive Goal: Layer 1 - Functional Minimal)
        view_expense()
        input("Press enter to continue...\n")

    elif choice == 3:   # 3. Delete Expense (Progressive Goal: Layer 2 - Low Target)
        delete_expense()
        input("Press enter to continue...\n")

    elif choice == 4:   # 4. Update Expense (Progressive Goal: Layer 2 - Low Target)
        update_expense()
        input("Press enter to continue...\n")

    elif choice == 5:   # 5. Save Data (Progressive Goal: Layer 1 - Functional Minimal)
        pass
    elif choice == 6:   # 6. Load Data (Progressive Goal: Layer 1 - Functional Minimal)
        pass
    elif choice == 7:   # 7. Calculate Total Expenses (Progressive Goal: Layer 3 - Desirable Target)
        pass
    elif choice == 8:   # 8. Quit
        continue_program = False
    else:
        print("Invalid choice, try again.\n")




