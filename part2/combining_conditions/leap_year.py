""" Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

Some examples:

Sample output
Please type in a year: 2011
That year is not a leap year.

Sample output
Please type in a year: 2020
That year is a leap year.

Sample output
Please type in a year: 1800
That year is not a leap year. """


Year = int(input("Please type in a year:  "))

if Year % 4 == 0 and Year % 100 != 0:
    print("That year is a leap year.")
elif Year % 100 == 0 and Year % 400 != 0:
    print("That year is not a leap year")
elif Year % 400 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year")


# Correction :
year = int(input("Please type in a year: "))

# First, we make assumption that a year is not a leap year
leap_year = False

if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True

if leap_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
