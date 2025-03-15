import random

class Hero:
    def __str__(self):
        return "This is Jeremy's hero class!"
    
    def __init__(self):
        self.name = input("Please choose a name for your hero: ")
        self.INVENTORY = {'HP Potion': ['health potion', 'health potion', 'health potion'],
                          'Mana Potion': ['mana potion', 'mana potion', 'mana potion']}
        self.HP = random.randint(95, 105)
        self.MANA = 100
        self.ATK = random.randint(10, 12)
        self.DEF = random.randint(5, 7)
        self.ATK_LUCK = 90

        self.display_stats()

    def display_stats(self):
        print(f'\nHero Name: {self.name}')
        print(f'HP: {self.HP}')
        print(f'Inventory: {self.INVENTORY}')
        print(f'Mana: {self.MANA}')
        print(f'Attack: {self.ATK}')
        print(f'Defense: {self.DEF}')
        print(f'Attack Luck: {self.ATK_LUCK}')
    
    def normal_attack(self):
        if random.randint(0, 100) < self.ATK_LUCK:
            print(f'{self.name} normal attack hit!')
            return self.ATK
        else:
            print(f'{self.name} normal attack missed!')
            return 0
    
    def take_damage(self, enemy_damage):
        self.HP -= (enemy_damage - self.DEF)
        print(f'{self.name} HP: {self.HP}')
    
    def use_potion(self):
        print(f'Inventory: {self.INVENTORY}')
        hp_or_mana = input("Which potion would you like to use? (HP or MANA)")
        if hp_or_mana.upper() == 'HP':
            if len(self.INVENTORY['HP Potion']) == 0:
                print("Sorry, there are no health potions available.")
                print(f"{self.name} does nothing.")
            else:
                print(f'{self.name} uses a health potion to restore 20 health!')
                self.HP += 20
                self.INVENTORY['HP Potion'].remove('health potion')
                print(f'{self.name} HP: {self.HP}')
        elif hp_or_mana.upper() == 'MANA':
            if len(self.INVENTORY['Mana Potion']) == 0:
                print("Sorry, there are no health potions available.")
                print(f"{self.name} does nothing.")
            else:
                print(f'{self.name} uses a health potion to restore 50 mana!')
                self.MANA += 50
                self.INVENTORY['Mana Potion'].remove('mana potion')
                print(f'{self.name} Mana: {self.MANA}')
        else:
            print(f"Sorry, invalid input. {self.name} does nothing.")

class Swordmaster(Hero):
    def __init__(self):
        super().__init__()
        self.SPATK = random.randint(14, 16)
        self.SPD = random.randint(3, 5)
        self.DODGE = 50

    def mana_katti(self):
        pass

    def sol_katti(self):
        pass

    def rune_blade(self):
        pass

class Lord(Hero):
    def __init__(self):
        super().__init__()
        self.ATK = random.randint(18, 20)
        self.SPATK = random.randint(20, 25)
        self.SPD = 0
    
    def rapier(self):
        pass

    def durandal(self):
        pass

    def rex_hasta(self):
        pass

class Axe_Lord(Hero):
    def __init__(self):
        super().__init__()
        self.ATK = random.randint(20, 22)
        self.SPATK = random.randint(20, 22)
        self.SPD = 2

    def wolf_beil(self):
        pass

    def basilikos(self):
        pass

    def armads(self):
        pass




if __name__ == '__main__':
    my_hero = Hero()
    print(my_hero)
    
    # Test hero class
    while True:
        print('\nMain Menu')
        print('1. Display Stats')
        print('2. Normal Attack')
        print('3. Take Damage')
        print('4. Use Potion')
        print('5. End code')

        user_choice = input("Choose an option: ")
        print("")
        if user_choice == '1':
            my_hero.display_stats()
        elif user_choice == '2':
            my_hero.normal_attack()
        elif user_choice == '3':
            while True:
                try:
                    damage = int(input('How much damage should your hero take?'))
                except ValueError:
                    print("Sorry, whole numbers only.")
                else:
                    my_hero.take_damage(damage)
                    break
        elif user_choice == '4':
            my_hero.use_potion()
        elif user_choice == '5':
            print("Ending code. Thanks for playing!")
            break
