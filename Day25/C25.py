from collections import defaultdict
from gmpy2 import digits
from math import log
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(25).splitlines()

def to_decimal(snafu):
    power = len(snafu)
    powers = [5**n for n in range(power)][::-1]
    decimal = 0
    for x,y in zip(snafu, powers):
        if x == "-":
            decimal -= y
        elif x == '=':
            decimal -= 2*y
        else:
            decimal += int(x)*y
    return decimal

    
def to_snafu(decimal):
    snafu = ""
    base_5 = list(map(int,digits(decimal, 5)[::-1]))
    positions = range(len(base_5))
    position_digit = defaultdict(int)
    for i in positions:
        position_digit[i] = base_5[i]

    for i, d in position_digit.items():
        if d == 5:
            position_digit[i] = 0
            position_digit[i+1] += 1
        elif d == 4:
            position_digit[i] = "-"
            position_digit[i+1] += 1
        elif d == 3:
            position_digit[i] = "="
            position_digit[i+1] += 1
        snafu += str(position_digit[i])
    snafu = snafu[::-1]
    return snafu
    


    """ snafu = ""
    power_below = int(log(decimal, 5))
    power_above = power_below + 1
    while decimal:
        while power_below > decimal:
            power_below -= 1
        power_above = power_above+1
        if decimal > 0:      
            # powers of are odd so their difference is even, which means there can't be a number just in between
            below_closer = decimal - power_below < power_above - decimal 
            if below_closer:
                pass
            else:
                snafu+= str(power_above)
                decimal -= power_above
                power_above -= 1
                power_below -= 1
        else:

 """

    

def supply(text):
    fuel = 0
    for snafu in text:
        fuel += to_decimal(snafu)
    return to_snafu(fuel)

#print(supply(text))

