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
        self.DEF = 7
        self.DODGE = 30
        self.durability = {'Mana Katti': 10, 'Sol Katti': 5, 'Rune Blade': 3}

    def special_attack_1(self):
        if self.durability['Mana Katti'] > 0:
            return self.check_attack('Mana Katti', 95, 70, 2)
        else:
            print('Mana Katti is broken...')
            print(f'{self.name} does a basic attack!')
            return super().normal_attack()

    def special_attack_2(self):
        if self.durability['Sol Katti'] > 0:
            return self.check_attack('Sol Katti', 90, 80, 4)
        else:
            print('Sol Katti is broken...')
            print(f'{self.name} does a basic attack!')
            return super().normal_attack()

    def special_attack_3(self):
        if self.durability['Rune Blade'] > 0:
            return self.check_attack('Rune Blade', 80, 10, 1)
        else:
            print('Rune Blade is broken...')
            print(f'{self.name} does a basic attack!')
            return super().normal_attack()
    
    def check_attack(self, weapon, hit, crit_chance, modifier):
        chance = random.randint(0, 101)
        if chance <= hit and chance <= crit_chance:
            print(f'{self.name} crit with {weapon}!')
            self.durability[weapon] -= 1
            return (self.SPATK + modifier) * 2
        elif chance <= hit:
            print(f'{self.name} hit with {weapon}!')
            self.durability[weapon] -= 1
            return self.SPATK + modifier
        else:
            print(f'{self.name} missed with {weapon}...')
            return 0

    def take_damage(self, enemy_damage):
        if random.randint(0, 101) <= self.DODGE:
            print(f'{self.name} dodged the attack!')
        else:
            self.HP -= (enemy_damage - self.DEF)
            print(f'{self.name} HP: {self.HP}')

class Lord(Hero):
    def __init__(self):
        super().__init__()
        self.durability = {'Rapier': 15, 'Durandal': 5, 'Rex Hasta': 5}
        self.ATK = random.randint(18, 20)
        self.SPATK = random.randint(20, 25)
        self.DEF = 10
    
    def special_attack_1(self):
        if self.durability['Rapier'] > 0:
            return self.check_attack('Rapier', 90, 30, 0)
        else:
            print('Rapier is broken...')
            print(f'{self.name} does a basic attack!')
            return super().normal_attack()
        
    def special_attack_2(self):
        if self.durability['Durandal'] > 0:
            return self.check_attack('Durandal', 75, 15, 5)
        else:
            print('Durandal is broken...')
            print(f'{self.name} does a basic attack!')
            return super().normal_attack()

    def special_attack_3(self):
        if self.durability['Rex Hasta'] > 0:
            return self.check_attack('Rex Hasta', 75, 5, 10)
        else:
            print('Rex Hasta is broken...')
            print(f'{self.name} does a basic attack!')
            return super().normal_attack()

    def check_attack(self, weapon, hit, crit_chance, modifier):
        chance = random.randint(0, 101)
        if chance <= hit and chance <= crit_chance:
            print(f'{self.name} crit with {weapon}!')
            self.durability[weapon] -= 1
            return (self.SPATK + modifier) * 2
        elif chance <= hit:
            print(f'{self.name} hit with {weapon}!')
            self.durability[weapon] -= 1
            return self.SPATK + modifier
        else:
            print(f'{self.name} missed with {weapon}...')
            return 0

class Axe_Lord(Hero):
    def __init__(self):
        super().__init__()
        self.durability = {'Wolf Beil': 15, 'Basilikos': 5, 'Armads': 5}
        self.ATK = random.randint(20, 22)
        self.SPATK = random.randint(20, 22)
        self.DEF = 15

    def special_attack_1(self):
        if self.durability['Wolf Beil'] > 0:
            return self.check_attack('Wolf Beil', 70, 10, 0)
        else:
            print('Wolf Beil is broken...')
            print(f'{self.name} does a basic attack!')
            return super().normal_attack()

    def special_attack_2(self):
        if self.durability['Basilikos'] > 0:
            return self.check_attack('Basilikos', 60, 10, 10)
        else:
            print('Basilikos is broken...')
            print(f'{self.name} does a basic attack!')
            return super().normal_attack()

    def special_attack_3(self):
        if self.durability['Armads'] > 0:
            return self.check_attack('Armads', 50, 10, 20)
        else:
            print('Armads is broken...')
            print(f'{self.name} does a basic attack!')
            return super().normal_attack()

    def check_attack(self, weapon, hit, crit_chance, modifier):
        chance = random.randint(0, 101)
        if chance <= hit and chance <= crit_chance:
            print(f'{self.name} crit with {weapon}!')
            self.durability[weapon] -= 1
            return (self.SPATK + modifier) * 2
        elif chance <= hit:
            print(f'{self.name} hit with {weapon}!')
            self.durability[weapon] -= 1
            return self.SPATK + modifier
        else:
            print(f'{self.name} missed with {weapon}...')
            return 0


if __name__ == '__main__':
    my_hero = Axe_Lord()
    print(my_hero)
    
    # Test hero class
    while True:
        print('\nMain Menu')
        print('1. Display Stats')
        print('2. Normal Attack')
        print('3. Take Damage')
        print('4. Use Potion')
        print('5. Wolf Beil')
        print('6. Basilikos')
        print('7. Armads')
        print('8. End code')

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
            print(my_hero.wolf_beil())
        elif user_choice == '6':
            print(my_hero.basilikos())
        elif user_choice == '7':
            print(my_hero.armads())
        elif user_choice == '8':
            print("Ending code. Thanks for playing!")
            break
