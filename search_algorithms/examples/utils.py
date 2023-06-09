class Node:
    def __init__(self, state, parent = None, g = 0, h = 0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

class Problem:
    def __init__(self, initial_state: Node, goal_nodes: list, actions: dict, heuristic = None, transition = None):
        self.initial_state = initial_state
        self.goal_nodes = goal_nodes
        self.actions = actions
        self.heuristic = heuristic
        self.__transition = transition
        self.__solution = []
        

    def result(self, parent_state, action) -> str:
        if(not self.__transition):
            return action
        return self.__transition(parent_state, action)

    def goal_test(self, state: any) -> bool:
        if (state in [goal_node.state for goal_node in self.goal_nodes]):
            return True
        return False
    
    def solution(self, node: Node) -> list:
        self.__solution.append(node.state)
        if (node.parent):
            self.solution(node.parent)
        return self.__solution