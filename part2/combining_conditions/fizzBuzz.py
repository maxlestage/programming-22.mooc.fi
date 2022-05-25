""" 
Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

Some examples of expected behaviour:

Sample output
Number: 9
Fizz

Sample output
Number: 7

Sample output
Number: 20
Buzz

Sample output
Number: 45
FizzBuzz
"""

number = int(input("Number: "))

if number % 3 == 0 & number % 5 == 0:
    print("FizzBuzz")
elif number % 3:
    print("Fizz")
elif number % 5:
    print("Buzz")
else:
    print("")


# Alternative :
if number % 15 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

# Correction :
if number % 3 == 0 and number % 5 == 0:
    # This condition must be evaluated first, because if this is true,
    # also both of the following conditions are true
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
