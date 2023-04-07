import copy

class Node:
    def __init__(self, state: any, action: any = None):
        self.state = copy.deepcopy(state)
        if (action):
            self.action = action
            self.__swap()
        else:
            self.action == copy.deepcopy(state)

    def __swap(self):
        a, b = self.state.index(-1), self.action
        self.state[b], self.state[a] = self.state[a], self.state[b]

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
        for action in problem.actions[node.action]:
            child: Node = Node(node.state, action)
            if (child.state not in explored and child.state not in frontier):
                if (problem.goal_test(child.state)):
                    return True
                frontier.append(child)

if __name__ == '__main__':
    # actions = {0: [1, 3], 1: [2,4,0], 2: [5,1], 3: [0,4,6], 4: [1,5,7,3], 5: [2,8,4], 6: [3,7], 7: [4,8,6], 8: [5,7]}
    # initial_state = Node([1,2,3,4,5,6,7,-1,8], 7)
    # goal_state = Node([1,2,3,4,5,6,7,8,-1], 8)
    actions = {'A':['B'], 'B': ['A','C','D'], 'C': ['B','E'], 'D': ['B','E'], 'E':['C','D']}
    initial_state = Node('A')
    goal_state = Node('E')
    problem = Problem(initial_state, goal_state, actions)
    BFS(problem)
