from utils import Problem

class HillClimbing:
    def __init__(self, problem: Problem):
        self.problem = problem
        self.states = [(problem.initial_state.state, problem.initial_state.value)]

    def search(self) -> int:
        current = self.problem.initial_state
        while True:
            neighbor = self.problem.next_state(current)
            if neighbor.value >= current.value:
                return self.states
            current = neighbor
            self.states.append((current.state, current.value))
            