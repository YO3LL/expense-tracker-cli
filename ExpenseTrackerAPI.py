''' Solo Project: Personal Expense and Budget Tracker '''
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
def add_expense(expenses):
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
    category = input('Enter your category: ').strip().lower()

    # Enter 'date' - Use string parse time to translate into a date type
    while True:

        date_str = input('Enter date (YYYY-MM-DD): ').strip()
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            break

        except ValueError:
            print('Invalid date, try again.')

    # Enter 'description' - Removes whitespaces
    while True:
        description = input('Enter description (do not include commas): ').strip()

        if ',' in description:
            print('Description cannot contain commas.')
            continue

        break

    # Creates a new Expense instance with 'amount', 'category', and 'date'
    new_expense = Expense(amount, category, date, description)
    # Adds the new expense to the database
    expenses.append(new_expense)

    print('Expense added successfully.\n')

# View Expense Function
def view_expenses(expenses):
    if not expenses:
        print('\nNo expenses recorded.\n')
        input("Press enter to continue...")

    else:
        print('\nExpenses:')

        display_header_helper()             # Header        
        display_expenses_helper(expenses)   # Rows

    print()  # \n

# Delete Expense Function
def delete_expense(expenses):
    if not expenses:
        print('No expenses recorded.\n')
        input("Press enter to continue...")

    else:
        print('Select which expense number you would like to remove.')
        display_header_helper()             # Header
        display_expenses_helper(expenses)   # Rows

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
def update_expense(expenses):
    if not expenses:
        print('No expenses recorded.\n')
        input("Press enter to continue...")

    else:
        print('Select which expense number you would like to update.')
        display_header_helper()                # Header
        display_expenses_helper(expenses)   # Rows

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
                            category = input('Enter your category: ').strip().lower()

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
                            while True:
                                description = input('Enter description (do not include commas): ').strip()
                                if ',' in description:
                                    print('Description cannot contain commas.')
                                    continue
                                break

                            expenses[update_expense_index].description = description

                            print('Expense updated successfully.\n')
                            break

                    else:
                        print(f'Invalid choice, try again. Please select a valid field {valid_fields}.') # Checks valid field (Amount | Category | Date | Description)

                else:
                    print('Invalid choice, try again. Please select a number from the item list.') # Checks valid index for budget item in expenses[]

            except ValueError:
                print('Invalid choice, try again. Please select a number from the item list.') # Checks valid index TYPE for budget item in expenses[]

# Save Data Function
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

# Load Data Function
def load_data(expenses):
    file_name = input('Enter file name: ')
    try:
        with open(file_name, 'r') as file:

            expenses.clear()

            for line in file:
                line = line.strip()

                if not line: # same as: if line == ""
                    continue

                parts = line.split(',')

                if len(parts) != 4:
                    print(f"Invalid file format.\n")
                    continue

                try:
                    amount = float(parts[0])
                    category = parts[1]
                    date = datetime.strptime(parts[2], "%Y-%m-%d")
                    description = parts[3]

                    expenses.append(Expense(amount, category, date, description))

                except ValueError:
                    print(f"Error parsing line: {line}")

        print("Load successful.\n")

    except FileNotFoundError:
        print('File not found.\n')

    except Exception:
        print('An error occurred while loading data.\n')
        
# Calculate Total Expenses Function
def total_expenses(expenses):
    total = 0
    if not expenses:
        print('No expenses found.\n')
        input("Press enter to continue...")
        return

    for expense in expenses:
        total += expense.amount

    print(f'Total expenses: ${total:.2f}\n')

# MAIN
while continue_program:
    # Display menu
    choice = menu()

    if choice == 1:     # 1. Add Expense (Progressive Goal: Layer 1 - Functional Minimal)
        add_expense(expenses)
        input("Press enter to continue...")

    elif choice == 2:   # 2. View Expenses (Progressive Goal: Layer 1 - Functional Minimal)
        view_expenses(expenses)
        input("Press enter to continue...")

    elif choice == 3:   # 3. Delete Expense (Progressive Goal: Layer 2 - Low Target)
        delete_expense(expenses)
        input("Press enter to continue...")

    elif choice == 4:   # 4. Update Expense (Progressive Goal: Layer 2 - Low Target)
        update_expense(expenses)
        input("Press enter to continue...")

    elif choice == 5:   # 5. Save Data (Progressive Goal: Layer 1 - Functional Minimal)
        save_data(expenses)
        input("Press enter to continue...")

    elif choice == 6:   # 6. Load Data (Progressive Goal: Layer 1 - Functional Minimal)
        load_data(expenses)
        input("Press enter to continue...")
        
    elif choice == 7:   # 7. Calculate Total Expenses (Progressive Goal: Layer 3 - Desirable Target)
        total_expenses(expenses)
        input("Press enter to continue...")

    elif choice == 8:   # 8. Quit
        print("Program successfully terminated. Thank you!")
        continue_program = False

    else:
        print("Invalid choice, try again.\n")




