""" 
Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

Sample output
Hourly wage: 8.5
Hours worked: 3
Day of the week: Monday
Daily wages: 25.5 euros

Sample output
Hourly wage: 12.5
Hours worked: 10
Day of the week: Sunday
Daily wages: 250.0 euros
"""
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_the_week = str(input("Day of the week: "))

if day_of_the_week != "Sunday":
    print(f"Daily wages: {hourly_wage*hours_worked} euros")

if day_of_the_week == "Sunday":
    print(f"Daily wages: {(hourly_wage*hours_worked) *2} euros")


# Autre façon de faire :
hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
weekday = input("Day of the week: ")

if weekday == "Sunday":
    # The salary is double on Sundays
    hourly_wage *= 2

total_wage = hourly_wage * hours_worked
print(f"Daily wages: {total_wage} euros")
