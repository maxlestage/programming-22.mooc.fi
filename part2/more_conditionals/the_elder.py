""" 
Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

Some examples of expected behaviour:

Sample output
Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada

Sample output
Person 1:
Name: Bill
Age: 1
Person 2:
Name: Jean
Age: 1
Bill and Jean are the same age
"""
print(f"Person 1: ")
person_1 = str(input("Name: "))
age_1 = int(input("Age: "))

print(f"Person 2: ")
person_2 = str(input("Name: "))
age_2 = int(input("Age: "))

if age_1 > age_2:
    print(f"The elder is {person_1}")
elif age_1 < age_2:
    print(f"The elder is {person_2}")
else:
    print(f"{person_1} and {person_2} are the same age")


# Correction, façon de faire alternantive :

print("Person 1:")
name1 = input("Name: ")
age1 = int(input("Age: "))

print("Person 2:")
name2 = input("Name: ")
age2 = int(input("Age: "))

if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")
