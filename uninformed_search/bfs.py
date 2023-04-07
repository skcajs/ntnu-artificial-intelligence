from utils import Problem, Node
from itertools import permutations

def BFS(problem: Problem) -> list:
    node: Node = problem.initial_state
    frontier: list = [node]
    explored: list = []
    if(problem.goal_test(node)):
        return node.state
    while(True):
        if(len(frontier)==0):
            return []
        node = frontier.pop(0)
        explored.append(node.state)
        for action in problem.actions[node.state]:
            child: Node = Node(problem.result(node.state, action), node)
            if (child.state not in explored and child.state not in [f.state for f in frontier]):
                if (problem.goal_test(child.state)):
                    return problem.solution(child)
                frontier.append(child)


if __name__ == '__main__':

    def result(state, action):
        state_list = list(state)
        a, b = state_list.index('0'), action
        state_list[b], state_list[a] = state_list[a], state_list[b]
        return ''.join(state_list)
    
    actions = {}
    keys = {0: [1, 3], 1: [2,4,0], 2: [5,1], 3: [0,4], 4: [1,5,3], 5: [2,4]}

    for perm in [''.join(map(str, p)) for p in permutations(range(6))]:
        actions[perm] = keys[perm.index('0')]
            
    initial_state = Node('120345')
    goal_state = Node('123450')
    problem = Problem(initial_state, goal_state, actions, result)
    
    print(BFS(problem))