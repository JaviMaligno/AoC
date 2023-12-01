#import cvxpy as cp
import numpy as np
import re
import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
text = get_input(16)

def graph(text):
    valves = {}
    for x in map(lambda x: x.split('; '), text.splitlines()):
        valve = re.search('[A-Z][A-Z]', x[0]).group()
        rate = int(re.search('\d+', x[0]).group())
        neighbors = re.search('([A-Z][A-Z](, )?)+', x[1]).group().split(', ')
        valves[valve] = {'rate': rate, 'neighbors': neighbors, 'state': 1} #1 means closed
    return valves
print(len(graph(text)))
# I have a recursive model and an integer programming model. 
def letter_to_number(valves):
    keys = valves.keys()
    equivalence = dict(zip(keys, range(len(keys))))
    numerical_valves = {}
    for k in keys:
        numerical_valves[equivalence[k]]=[equivalence[neighbor] for neighbor in valves[k]['neighbors']]
    return numerical_valves

    
# INTEGER PROGRAMMING

# GEKKO
from gekko import GEKKO

m = GEKKO()

def solver(numerical_valves, steps = 30):
    size = len(numerical_valves)
    time = range(steps)
    x = m.Array(m.Var, (size,size, steps), value = 0, integer = True, lb=0, up=1)
    for k in time:
        m.Equation(np.sum(x[:,:,k]) == 1)
    for i in range(size):
        m.Equation(m.sum(x[i,i,:]) <= 1)
    #PEREZA


x = m.Array(m.Var,(10,10,30), value = 0, integer = True, lb = 0, ub = 1)
print(x[1,1,:])
# CVXPY MAKES IT TOO DIFFICULT BECAUSE IT DOESN'T TAKE 3D ARRAYS MAY CONSIDER IT LATER ANYWAY
""" def solver(numerical_valves, steps = 30):
    size = len(numerical_valves)
    time = range(steps)
    variables = {} #maybe use a np.array instead
    constraints = []
    #cvxpy does not support 3d arrays, I will try to do it by defining an array of variables for each time
   
    for t in time:
        variables[t] = cp.Variable((size, size), boolean = True)
        constraints += [cp.sum(variables[t])  == 1]
        for i in range(size):
            constraints += [cp.sum(variables[t][i,i]) <=1 for t in time]
            for j in range(i+1,size):
                if j not in numerical_valves[i]:
                    constraints += [variables[t][i,j] == 0, variables[t][j,i] ==0]

    # still need the costs and its constraints 
    expression = cp.sum(cp.trace(variables[t])*(30-t) for t in time) # I can do this in a loop if necessary https://stackoverflow.com/questions/53839771/how-to-tell-cvxpy-how-to-sum-over-values-of-a-matrix-in-an-objective-function
    obj = cp.Maximize(expression,constraints)

x= cp.Variable((10,10), boolean = True)

print(x) """
# RECURSIVE MODEL
# At the moment it is failing because the rate keeps increasing and it should be topped at the sum of rates
# I'll try to find the error later
def recursive_flow(valves, time = 30, initial_flow = 0, initial_rate = 0, initial_valve = 'AA', open = []):
    current_flow = initial_flow
    current_valve = initial_valve
    current_rate = initial_rate
    iter_valves = valves.copy()
    if time == 0:
        return current_flow, valves
    elif time == 1:
        closed = valves[current_valve]['state'] #if it is closed, we open it
        rate = valves[current_valve]['rate']
        current_rate = current_rate + rate if closed else current_rate
        current_flow = current_flow + current_rate 
        iter_valves[current_valve]['state'] = 0
        return current_flow, iter_valves
    else:
        closed = valves[current_valve]['state']
        rate = valves[current_valve]['rate']
        if rate == 0:
            iter_valves[current_valve]['state'] = 0
            for neighbor in valves[current_valve]['neighbors']:
                return recursive_flow(iter_valves, time = time-1,initial_flow=current_flow+current_rate, initial_rate = current_rate, initial_valve=neighbor)    
        if closed:
            potential_rate = current_rate+rate
            # if it is closed we can either open it or leave it closed
            # if we open it, we gain the rate for this moment and the next one, in which we will be in a neighbor
            next_flow = []
            open_valves = iter_valves.copy()
            open_valves[current_valve]['state'] = 0
            for neighbor in valves[current_valve]['neighbors']:
                open_flow =  recursive_flow(open_valves, time = time-2, initial_flow=current_flow+potential_rate, initial_rate = potential_rate, initial_valve=neighbor, open = current_valve)
                closed_flow = recursive_flow(iter_valves, time = time-1,initial_flow=current_flow+current_rate, initial_rate = current_rate, initial_valve=neighbor)
                if open_flow >= closed_flow:
                    next_flow.append(open_flow)
                else:
                    next_flow.append(closed_flow)

                #next_flow.append((rate + recursive_flow(valves, time = time-2, initial_flow=current_flow+2*potential_rate, initial_rate = potential_rate, initial_valve=neighbor), neighbor))
                #next_flow.append((recursive_flow(valves, time = time-1,initial_flow=current_flow+current_rate, initial_rate = current_rate, initial_valve=neighbor),neighbor))
            
            max_flow = max(next_flow)
            current_flow += max_flow[0]
            iter_valves = max_flow[1]
            #iter_valves[current_valve]['state'] = max_flow[2]
            #current_valve = max_flow[1]
            return current_flow, iter_valves

        else:
            max_flow = max(recursive_flow(iter_valves, time = time-1,initial_flow=current_flow+current_rate, initial_rate = current_rate, initial_valve=neighbor) for neighbor in valves[current_valve]['neighbors'])
            current_flow += max_flow[0]
            iter_valves= max_flow[1]
            return current_flow, iter_valves








#print(graph(text))