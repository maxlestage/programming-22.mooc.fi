""" 
The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

points	grade
< 0	impossible!
0-49	fail
50-59	1
60-69	2
70-79	3
80-89	4
90-100	5
> 100	impossible!
Some examples:

Sample output
How many points [0-100]: 37
Grade: fail

Sample output
How many points [0-100]: 76
Grade: 3

Sample output
How many points [0-100]: -3
Grade: impossible!

"""

note = int(input("How many points [0-100]: "))

if note < 0:
    print("impossible!")
elif note >= 0 and note <= 49:
    print("fail")
elif note >= 50 and note <= 59:
    print("1")
elif note >= 60 and note <= 69:
    print("2")
elif note >= 70 and note <= 79:
    print("3")
elif note >= 80 and note <= 89:
    print("4")
elif note >= 90 and note <= 100:
    print("5")
else:
    print("impossible!")

# Alternative :
points = int(input("How many points [0-100]: "))

if points < 0 or points > 100:
    grade = "impossible!"
elif points < 50:
    grade = "fail"
elif points < 60:
    grade = "1"
elif points < 70:
    grade = "2"
elif points < 80:
    grade = "3"
elif points < 90:
    grade = "4"
else:
    grade = "5"

print(f"Grade: {grade}")
