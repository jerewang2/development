from Hero_Classes import *

class Battle:
    def __init__(self):
        print('Welcome to Battle!')
        print('This is a simulator that will have 2 heroes battle and 1 will emerge victorious!\n')

        self.run()

    def run(self):
        while True:
            print('Player 1, which of the following heroes will you choose?')
            choice_1 = input("Swordmaster\nLord\nAxe Lord\nChoice: ")
            if choice_1 == "Swordmaster":
                player_1 = Swordmaster()
                break
            elif choice_1 == 'Lord':
                player_1 = Lord()
                break
            elif choice_1 == 'Axe Lord':
                player_1 = Axe_Lord()
                break
            else:
                print('Sorry, invalid response.')
        
        while True:
            print('\nPlayer 2, which of the following heroes will you choose?')
            choice_2 = input("Swordmaster\nLord\nAxe Lord\nChoice: ")
            if choice_2 == "Swordmaster":
                player_2 = Swordmaster()
                break
            elif choice_2 == 'Lord':
                player_2 = Lord()
                break
            elif choice_2 == 'Axe Lord':
                player_2 = Axe_Lord()
                break
            else:
                print('Sorry, invalid response.')

        print("\nExcellent, both players have choosen their heroes. Let's start the battle!\n")

        while True:
            print("Player 1, choose an option:")

            while True:
                print('1. Display Stats')
                print('2. Normal Attack')
                print('3. Use Potion')
                print('4. Special Attack 1')
                print('5. Special Attack 2')
                print('6. Special Attack 3')

                user_choice = input("Choose an option: ")
                print("")
                if user_choice == '1':
                    player_1.display_stats()
                elif user_choice == '2':
                    player_2.take_damage(player_1.normal_attack())
                    break
                elif user_choice == '3':
                    player_1.use_potion()
                    break
                elif user_choice == '4':
                    player_2.take_damage(player_1.special_attack_1())
                    break
                elif user_choice == '5':
                    player_2.take_damage(player_1.special_attack_2())
                    break
                elif user_choice == '6':
                    player_2.take_damage(player_1.special_attack_3())
                    break

            if player_2.HP < 0:
                print("Player 1 won the battle!")
                print("Thanks for playing!")
                break

            while True: 
                print('1. Display Stats')
                print('2. Normal Attack')
                print('3. Use Potion')
                print('4. Special Attack 1')
                print('5. Special Attack 2')
                print('6. Special Attack 3')

                user_choice = input("Choose an option: ")
                print("")
                if user_choice == '1':
                    player_2.display_stats()
                elif user_choice == '2':
                    player_1.take_damage(player_2.normal_attack())
                    break
                elif user_choice == '3':
                    player_2.use_potion()
                    break
                elif user_choice == '4':
                    player_1.take_damage(player_2.special_attack_1())
                    break
                elif user_choice == '5':
                    player_1.take_damage(player_2.special_attack_2())
                    break
                elif user_choice == '6':
                    player_1.take_damage(player_2.special_attack_3())
                    break
            
            if player_1.HP < 0:
                print("Player 1 won the battle!")
                print("Thanks for playing!")
                break


if __name__ == '__main__':
    battle = Battle()