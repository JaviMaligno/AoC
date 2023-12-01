from C1 import *
with open(r"AoC2023\Day1\test.txt") as f1, open(r"AoC2023\Day1\test2.txt") as f2: 
    text1 = f1.read()
    text2 = f2.read()
    test1 = sum_two_digit_numbers(text1)
    test2 = sum_two_digit_numbers(text2)
    print(test1, test2)
    #print(sum_two_digit_numbers("eightwothree"))
