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