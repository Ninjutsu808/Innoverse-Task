def calculated_savings(expenses, income):
    if expenses > income:
        print("Seems like you are spending more than you earn")
    elif expenses == income:
        print(" this is not healthy, you are spending all you earn")
    
    elif expenses < income:
        savings = income - expenses
        print(f"You are saving {savings} per month")
        if  0 < savings < (0.2 * income):
           print("You should try to save more")
        elif (0.2 * income) <= savings < (0.5 * income):
           print("You are doing good, try to save even more")
        else :
           print("You are doing great, keep it up")  

    return 0
         

print("Welcome to the budget calculator \n" 
"Please enter your monthly income and expenses below")

monthly_income = float(input("Enter your monthly income: $"))
print("\naccording to your income your expenses should be divided as follows: \n" \
      "Food: $" + str(monthly_income* 0.25) +  "\n" \
      "Utilities: $" + str(monthly_income* 0.25) +  "\n" \
      "Transportation: $" + str(monthly_income* 0.20) +  "\n" \
      "Entertainment: $" + str(monthly_income* 0.10) +  "\n" \
      "Miscellaneous: $" + str(monthly_income* 0.20) +  "\n" )
      
monthly_total_expenses = float(input("Enter your monthly total expenses: $")) 

savings = monthly_income - monthly_total_expenses 


calculated_savings(monthly_total_expenses, monthly_income)

print("Please divide your expenses into the following categories")
food = float(input("Enter your monthly food expenses: $"))      
transportation = float(input("Enter your monthly transportation expenses: $"))
utilities = float(input("Enter your monthly utilities expenses: $"))
entertainment = float(input("Enter your monthly entertainment expenses: $"))
miscellaneous = float(input("Enter your monthly miscellaneous expenses: $"))
calculated_expense = food + transportation + utilities + entertainment + miscellaneous 
if calculated_expense != monthly_total_expenses:
    print("The sum of your categorized expenses does not match your total expenses. Please check your entries.")
    exit ()
else:
    print("Your categorized expenses match your total expenses.")

category_weight = {
    "food" : monthly_income * 0.25,
    "transportation" : monthly_income * 0.20,
    "utilities" : monthly_income * 0.25,
    "entertainment" : monthly_income * 0.10,
    "miscellaneous" : monthly_income * 0.20
}
actual_expenses = {
    "food": food,
    "transportation": transportation,
    "utilities": utilities,
    "entertainment": entertainment,
    "miscellaneous": miscellaneous
}


with open("budget_report.txt", "w") as file:
    file.write("Budget Report\n")
    file.write(f"Monthly Income: ${monthly_income}\n \
                Monthly Expenses: ${monthly_total_expenses}\n \
                Monthly Savings: ${savings}\n\n")
    file.write("Category Breakdown:\n")
    for category in actual_expenses:
        file.write(f"{category.capitalize()}: ${actual_expenses[category]}\n")

    file.write("\nAdvice Section:\n")
    for category in category_weight:
        expected = category_weight[category]
        actual = actual_expenses[category]
        if actual > expected:
            file.write(f"Overspending in {category}, try to cut back.\n")
        elif actual == expected:
            file.write(f"Spending correctly in {category}, keep it up.\n")
        else:
            file.write(f"Doing great in {category}, well managed.\n")
print(f"report has been generated - {file.name}")




