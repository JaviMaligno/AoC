import sympy as sp
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(21)

def parsed_dict(text, symbolic = True):
    dictionary = dict(list(map(lambda x: tuple(x.split(': ')),text.splitlines())))
    if symbolic:
        dictionary['root']=dictionary['root'].replace('+','=')
        dictionary['humn'] = 'x'
    return dictionary

def operate(x,y,op):
    pass


def operation(dictionary, starting_node = 'root'):
    value = dictionary[starting_node]
    if value.isnumeric():
        return int(value)
    else:
        terms = value.split(' ')
        if terms[1] == "=":
            x = operation(dictionary,starting_node = terms[0])
            op = terms[1]
            y = operation(dictionary,starting_node = terms[2])
            result = eval("x"+op+"y", {"x":x, "y":y})
            return result

def symbolic_operation(dictionary, starting_node = 'root'):
    value = dictionary[starting_node]
    if value.isnumeric() or value == 'x':
        return value
    else:
        terms = value.split(' ')
        x = symbolic_operation(dictionary,starting_node = terms[0])
        y = symbolic_operation(dictionary,starting_node = terms[2])
        if terms[1] == "=":
            expr = x + ' - ' + y
            solution = sp.solve(expr)
            return solution
        else:
            op = terms[1]
            expression = '(' + x + op + y + ')'
            return expression

dictionary = parsed_dict(text)

print(symbolic_operation(dictionary))