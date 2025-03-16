import re

with open('blackjack.csv', 'r') as data:
    card_totals = []
    labels = []    
    for line in data:
        card_totals.append(line)

