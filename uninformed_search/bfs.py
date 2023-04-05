class Node:
    def __init__(self, state: any):
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



def BFS(problem: Problem) -> bool:
    node: Node = problem.initial_state
    frontier: list = [node]
    explored: list = []
    if(problem.goal_test(node)):
        return True
    while(True):
        if(len(frontier)==0):
            return False
        node = frontier.pop(0)
        explored.append(node.state)
        for action in problem.actions[node.state]:
            child: Node = Node(action)
            if (child.state not in explored and child.state not in frontier):
                if (problem.goal_test(child.state)):
                    return True
                frontier.append(child)

if __name__ == '__main__':
    actions = {'A':['B'], 'B': ['A','C','D'], 'C': ['B','E'], 'D': ['B','E'], 'E':['C','D']}
    initial_state = Node('A')
    goal_state = Node('E')
    problem = Problem(initial_state, goal_state, actions)
    BFS(problem)
