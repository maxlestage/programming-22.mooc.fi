""" 
Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

Some examples of expected behaviour:

Sample output
What is the weather forecast for tomorrow?
Temperature: 21
Will it rain (yes/no): no
Wear jeans and a T-shirt

Sample output
What is the weather forecast for tomorrow?
Temperature: 11
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well

Sample output
What is the weather forecast for tomorrow?
Temperature: 7
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you

Sample output
What is the weather forecast for tomorrow?
Temperature: 3
Will it rain (yes/no): yes
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you
Make it a warm coat, actually
I think gloves are in order
Don't forget your umbrella!

"""
print(f"What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = str(input("Will it rain (yes/no): "))

if rain == "no":
    if temperature > 20:
        print(f"Wear jeans and a T-shirt")

    if temperature <= 20 and temperature >= 10:
        print(f"Wear jeans and a T-shirt")
        print(f"I recommend a jumper as well")
    if temperature == 10:
        print(f"Take a jacket with you")
    if temperature < 10 and temperature >= 5:
        print(f"Wear jeans and a T-shirt")
        print(f"I recommend a jumper as well")
        print(f"Take a jacket with you")
    if temperature <= 5:
        print(f"Wear jeans and a T-shirt")
        print(f"I recommend a jumper as well")
        print(f"Take a jacket with you")
        print(f"Make it a warm coat, actually")
        print(f"I think gloves are in order")
else:
    if temperature > 20:
        print(f"Wear jeans and a T-shirt")
        print(f"Don't forget your umbrella!")
    if temperature <= 20 and temperature >= 10:
        print(f"Wear jeans and a T-shirt")
        print(f"I recommend a jumper as well")
        print(f"Don't forget your umbrella!")
    if temperature < 10 and temperature >= 5:
        print(f"Wear jeans and a T-shirt")
        print(f"I recommend a jumper as well")
        print(f"Take a jacket with you")
        print(f"Don't forget your umbrella!")
    if temperature <= 5:
        print(f"Wear jeans and a T-shirt")
        print(f"I recommend a jumper as well")
        print(f"Take a jacket with you")
        print(f"Make it a warm coat, actually")
        print(f"I think gloves are in order")
        print(f"Don't forget your umbrella!")

# Correction :

print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")
if temperature < 21:
    print("I recommend a jumper as well")
if temperature < 11:
    print("Take a jacket with you")
if temperature < 6:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")
