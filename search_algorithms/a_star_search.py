from utils import Problem, Node
from itertools import permutations

class AST:
    def __init__(self, problem: Problem):
        self.problem = problem
    
    def search(self) -> list:
        node = self.problem.initial_state
        frontier = [node]
        explored = []
        while True:
            if(len(frontier) == 0):
                return []
            node = frontier.pop(0)
            if(self.problem.goal_test(node.state)):
                return self.problem.solution(node)
            explored.append(node.state)
            for action in self.problem.actions[node.state]:
                child_state = self.problem.result(node.state, action[0])
                child = Node(child_state, node, g=action[1] + node.g, h=self.problem.heuristic(child_state))
                if (child.state not in explored and child.state not in [f.state for f in frontier]):
                    frontier.append(child)
                elif (child.state in [f.state for f in frontier if f.g + f.h > child.g + child.h]):
                    frontier[next(i for i, x in enumerate(frontier) if x.state == child.state)] = child
            frontier.sort(key=lambda x: x.g + x.h)

if __name__ == "__main__":

    def result(state, action):
        state_list = list(state)
        a, b = state_list.index('0'), action
        state_list[b], state_list[a] = state_list[a], state_list[b]
        return ''.join(state_list)
    
    actions = {}
    cost = 1
    keys = {
        0: [[1, cost], [3, cost]], 
        1: [[2, cost],[4, cost],[0, cost]], 
        2: [[5, cost],[1, cost]], 
        3: [[0, cost],[4, cost],[6, cost]], 
        4: [[1, cost],[5, cost],[7, cost],[3, cost]], 
        5: [[2, cost],[8, cost],[4, cost]], 
        6: [[3, cost],[7, cost]], 
        7: [[4, cost],[8, cost],[6, cost]], 
        8: [[5, cost],[7, cost]]}

    for perm in [''.join(map(str, p)) for p in permutations(range(9))]:
        actions[perm] = keys[perm.index('0')]
            

    def heuristic(s: str):
        goal = list('123456780')
        state = list(s)
        total = 0
        for i in range(9):
            if (goal.index(str(i)) != state.index(str(i))):
                total += 1
        return total
    
    initial_state = Node('743216508')
    goal_nodes = [Node('123456780')]

    problem = Problem(initial_state=initial_state, goal_nodes=goal_nodes, actions=actions, heuristic=heuristic, func=result)
    ast = AST(problem)

    res = ast.search()
    print(res)
    print(len(res))

# if __name__ == "__main__":
#     actions = {
#         'S': [['A', 5], ['B', 9], ['D', 6]], 
#         'A': [['G1', 9], ['B', 3]],
#         'B': [['A', 2], ['C', 1]], 
#         'C': [['S', 6], ['G2', 5], ['F', 7]], 
#         'D': [['S', 1], ['C', 2], ['E', 2]], 
#         'E': [['G3', 4]], 
#         'F': [['D', 2], ['G3', 8]],
#         'G1': [],
#         'G2': [],
#         'G3': []
#     }
#     def heuristic(s: str):
#         return {
#             'S': 5, 
#             'A': 7,
#             'B': 3, 
#             'C': 4, 
#             'D': 6, 
#             'E': 5, 
#             'F': 6,
#             'G1': 0,
#             'G2': 0,
#             'G3': 0    
#         }[s]
   
#     initial_state = Node('S', h=heuristic('S'))
#     goal_nodes = [Node('G1'), Node('G2'), Node('G3')]
#     problem = Problem(initial_state=initial_state, goal_nodes=goal_nodes, actions=actions, heuristic=heuristic)
#     ast = AST(problem)

#     print(ast.search())
