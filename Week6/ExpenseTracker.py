from datetime import datetime

expense_records = []
category_totals = {}
unique_categories = set()

# store as tuples
overall_total = {
    "highest": (0, ""),
    "lowest": (float('inf'), ""),
    "total": 0
}

def report():
    global overall_total
    
    # Reset totals each time report is run
    overall_total = {
        "highest": (0, ""),
        "lowest": (float('inf'), ""),
        "total": 0
    }

    categorization()

    # Print category totals
    for category, total in category_totals.items():
        print(f"{category}: {total}")

    # Determine highest, lowest, total
    for category, total in category_totals.items():
        # highest
        if total > overall_total["highest"][0]:
            overall_total["highest"] = (total, category)

        # lowest
        if total < overall_total["lowest"][0]:
            overall_total["lowest"] = (total, category)

        # sum
        overall_total["total"] += total

    print("\n--- Expense Summary ---")
    print(f"Highest Expense: ${overall_total['highest'][0]} in category '{overall_total['highest'][1]}'")
    print(f"Lowest Expense:  ${overall_total['lowest'][0]} in category '{overall_total['lowest'][1]}'")
    print(f"Overall Total Expenses: ${overall_total['total']}\n")

def categorization():
    category_totals.clear()
    unique_categories.clear()

    for category, amount, _ in expense_records:
        category_totals[category] = category_totals.get(category, 0) + amount
        if category not in unique_categories:
            unique_categories.add(category)

def validate_date_format(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date
    except ValueError:
        print("Invalid date format.")
        return None


# Main loop
while True:
    command = input("\nEnter command ('report', 'exit', or ENTER to add expense):\n")
    
    match command.lower():
        case "exit":
            print("Exiting program...")
            report()
            break
        
        case "report":
            report()
        
        case _:
            category = input("Enter expense category:\n")
            amount = float(input("Enter expense amount:\n"))
            date = validate_date_format(input("Enter expense date (YYYY-MM-DD):\n"))
            expense_records.append((category, amount, date))
            print(f"Added expense: {category}, {amount}, {date}")
        