from utils import Problem, Node

def DFS(problem: Problem) -> list:
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
            child: Node = Node(action, node)
            if (child.state not in explored and child.state not in [f.state for f in frontier]):
                if (problem.goal_test(child.state)):
                    return problem.get_solution(child)
                frontier.append(child)