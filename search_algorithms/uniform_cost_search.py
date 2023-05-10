from utils import Problem, Node
class UniformCostSearch:
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
                child = Node(self.problem.result(node.state, action[0]), node, action[1] + node.g)
                if (child.state not in explored and child.state not in [f.state for f in frontier]):
                    frontier.append(child)
                elif (child.state in [f.state for f in frontier if f.g > child.g]):
                    frontier[next(i for i, x in enumerate(frontier) if x.state == child.state)] = child
            frontier.sort(key=lambda x: x.g)

if __name__ == "__main__":
    actions = {
        'S': [['A', 5], ['B', 9], ['D', 6]], 
        'A': [['G1', 6], ['B', 3]],
        'B': [['A', 2], ['C', 1]], 
        'C': [['S', 6], ['G2', 5], ['F', 7]], 
        'D': [['S', 1], ['C', 2], ['E', 2]], 
        'E': [['G3', 7]], 
        'F': [['D', 2], ['G3', 8]],
        'G1': [],
        'G2': [],
        'G3': []
    }
    initial_state = Node('S')
    goal_nodes = [Node('G1'), Node('G2'), Node('G3')]
    problem = Problem(initial_state, goal_nodes, actions)
    ucs = UniformCostSearch(problem)

    print(ucs.search())