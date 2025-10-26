import json
# """
# Add "Sort by category", "Search"
# Clean up
# Final Push
# """
Categories = [ #List of all categories in order to iterate
        "Food", "Social Life", "Pets", "Transport", "Culture", "Household", "Apparel", "Beauty", "Health", "Education", "Gift", "Others"
    ]
Category_Text = "Food | Social Life | Pets | Transport | Culture | Household | Apparel | Beauty | Health | Education | Gift | Others"
def main():
    while True: #Main Func, takes in user input and runs correct process
        print("Choose Option\n 1.Add Expense | 2. Remove Expense | 3. View Expense | 4. Search for Expense | 5. Sort by Category | 6. Exit")
        user_input = input("Option: ")
        if (user_input.isdigit() and int(user_input) == 1) or str(user_input.lower()) == "add expense":
            Name = input("Usage: ")
            cost = float(input("Cost:" ))
            print(Category_Text)
            category = input("Which Category? ")
            add_expense(Name, cost, category)
        elif (user_input.isdigit() and int(user_input) == 2) or user_input.lower() == "remove expense":
            with open("total_expenses.json", 'r') as f:
                expenses = json.load(f)
            for i in expenses:
                print(i["Name"], "---", i["Cost"])
            desired_expense = input("Which expense would you like to remove: ")
            remove_expense(desired_expense)
        elif (user_input.isdigit() and int(user_input) == 3) or user_input.lower() == "view expense":
            view_expense()
        elif (user_input.isdigit() and int(user_input) == 4) or user_input.lower() == "search for expense":
            search_for_expense()
        elif (user_input.isdigit() and int(user_input) == 5) or user_input.lower() == "sort by category":
            sort_by_category()
        elif (user_input.isdigit() and int(user_input) == 6) or user_input.lower() == "exit":
            exit()
        else:
            print("Enter a valid choice")

def add_expense(Name, cost, category): #Add Expense
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

def remove_expense(Name): #Remove Expense
        try:
            with open("total_expenses.json", "r") as f:
                expenses = json.load(f)
            if isinstance(expenses, dict):
                expenses = [expenses]
            matches = [count for count in expenses if count["Name"].lower() == Name.lower()]
            if len(matches) == 1:
                expenses.remove(matches[0])
            else:
                print(f"Multiple expenses fonud for", Name)
                for number, i in enumerate(matches, start=1):
                    print(f"{number} Cost: {i["Cost"]} | Category: {i["Category"]}")
                while True:
                    try:
                        choice = int(input("Which expense would you like to remove? "))
                        if 1 <= choice <= len(matches):
                            expenses.remove(matches[choice-1])
                            print("Removed Expense")
                            break
                        else:
                            print("Please Enter a Valid Number")
                    except ValueError:
                        print("Please enter a Valid Number")
            with open("total_expenses.json", "w") as f:
                json.dump(expenses, f, indent=4)
        except FileNotFoundError:
            print("File Not Found!")

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


if __name__ == "__main__":
    main()