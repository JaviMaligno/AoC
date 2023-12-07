import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(7)

def process_input(input_text):
    lines = input_text.strip().split('\n')
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append((hand, int(bid)))
    return hands

def calculate_winnings(hands):
    card_order = '23456789TJQKA'
    hand_order = ['High card', 'One pair', 'Two pair', 'Three of a kind', 'Full house', 'Four of a kind', 'Five of a kind']

    def hand_rank(hand):
        counts = {card: hand.count(card) for card in set(hand)}
        counts = sorted(counts.items(), key=lambda x: (-x[1], -card_order.index(x[0])))
        if len(counts) == 5:
            return ('High card', counts)
        elif len(counts) == 4:
            return ('One pair', counts)
        elif len(counts) == 3:
            if counts[0][1] == 2:
                return ('Two pair', counts)
            else:
                return ('Three of a kind', counts)
        elif len(counts) == 2:
            if counts[0][1] == 3:
                return ('Full house', counts)
            else:
                return ('Four of a kind', counts)
        else:
            return ('Five of a kind', counts)

    hands = sorted(hands, key=lambda x: (hand_order.index(hand_rank(x[0])[0]), hand_rank(x[0])[1]))
    total_winnings = sum(bid * (rank + 1) for rank, (hand, bid) in enumerate(hands))
    return hands, total_winnings


hands = process_input(text)
#print(hands)  # Output: [('32T3K', 765), ('T55J5', 684), ('KK677', 28), ('KTJJT', 220), ('QQQJA', 483)]
#hands = [('32T3K', 765), ('T55J5', 684), ('KK677', 28), ('KTJJT', 220), ('QQQJA', 483)]
print(calculate_winnings(hands))  # Output: 6440
