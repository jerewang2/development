import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

class Blackjack:
    def __init__(self):
        self.deck = {}
        self.ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['\u2663', '\u2665', '\u2666', '\u2660']
        self.parameters = []
        self.card_totals = []
        self.labels = []

        self.retrieve_and_process()

        for rank in self.ranks:
            for suit in self.suits:
                self.deck[rank + suit] = self.parameters[2]
        
        self.run()

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
        
    def run(self):
        # self.plot_raw_data()
        card = 16
        print(f'Machine Learning Prediction for card value {card}: {self.machine_learning(card)}')

if __name__ == '__main__':
    game = Blackjack()