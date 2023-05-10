class State:
    def __init__(self, h = 0):
        self.h = h

class Problem:
    def __init__(self, initial_sate: int, heuristic):
        self.initial_state = initial_sate

        self.heuristic = heuristic
    
    def next_state(self, state) -> int:
        top = state+1
        bottom = state-1
        if (self.value(top) > self.value(bottom)):
            return top
        else:
            return bottom
       

    def value(self, state) -> int:
        return self.heuristic(state)