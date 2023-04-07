class Node:
    def __init__(self, state: any, parent = None):
        self.state = state
        self.parent = parent


class Problem:
    def __init__(self, initial_state: Node, goal_state: Node, actions: dict):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions
        self.solution = []

    def goal_test(self, state: any) -> bool:
        if (state == self.goal_state.state):
            return True
        return False
    
    def get_solution(self, node: Node) -> list:
        self.solution.append(node.state)
        if (node.parent):
            self.get_solution(node.parent)
        return self.solution


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
            child: Node = Node(action, node)
            if (child.state not in explored and child.state not in [f.state for f in frontier]):
                if (problem.goal_test(child.state)):
                    return problem.get_solution(child)
                frontier.append(child)

if __name__ == '__main__':
    actions = {'A':['B', 'E'], 'B': ['C','A'], 'C': ['D', 'H', 'E', 'B'], 'D': ['C','J'], 'E':['A', 'C', 'F'], 'F': ['E', 'G'], 'G': ['F', 'H', 'I'], 'H': ['C', 'J', 'I', 'G'], 'J': ['D', 'H', 'I']}
    initial_state = Node('A')
    goal_state = Node('I')
    problem = Problem(initial_state, goal_state, actions)
    print(BFS(problem))