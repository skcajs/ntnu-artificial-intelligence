from utils import Problem
import math

class HillClimbing:
    def __init__(self, problem: Problem):
        self.problem = problem

    def search(self) -> int:
        current = self.problem.initial_state
        while True:
            neighbor = self.problem.next_state(current.state)
            if neighbor.value <= current.value:
                return current.state
            current = neighbor
            
# if __name__ == "__main__":

#     def heuristic(x: int):
#         return math.sin(x)
    
#     def successors(x: int):
#         return [x+1, x-1]
    

#     problem = Problem(7, f_heuristic=heuristic, f_successors=successors)
    
#     hc = HillClimbing(problem=problem)

#     print(hc.search())

if __name__ == "__main__":

    def heuristic(x: int):
        return x
    
    def successors(x: str):
        rows = x.split(' ')
        states = []
        for j in range(4):
            for row in rows:
                _rows = x.split(' ')
                if(_rows[j] == row):
                    _rows[j] = '....'
                    _rows[j] = _rows[j][:j] + 'X' + _rows[j][j+1:]
                state = f'{_rows[0]} {_rows[1]} {_rows[2]} {_rows[3]}'
                states.append(state)
                
        return states
    
    initial_state = '..X. .X.. .X.. ..X.'
    problem = Problem(initial_state, f_heuristic=heuristic, f_successors=successors)
    
    hc = HillClimbing(problem=problem)

    print(hc.search())