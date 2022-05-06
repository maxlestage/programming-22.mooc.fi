""" 
Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

The program should function as follows:

Sample output
Number 1: 2
Number 2: 1
Number 3: 6
Number 4: 7
The sum of the numbers is 16 and the mean is 4.0
"""
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
num3 = int(input("Number 3:"))
num4 = int(input("Number 4:"))

print(f"The sum of the numbers is {num1+num2+num3+num4} and the mean is {(num1+num2+num3+num4)/4}")

# Correction cause different way :
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))
number4 = int(input("Number 4: "))

sum = number1 + number2 + number3 + number4

print(f"The sum of the numbers is {sum} and the mean is {sum/4}")
