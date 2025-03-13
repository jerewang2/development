def display_recipes():
    print('\nAvailable Recipes:')
    print('Crafting Table: 4 wood')
    print('Pickaxe: 3 wood + 2 sticks')

def mine_wood():
    print("Mining 1 wood...")
    print("Mined 1 wood!")
    return 1

def mine_stick():
    print("Mining 1 stick...")
    print("Mined 1 stick!")
    return 1

def craft_crafting_table(wood_inv):
    if wood_inv < 4:
        print('Sorry, not enough wood.')
        return wood_inv - 0, 0
    else:
        print('Crafting 1 crafting table...')
        print('Crafted 1 crafting table!')
        return wood_inv - 4, 1
    
def craft_pickaxe(wood_inv, stick_inv):
    if wood_inv < 3 or stick_inv < 2:
        print('Sorry, not enough material.')
        return wood_inv - 0, stick_inv - 0, 0
    else:
        print('Crafting 1 pickaxe...')
        print('Crafted 1 pickaxe!')
        return wood_inv - 3, stick_inv - 2, 1

def display_inventory(inv):
    for material in inv:
        print(f'{material[0]}: {material[1]}')    

if __name__ == '__main__':
    print("Welcome to Mini Miner!")
    print("Your mission is to craft 1 of each of the shown recipes:")

    display_recipes()

    print("Let's start your adventure!")

    wood = 0
    sticks = 0
    crafting_table = 0
    pickaxe = 0

    while True:
        print('\nMain Menu:')
        print('1. Display Inventory')
        print('2. Mine Wood')
        print('3. Mine Stick')
        print('4. Craft Crafting Table')
        print('5. Craft Pickaxe')
        
        choice = input("What would you like to do? ")
        print("")
        if choice == '1':
            display_inventory((('wood', wood), ('sticks', sticks), ('crafting table', crafting_table), ('pickaxe', pickaxe)))
        elif choice == '2':
            wood += mine_wood()
        elif choice == '3':
            sticks += mine_stick()
        elif choice == '4':
            wood, crafting_table = craft_crafting_table(wood)
        elif choice == '5':
            wood, sticks, pickaxe = craft_pickaxe(wood, sticks)
        else:
            print("Sorry, incorrect input. Please try again.")

        if crafting_table == 1 and pickaxe == 1:
            print("Congratulations! You completed your mission!")
            print('Thank you for playing!\n')
            break