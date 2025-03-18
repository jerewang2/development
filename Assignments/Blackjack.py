import re
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore")

class Blackjack:
    def __init__(self):
        self.deck = {}
        self.ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['\u2663', '\u2665', '\u2666', '\u2660']
        self.parameters = []
        self.card_totals = []
        self.labels = []
        self.players = {}

        self.retrieve_and_process()

        for rank in self.ranks:
            for suit in self.suits:
                self.deck[rank + suit] = int(self.parameters[2])

        
        
        self.run()

    def draw_card(self):
        while True:
            rand_rank = random.choice(self.ranks)
            rand_suit = random.choice(self.suits)
            if self.deck[rand_rank + rand_suit] > 0:
                self.deck[rand_rank + rand_suit] -= 1
                return rand_rank + rand_suit
    
    def setup(self):
        for i in range(int(self.parameters[1]) + 1):
            self.players[i + 1] = []
        
        for i in range(2):
            for j in range(int(self.parameters[1]) + 1):    
                self.players[j + 1].append(self.draw_card())

    def retrieve_and_process(self):
        with open('Assignments/blackjack_parameters.txt', 'r') as text:
            pattern = r'\= (.*)'
            
            for line in text:
                found = re.search(pattern, line)
                if found:
                    self.parameters.append(found.group()[2:])
                else:
                    print("NO match found.")

        with open('Assignments/blackjack.csv', 'r') as data:
            num_pattern = r'\d+'
            success_pattern = r'success'
            miss_pattern = r'miss'

            for line in data:
                num_found = re.search(num_pattern, line)
                success_found = re.search(success_pattern, line)
                miss_found = re.search(miss_pattern, line)
                if num_found:
                    self.card_totals.append(int(num_found.group()))
                if success_found:
                    self.labels.append(success_found.group())
                if miss_found:
                    self.labels.append(miss_found.group())

    def plot_raw_data(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.card_totals, self.labels, 'o', color='blue', alpha=0.6)
        plt.xlabel('Card Totals')
        plt.ylabel('Outcome')
        plt.title('Plot of Success vs. Miss')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    def machine_learning(self, card_value):
        dataframe = pd.read_csv('Assignments/blackjack.csv')
        X = dataframe[['Player_Total']]
        y = dataframe['Label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Run Logistic Regression
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # Predicting the Test set results
        y_pred = model.predict(X_test)

        # Return Prediction
        return model.predict([[card_value]])
        
    def calculate_hand_value(self, cards):
        total = 0
        for card in cards:
            if card[:-1] == 'A':
                total += 1
            elif card[:-1] == '10' or card[:-1] == 'J' or card[:-1] == 'Q' or card[:-1] == 'K':
                total += 10
            else:
                total += int(card[:-1])
        return total

    def play_game(self):
        for player, hand in self.players.items():
            if int(player) == int(self.parameters[1]) + 1:
                # This is the dealer
                pass
            else:
                print(f'Player {player} here is your hand: {hand}')
                card_total = self.calculate_hand_value(hand)
                print(f'Card total: {card_total}')

                # Machine Learning
                if self.machine_learning(card_total)[0] == 'success':
                    print('AI suggests you can hit!')
                else:
                    print('AI suggests you stay.')

                decision = input("Would you like to hit or pass? ")

    def run(self):
        # self.plot_raw_data()
        self.setup()
        print(self.players)
        self.play_game()
        # card = 16
        # print(f'Machine Learning Prediction for card value {card}: {self.machine_learning(card)}')

if __name__ == '__main__':
    game = Blackjack()