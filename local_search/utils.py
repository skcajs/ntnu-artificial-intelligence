class Node:
    def __init__(self, state, value = 0):
        self.state = state
        self.value = value

class Problem:
    def __init__(self, initial_state: int, f_heuristic = None, f_successors = None):
        self.heuristic = f_heuristic
        self.successors = f_successors
        self.initial_state = Node(state = initial_state, value=self.__value(initial_state))

    
    def next_state(self, current: Node) -> Node:
        successors = {n: self.heuristic(n) for n in self.successors(current) }
        successor = max(successors, key=successors.get)
        return Node(state=successor, value=successors[successor])

    def __value(self, state) -> int:
        return self.heuristic(state)