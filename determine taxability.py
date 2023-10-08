def determine_taxability():
    age = int(input("Please enter the inhabitant's age: "))
    sexe = input("Please enter the inhabitant's gender (M for male, F for female): ").upper()

    if (sexe == "M" and age > 20) or (sexe == "F" and age >= 18 and age <= 35):
        print("The inhabitant is taxable.")
    else:
        print("The inhabitant is not taxable.")
determine_taxability()
20