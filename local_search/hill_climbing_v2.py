from utils import Problem
import math

class HillClimbing:
    def __init__(self, problem: Problem):
        self.problem = problem

    def search(self) -> int:
        current = self.problem.initial_state
        while True:
            neighbor = self.problem.next_state(current)
            if self.problem.value(neighbor) <= self.problem.value(current):
                return current
            current = neighbor
            
if __name__ == "__main__":

    def objective(x: int):
        return math.sin(x)
    
    state = 3
    problem = Problem(state, objective=objective)
    
    hc = HillClimbing(problem=problem)

    print(hc.search())