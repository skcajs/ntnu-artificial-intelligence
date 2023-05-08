from utils import Problem, Node

class AST:
    def __init__(self, problem: Problem):
        self.problem = problem
    
    def search(self) -> list:
        node = self.problem.initial_state
        frontier = [node]
        explored = []
        goals = []
        while True:
            if(len(frontier) == 0):
                if(len(goals) == 0):
                    return []
                return self.problem.solution(min(goals, key=lambda x: x.g))
            node = frontier.pop(0)
            explored.append(node.state)
            for action in self.problem.actions[node.state]:
                child_state = self.problem.result(node.state, action[0])
                child = Node(child_state, node, g=action[1] + node.g, h=self.problem.heuristics[child_state])
                if(self.problem.goal_test(child.state) and child.state not in [goal.state for goal in goals]):
                    goals.append(child)
                elif (child.state in [goal.state for goal in goals if goal.g + goal.h > child.g + child.h]):
                    goals[next(i for i, x in enumerate(goals) if x.state == child.state)] = child
                if (child.state not in explored and child.state not in [f.state for f in frontier]):
                    frontier.append(child)
                elif (child.state in [f.state for f in frontier if f.g + f.h > child.g + child.h]):
                    frontier[next(i for i, x in enumerate(frontier) if x.state == child.state)] = child
            frontier.sort(key=lambda x: x.g + x.h)

if __name__ == "__main__":
    actions = {
        'S': [['A', 5], ['B', 9], ['D', 6]], 
        'A': [['G1', 9], ['B', 3]],
        'B': [['A', 2], ['C', 1]], 
        'C': [['S', 6], ['G2', 5], ['F', 7]], 
        'D': [['S', 1], ['C', 2], ['E', 2]], 
        'E': [['G3', 7]], 
        'F': [['D', 2], ['G3', 8]],
        'G1': [],
        'G2': [],
        'G3': []
    }
    heuristics = {
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
    }
    initial_state = Node('S', h=heuristics['S'])
    goal_nodes = [Node('G1'), Node('G2'), Node('G3')]
    problem = Problem(initial_state=initial_state, goal_nodes=goal_nodes, heuristics=heuristics, actions=actions)
    ast = AST(problem)

    print(ast.search())
