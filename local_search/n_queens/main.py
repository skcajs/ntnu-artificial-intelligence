from n_queens import create_board, successors, heuristic
from utils import Problem, Node
from hill_climbing import HillClimbing

if __name__ == "__main__":
    initial_state = create_board(8)
    problem = Problem(initial_state=initial_state, f_heuristic=heuristic, f_successors=successors)
    hc = HillClimbing(problem)
    print(hc.search())
