print("\nWelcome to Aji~")
print("We are a Japanese inspired establishment designed to provide a memorable tasting experience.")
print("My name is Eve and I will be your server today. Here is our menu for this evening.\n")

print("Beverages:")
print("Water                 -")
print("Genmaicha             4")
print("Yuzu                  3")
print("Umesha                8")

print("\nAppetizers:")
print("Yakitori               ")
print("  Momo                8")
print("  Tsukune             7")
print("  Torinegi            8")
print("Edamame               5")
print("Chawanmushi           10")

print("\nEntrees:")
print("Omakase (10 piece)    75")
print("Tonkatsu Ramen *      25")
print("Sukiyaki *            30")
print("Tempura Tasting       50")
print("Tonkatsu              25")
print("Kaiseki               75")
print("* add egg for $2")

print("\nDesserts:")
print("Cheesecake *          15")
print("Mochi Assortment      12")
print("Matcha Crepe *        10")
print("Milk Pudding          10")
print("* add tea for $2\n")

print("I am happy to take your order.\n")

total = 0

drink = input("Which drink would you like to have?\n")
if drink.lower() == 'water':
    total += 0
elif drink.lower() == 'genmaicha':
    total += 4
elif drink.lower() == 'yuzu':
    total += 3
elif drink.lower() == 'umesha':
    total += 7
else:
    print("Sorry, that was an invalid input. Please rerun the code.\n")

print(f'Current total: ${total}.\n')

appetizer = input("Which appetizer would you like to have?\n")
if appetizer.lower() == 'momo':
    total += 8
elif appetizer.lower() == 'tsukune':
    total += 7
elif appetizer.lower() == 'torinegi':
    total += 8
elif appetizer.lower() == 'edamame':
    total += 5
elif appetizer.lower() == 'chawanmushi':
    total += 10
else:
    print("Sorry, that was an invalid input. Please rerun the code.\n")

print(f'Current total: ${total}.\n')

entree = input("Which entree would you like to have?\n")
if entree.lower() == 'omakase':
    total += 75
elif entree.lower() == 'tonkatsu ramen':
    total += 25
    egg = input("Would you like to add an egg? (yes/no)")
    if egg.lower() == 'yes':
        total += 2
elif entree.lower() == 'sukiyaki':
    total += 30
    egg = input("Would you like to add an egg? (yes/no)")
    if egg.lower() == 'yes':
        total += 2
elif entree.lower() == 'tempura tasting':
    total += 50
elif entree.lower() == 'tonkatsu':
    total += 25
elif entree.lower() == 'kaiseki':
    total += 75
else:
    print("Sorry, that was an invalid input. Please rerun the code.\n")

print(f'Current total: ${total}.\n')

dessert = input("Which dessert would you like to have?\n")
if dessert.lower() == 'cheesecake':
    total += 15
    tea = input("Would you like to hot tea to go with your cheesecake? (yes/no)")
    if tea.lower() == 'yes':
        total += 2
elif dessert.lower() == 'mochi assortment':
    total += 12
elif dessert.lower() == 'matcha crepe':
    total += 10
    tea = input("Would you like to hot tea to go with your matcha crepe? (yes/no)")
    if tea.lower() == 'yes':
        total += 2
elif dessert.lower() == 'milk pudding':
    total += 10
else:
    print("Sorry, that was an invalid input. Please rerun the code.\n")

print(f'Your total for today is ${total}.')
tip = input("Would you like add a tip? (0%, 5%, 10%, 15%, 20%, custom)")
if tip == '0%':
    pass
elif tip == '5%':
    total *= 1.05
elif tip == '10%':
    total *= 1.10
elif tip == '15%':
    total *= 1.15
elif tip == '20%':
    total *= 1.20
elif tip == 'custom':
    custom = float(input("How much would you like to tip?"))
    total += custom
else:
    print("Sorry, that was an invalid input. Please rerun the code.\n")

print(f'Thank you! Your final total is ${total}. Enjoy the rest of your evening~')