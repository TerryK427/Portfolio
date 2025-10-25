import json

Categories = [
        "Food | Social Life | Pets | Transport | Culture | Household | Apparel | Beauty | Health | Education | Gift | Others"
    ]
def main():
    while True:
        print("Choose Option\n 1.Add Expense | 2. View Expense | 3. Show total | 4. Exit")
        user_input = input("Option: ")
        if int(user_input) == 1 or user_input == "Add Expense":
            Name = input("Usage: ")
            cost = float(input("Cost:" ))
            print(*Categories)
            category = input("Which Category? ")
            add_expense(Name, cost, category)
        elif int(user_input) == 2 or user_input == "View Expense":
            view_expense()
        elif int(user_input) == 3 or user_input == "Show Total":
            show_total()
        elif int(user_input) == 4 or user_input == "Exit":
            exit()
        else:
            print("Enter a valid choice")

def add_expense(Name, cost, category):
    try:
        with open("total_expenses.json", "r") as f:
            expense = json.load(f)
            if isinstance(expense, dict):
                expense = [expense]
    except (FileNotFoundError, json.JSONDecodeError):
        expense = []
    new_expense = {f"Name": Name,"Cost": cost, "Category" : category}
    expense.append(new_expense)
    with open("total_expenses.json", "w") as f:
        json.dump(expense, f, indent=4)
    print("Expense added!")


def view_expense():
    try:
        with open("total_expenses.json", "r") as f:
            expenses = json.load(f)
            total = 0
            for i in expenses:
                print(i["Cost"], "used for", i["Name"], "in", i["Category"])
                total += i["Cost"]
            print("-----------------------------------------\nTotal used:", total)
    except FileNotFoundError:
        print("No Expenses saved!")

def show_total():
    try:
        with open("total_expenses.json", "r") as f:
            expenses = json.load(f)
            total = sum(i["Cost"] for i in expenses)
            print(f"Total Used: {total}")
    except FileNotFoundError:
        print("No expenses found!")

if __name__ == "__main__":
    main()