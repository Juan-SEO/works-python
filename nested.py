height = int(input("What is your height? "))
age = int(input("How old are you? "))

if height > 120:
    print("puedes montar")
    if age < 12:
        print("Pagas 5$")
    elif age >= 12 and age <= 18:
        print("Pagas 7$")
    else:
        print("Pagas 12$")
else:
    print("No puedes montar")