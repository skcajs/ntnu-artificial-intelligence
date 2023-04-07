class Node:
    def __init__(self, state):
        self.state = state

class Problem:
    def __init__(self, initial_state: Node, goal_state: Node, actions: dict):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

    def goal_test(self, state: any) -> bool:
        if (state == self.goal_state.state):
            return True
        return False


def DFS(problem: Problem) -> list:
    node: Node = problem.initial_state
    frontier: list = [node.state]
    explored: list = []
    if(problem.goal_test(node)):
        return node.state
    while(True):
        if(len(frontier)==0):
            return []
        node = Node(frontier.pop(0))
        explored.append(node.state)
        for action in problem.actions[node.state]:
            child: Node = Node(action)
            if (child.state not in explored and child.state not in frontier):
                if (problem.goal_test(child.state)):
                    return f"State found: {child.state}\nExplored: {explored}\nFrontier: {frontier}"
                frontier.append(child.state)

if __name__ == '__main__':
    actions = {'A':['B', 'E'], 'B': ['C','A'], 'C': ['D', 'H', 'E', 'B'], 'D': ['C','J'], 'E':['A', 'C', 'F'], 'F': ['E', 'G'], 'G': ['F', 'H', 'I'], 'H': ['C', 'J', 'I', 'G'], 'J': ['D', 'H', 'I']}
    initial_state = Node('A')
    goal_state = Node('I')
    problem = Problem(initial_state, goal_state, actions)
    print(DFS(problem))
