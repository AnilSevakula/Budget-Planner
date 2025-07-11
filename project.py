import os
import sys

DATA_FILE = "data.txt"


def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as _:
            pass
        return 0, []
    income = 0
    expenses = []
    with open(DATA_FILE, "r") as file:
        try:
            income = float(file.readline().strip())
            for row in file.readlines():
                category, amt = row.strip().split(",")
                expenses.append((category, amt))
        except ValueError:
            pass

    return income, expenses


def add_expense(expenses):
    category = input("Enter Expense Category: ").lower()
    while True:
        try:
            amt = float(input("Enter Expense Amount: "))
            if amt < 0:
                raise ValueError
            expenses.append((category, amt))
            with open(DATA_FILE, "a") as file:
                file.write('\n' + category + "," + str(amt))
            break
        except ValueError:
            print("Please enter valid amount")
    print("Expense has been added!!!")


def set_income(expenses):
    income = 0
    while True:
        try:
            income = float(input("Enter your Income:"))
            if income < 0:
                print("Income must be positive")
                continue
            write_all_data(income, expenses)
            break
        except ValueError:
            print("Income must be float or integer")
            continue
    print("Income has been set to", income)
    return income


def delete_expense(income, expenses):
    if not expenses:
        print("There were no expenses to delete")
        return []
    print("List of your expenses")
    for i, ex in enumerate(expenses):
        print(f"{i + 1}. {ex[0]} : {ex[1]}")
    while True:
        try:
            choice = int(input("Select the expense number to delete: "))
            if choice < 1 or choice > len(expenses):
                raise ValueError
        except ValueError:
            print("Invalid choice of expenses")
        else:
            break
    expenses.pop(choice - 1)
    write_all_data(income, expenses)
    print("Expense deleted successfully!!!")


def edit_expense(income, expenses):
    if not expenses:
        print("There were no expenses to edit")
        return
    print("List of your expenses")
    for i, ex in enumerate(expenses):
        print(f"{i + 1}. {ex[0]} : {ex[1]}")
    while True:
        try:
            choice = int(input("Select the expense number to edit: "))
            if choice < 1 or choice > len(expenses):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice of expenses")
    i = 1
    for category, amt in expenses:
        if i == choice:
            print("\n1.Edit expense category")
            print("2.Edit expense amount")
            while True:
                try:
                    ch = int(input("Enter your choice: "))
                    if ch < 1 or ch > 2:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid choice")
            if ch == 1:
                new_category = input("Enter new category name: ")
                expenses[i - 1] = (new_category, amt)
            elif ch == 2:
                while True:
                    try:
                        new_amt = float(input("Enter new expense amount: "))
                        if new_amt < 0:
                            raise ValueError
                        expenses[i - 1] = (category, new_amt)
                        break
                    except ValueError:
                        print("Invalid amount")
            break
        i += 1
    write_all_data(income, expenses)
    print("Expense edited successfully!!!")


def write_all_data(income, expenses):
    with open(DATA_FILE, "w") as file:
        file.write(str(income))
        for category, amt in expenses:
            file.write('\n' + category + "," + str(amt))


def view_expenses(expenses):
    total = 0
    if not expenses:
        print("No Expenses to show")
        return
    print("\nList of all your Expenses:")
    for category, amt in expenses:
        print(f"{category} : {amt}")
        total += float(amt)


def view_summary(income, expenses):
    total = 0
    exp = {}
    print("\nSummary of your Expenses")
    for category, amt in expenses:
        if category not in exp.keys():
            exp[category] = float(amt)
        else:
            exp[category] += float(amt)
        total += float(amt)
    for category in exp.keys():
        print(f"{category} : {exp[category]}")
    print("Total Expenses:", total)
    print("Total Income:", income)
    print("Balance:", income - total)


def clear():
    with open(DATA_FILE, "w") as _:
        pass
    print("All items have been cleared!!!")


def main():
    income, expenses = load_data()
    while True:
        print("\n===SIMPLE BUDGET PLANNER===")
        print("1. Set Income")
        print("2. Add Expense")
        print("3. View All Expenses")
        print("4. View Summary")
        print("5. Clear All Items")
        print("6. Delete an Expense")
        print("7. Edit an Expense")
        print("8. Save and Exit")
        print("===========================\n")
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 8:
                raise ValueError
        except ValueError:
            print("Invalid Choice")
            continue
        if choice == 1:
            income = set_income(expenses)
        elif choice == 2:
            add_expense(expenses)
        elif choice == 3:
            view_expenses(expenses)
        elif choice == 4:
            view_summary(income, expenses)
        elif choice == 5:
            clear()
            income, expenses = 0, []
        elif choice == 6:
            delete_expense(income, expenses)
        elif choice == 7:
            edit_expense(income, expenses)
        elif choice == 8:
            sys.exit("Saved!!\nGood Bye")
        else:
            print("Invalid Choice")


if __name__ == '__main__':
    main()
