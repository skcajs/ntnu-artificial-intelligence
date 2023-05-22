from a_star_search import AStarSearch
from greedy_best_first_search import GBFS
from uniform_cost_search import UniformCostSearch

from utils import Problem, Node


if __name__ == "__main__":
    actions = {
        'S': [['A', 5], ['B', 9], ['D', 6]], 
        'A': [['G1', 9], ['B', 3]],
        'B': [['A', 2], ['C', 1]], 
        'C': [['S', 6], ['G2', 5], ['F', 7]], 
        'D': [['S', 1], ['C', 2], ['E', 2]], 
        'E': [['G3', 4]], 
        'F': [['D', 2], ['G3', 8]],
        'G1': [],
        'G2': [],
        'G3': []
    }
    def heuristic(s: str):
        return {
            'S': 5, 
            'A': 7,
            'B': 3, 
            'C': 4, 
            'D': 6, 
            'E': 5, 
            'F': 6,
            'G1': 0,
            'G2': 0,
            'G3': 0    
        }[s]
   
    initial_state = Node('S', h=heuristic('S'))
    goal_nodes = [Node('G1'), Node('G2'), Node('G3')]

    ast_problem = Problem(initial_state=initial_state, goal_nodes=goal_nodes, actions=actions, heuristic=heuristic)
    ast = AStarSearch(ast_problem)

    ucs_problem = Problem(initial_state, goal_nodes, actions)
    ucs = UniformCostSearch(ucs_problem)

    gbfs_problem = Problem(initial_state=initial_state, goal_nodes=goal_nodes, heuristic=heuristic, actions=actions)
    gbfs = GBFS(gbfs_problem)

    print('Uniform Cost', ucs.search())
    print('Greedy Best First', gbfs.search())
    print('A* Search', ast.search())