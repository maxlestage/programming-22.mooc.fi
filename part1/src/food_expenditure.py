""" 
Please write a program which estimates a user's typical food expenditure.

The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

Based on this information the program calculates the user's typical food expenditure both weekly and daily.

The program should function as follows:

Sample output
How many times a week do you eat at the student cafeteria? 4
The price of a typical student lunch? 2.5
How much money do you spend on groceries in a week? 28.5

Average food expenditure:
Daily: 5.5 euros
Weekly: 38.5 euros
"""
nb_times_cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
typical_price = float(input("The price of a typical student lunch? "))
money_spend_in_week = float(input("How much money do you spend on groceries in a week? "))
print(
    f"Average food expenditure:\nDaily: {((typical_price*nb_times_cafeteria)+money_spend_in_week)/7} euros\nWeekly: {(typical_price*nb_times_cafeteria)+money_spend_in_week} euros"
)

# Correction cause different way to solve it :
times_in_cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
price_of_lunch = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

weekly = groceries + times_in_cafeteria * price_of_lunch

print("Average food expenditure:")
print(f"Daily: {weekly / 7} euros")
print(f"Weekly: {weekly} euros")
