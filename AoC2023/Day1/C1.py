import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(r"AoC2023")
from get_data import get_input
text = get_input(1)
""" 
version 1
def sum_two_digit_numbers(text):
    lst = text.splitlines()
    total = 0
    for s in lst:
        # Find the first and last digit in the string
        digits = [char for char in s if char.isdigit()]
        #if len(digits) >= 2:
        two_digit_num = int(digits[0] + digits[-1])
        # Add the two-digit number to the total
        total += two_digit_num
    return total """

def sum_two_digit_numbers(text):
    lst = text.splitlines()
    total = 0
    digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digit_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for s in lst:
        # Find the first digit
        first_digit = None
        i = 0
        while i < len(s) and first_digit is None:
            if s[i].isdigit():
                first_digit = s[i]
                break
            else:
                for word, digit in zip(digit_words, digit_values):
                    if s[i:].startswith(word):
                        first_digit = digit
                        i += len(word)
                        break
                else:
                    i += 1
       
        # Find the last digit
        last_digit = None
        s_reversed = s[::-1]
        i = 0
        while i < len(s_reversed) and last_digit is None:
            if s_reversed[i].isdigit():
                last_digit = s_reversed[i]
                break
            else:
                for word, digit in zip(digit_words, digit_values):
                    if s_reversed[i:].startswith(word[::-1]):
                        last_digit = digit
                        i += len(word)
                        break
                else:
                    i += 1
        print(first_digit,last_digit)
        # Add the two-digit number to the total
        if first_digit is not None and last_digit is not None:
            two_digit_num = int(first_digit + last_digit)
            total += two_digit_num

    return total




print(sum_two_digit_numbers(text))