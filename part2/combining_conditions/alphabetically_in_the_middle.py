""" Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

Sample output
1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

Sample output
1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B """


letter_1 = str(input("1st letter: "))
letter_2 = str(input("2nd letter: "))
letter_3 = str(input("3rd letter: "))

if letter_1.lower().lower() < letter_2.lower():  # Si letter1 inf à letter2
    if letter_2.lower() > letter_3.lower():  # Si letter2 supp à letter3
        if letter_3.lower() > letter_1.lower():  # Si letter3 supp à letter1
            print(f"The letter in the middle is {letter_3} tata")

if letter_1.lower() < letter_2.lower():  # Si letter1 inf à letter2
    if letter_2.lower() > letter_3.lower():  # Si letter2 supp à letter3
        if letter_3.lower() < letter_1.lower():  # Si letter3 supp à letter1
            print(f"The letter in the middle is {letter_1} tbtb")

if letter_1.lower() > letter_2.lower():  # Si letter1 supp à letter2
    if letter_2.lower() > letter_3.lower():  # Si letter2 supp à letter3
        if letter_3.lower() < letter_1.lower():  # Si letter3 supp à letter1
            print(f"The letter in the middle is {letter_2} tctc")

if letter_1.lower() < letter_2.lower():  # Si letter1 inf à letter2
    if letter_2.lower() < letter_3.lower():  # Si letter2 inf à letter3
        if letter_3.lower() > letter_1.lower():  # Si letter3 supp à letter1
            print(f"The letter in the middle is {letter_2} tdtd")


if letter_1.lower() > letter_2.lower():  # Si letter1 inf à letter2
    if letter_2.lower() < letter_3.lower():  # Si letter2 inf à letter3
        if letter_3.lower() > letter_1.lower():  # Si letter3 inf à letter1
            print(f"The letter in the middle is {letter_1} tete")

if letter_1.lower() > letter_2.lower():  # Si letter1 supp à letter2
    if letter_2.lower() < letter_3.lower():  # Si letter2 inf à letter3
        if letter_3.lower() < letter_1.lower():  # Si letter3 inf à letter1
            print(f"The letter in the middle is {letter_3} tftf")


# Correction :
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if letter1 > letter2 and letter1 > letter3:
    if letter2 > letter3:
        middle = letter2
    else:
        middle = letter3
elif letter2 > letter3:
    if letter3 > letter1:
        middle = letter3
    else:
        middle = letter1
else:
    if letter2 > letter1:
        middle = letter2
    else:
        middle = letter1

print("The letter in the middle is " + middle)
