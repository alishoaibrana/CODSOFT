import os

while True:
    opr1 = int(input("Enter the 1 digit = "))
    opr2 = int(input("Enter the 2 digit = "))
    opr = input("Select Operation to perform (+,-,*,/) = ")

    if opr == '+':
        print(f"{opr1} {opr} {opr2} = {opr1 + opr2}")
    elif opr == '-':
        print(f"{opr1} {opr} {opr2} = {opr1 - opr2}")
    elif opr == '*':
        print(f"{opr1} {opr} {opr2} = {opr1 * opr2}")
    elif opr == '/':
        if opr2 == 0:
            print("ERROR: Cannot divide by 0")
            continue
        result = round(opr1 / opr2, 3)
        print(f"{opr1} {opr} {opr2} = {result}")

    choice = input("Do you want to perform more Calculations (yes/no): ")
    if choice.lower() != "yes":
        print("Thanks have a Nice Day")
        break

    os.system('cls')

