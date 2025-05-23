# TIP CALCULATOR
print("Welcome to the Tip Calculator!")
print("")

price = int(input("Enter the bill (before taxes and tips): "))
if(price > 100):
    print("Must be one fancy dinner your having!")
    print("")


tipPercent = int(input("Enter the tip percentage (5, 10, 20...): %"))
if(tipPercent > 15):
    print("In this economy!? Might as well be paying their wage at that point!")
    print("")


taxPercent = int(input("Enter the tax percentage (5, 10, 20...): %"))
if(taxPercent > 10 and tipPercent > 10 and price > 75):
    print("This may end up becoming quite the pricey feast.")
    print("")


numberOfPeople = int(input("Enter the number of people the bill will be split among: "))
if(numberOfPeople == 1 and price > 75):
    print("Either your treating yourself to a great meal or your just very nice to your friends.")
    print("")
print("")

tip = round((tipPercent/100) * price, 2)
tax = round((taxPercent/100) * price, 2)
total = round(price + tip + tax, 2)
pricePerPerson = round(total / numberOfPeople, 2)

print("According to my calculatoins...")
print("")

print(f"Before taxes and tips")
print("")

print(f"Subtotal: {price}")
print(f"Tip (%{tipPercent}): {tip}")
print(f"Tax (%{taxPercent}): {tax}")
print("")
print("")

print(f"After taxes and tips")
print("")

print(f"Total Bill: {total}")
print(f"Price Per Person: {pricePerPerson}")