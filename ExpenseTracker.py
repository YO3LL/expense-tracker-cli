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
ContinueProgram = True # Decides when to terminate program

# Vector that holds all expenses
expenses = []

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

while ContinueProgram:

    # Display menu
    choice = menu()

    # "1. Add Expense":
    if choice == 1:
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

    # "2. View Expenses":
    elif choice == 2:
        if not expenses:
            print('\nNo expenses recorded.\n')
        else:
            print('\nExpenses:')
            print(expenses) # view expenses
        print() # newline

    # "3. Delete Expense":
    elif choice == 3:
        for i, expense in enumerate(expenses):
            print(i+1, ". ", expense)
        print("Select which option to remove: ",end=" ") ##### LEFT OFF HERE. Change 12

    elif choice == 4:
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



