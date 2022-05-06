""" 
Please write a program which asks the user for a number. The program then prints out the number multiplied by five.

The program should function as follows:

Sample output
Please type in a number: 3
3 times 5 is 15 
"""
give_a_number = int(input("Please type a number: "))
default_number = 5
print(f"{give_a_number} times {default_number} is {give_a_number*default_number} ")


##################################
# Correction :
number = input("Please type in a number: ")
result = int(number) * 5
print(f"{number} times 5 is {result}")
