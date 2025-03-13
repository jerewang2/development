import random

print("Welcome to Jackpot!")
print("Today you will be playing a lottery. Choose 5 random numbers and 1 bonus number to win a cash prize!")
print("Choose 5 numbers from 0 - 50 for your drawing:")

winning_nums = random.sample(range(0, 51), 5)

winning_bonus = random.randint(0, 10)

user_nums = []
correct_nums = 0

# print(winning_nums, winning_bonus)

for i in range(5):
    choice = int(input(f"User number {i + 1}: "))
    user_nums.append(choice)

user_bonus = int(input("Choose a number from 0 - 10: "))

for num in user_nums:
    if num in winning_nums:
        correct_nums += 1

print(f"You got {correct_nums} correct numbers.")

if user_bonus == winning_bonus:
    print("You also got the bonus number!")
    print(f'Your total winnings is ${(correct_nums * 10) + 20}.')
else:
    print("Unfortunately, you did not get the bonus.")
    print(f'Your total winnings is ${(correct_nums * 10)}.')

print('Thank you for playing!')