class Node:
    def __init__(self, state, parent = None, g = 0, h = 0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

class Problem:
    def __init__(self, initial_state: Node, goal_state: Node, actions: dict, func = None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions
        self.__solution = []
        self.__func = func

    def result(self, parent_state, action) -> Node:
        if(not self.__func):
            return action
        return self.__func(parent_state, action)

    def goal_test(self, state: any) -> bool:
        if (state == self.goal_state.state):
            return True
        return False
    
    def solution(self, node: Node) -> list:
        self.__solution.append(node.state)
        if (node.parent):
            self.solution(node.parent)
        return self.__solution