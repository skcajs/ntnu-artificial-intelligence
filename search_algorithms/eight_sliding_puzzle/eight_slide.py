from itertools import permutations
from a_star_search import AStarSearch
from utils import Problem, Node
import numpy as np
import random

def generate_board(keys, n = 1000):
    state = '123456780'
    for _ in range(n):
        empty_index = state.index('0')
        action = random.choice(keys[empty_index])
        state = result(state, action[0])
    return state



def result(state, action):
    state_list = list(state)
    a, b = state_list.index('0'), action
    state_list[b], state_list[a] = state_list[a], state_list[b]
    return ''.join(state_list)
    
actions = {}
cost = 1
keys = {
    0: [[1, cost], [3, cost]], 
    1: [[2, cost],[4, cost],[0, cost]], 
    2: [[5, cost],[1, cost]], 
    3: [[0, cost],[4, cost],[6, cost]], 
    4: [[1, cost],[5, cost],[7, cost],[3, cost]], 
    5: [[2, cost],[8, cost],[4, cost]], 
    6: [[3, cost],[7, cost]], 
    7: [[4, cost],[8, cost],[6, cost]], 
    8: [[5, cost],[7, cost]]}

for perm in [''.join(map(str, p)) for p in permutations(range(9))]:
    actions[perm] = keys[perm.index('0')]
        

def heuristic(s: str):
    goal = list('123456780')
    state = list(s)
    total = 0
    for i in range(9):
        # Manhatton Distance
        goal_column = goal.index(str(i))%3
        state_column = state.index(str(i))%3
        goal_row = int(goal.index(str(i))/3%3)
        state_row = int(state.index(str(i))/3%3)
        total += abs(goal_column-state_column)
        total += abs(goal_row-state_row)
        # # Humming Distance
        # if (goal.index(str(i)) != state.index(str(i))):
        #     total += 1
    return total

def play():
    puzzle = generate_board(keys)
    initial_state = Node(puzzle)
    # initial_state = Node('615732048')
    goal_nodes = [Node('123456780')]

    problem = Problem(initial_state=initial_state, goal_nodes=goal_nodes, actions=actions, heuristic=heuristic, transition=result)
    ast = AStarSearch(problem)

    return ast.search()


board = play()

board.reverse()

boardpy = []

for b in board:
    bpy = np.array(list(b))
    m = bpy.reshape(3,3)
    boardpy.append(m)

for bpy in boardpy:
    print(bpy)
