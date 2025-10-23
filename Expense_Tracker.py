Expenses = []
Categories = [
        "Food | Social Life | Pets | Transport | Culture | Household | Apparel | Beauty | Health | Education | Gift | Others"
    ]
def main():
    print("Choose Option\n 1.Add Expense | 2. View Expense | 3. Show total | 4. Exit")
    user_input = input("Option: ")
    if int(user_input) == 1 or user_input == "Add Expense":
        cost = int(input("Cost:" ))
        print(*Categories)
        category = input("Which Category? ")
        add_expense(cost, category)
    elif int(user_input) == 2 or user_input == "View Expense":
        view_expense()
    elif int(user_input) == 3 or user_input == "Show Total":
        show_total()
    elif int(user_input) == 4 or user_input == "Exit":
        run_exit()
    else:
        print("Enter a valid choice")
    print(Expenses)

def add_expense(cost, category):
    Expenses.append({f"Expense": {cost}, "Category" : category})


if __name__ == "__main__":
    main()