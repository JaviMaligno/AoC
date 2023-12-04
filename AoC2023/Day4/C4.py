import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(4)

def calculate_points(text):
    cards = text.splitlines()
    total_points = 0
    for card in cards:
        # Remove the "Card (card number): " prefix
        card = card.split(": ")[1]
        # Split the card into winning numbers and user numbers
        winning_numbers, user_numbers = card.split("|")
        # Convert the numbers from strings to integers
        winning_numbers = list(map(int, winning_numbers.split()))
        user_numbers = list(map(int, user_numbers.split()))
        # Find the matches and calculate the points
        matches = set(winning_numbers).intersection(set(user_numbers))
        points = 2**(len(matches) - 1) if matches else 0
        total_points += points
    return total_points

def count_matches(input_string):
    # Split the input string into lines
    lines = input_string.splitlines()

    # Initialize an empty list to hold the cards
    cards = []

    # Process each line
    for line in lines:
        # Split the line into card number, winning numbers, and user numbers
        _, numbers = line.split(':')
        winning_numbers, user_numbers = numbers.split('|')

        # Convert the numbers from strings to integers and add them to the cards list
        cards.append((list(map(int, winning_numbers.split())), list(map(int, user_numbers.split()))))

    # Initialize a list to hold the number of copies of each card
    copies = [1] * len(cards)

    # Process each card
    for i in range(len(cards)):
        # Count the number of matches between the winning numbers and the user numbers
        matches = len(set(cards[i][0]) & set(cards[i][1]))

        # Add copies to the subsequent cards for each match
        for j in range(i+1, min(i+1+matches, len(cards))):
            copies[j] += copies[i]

    # Return the total number of cards
    return sum(copies)


print(count_matches(text))

