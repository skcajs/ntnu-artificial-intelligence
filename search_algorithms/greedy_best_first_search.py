from utils import Problem, Node

class greedy_best_first_search:
    def __init__(self, problem):
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
                child = Node(self.problem.result(node.state, action[0]), node, action[1] + node.cost)
                if (child.state not in explored and child.state not in [f.state for f in frontier]):
                    frontier.append(child)
                elif (child.state in [f.state for f in frontier if f.cost > child.cost]):
                    frontier[next(i for i, x in enumerate(frontier) if x.state == child.state)] = child
            frontier.sort(key=lambda x: x.cost)
