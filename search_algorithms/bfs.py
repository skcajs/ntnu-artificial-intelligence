from utils import Problem, Node

class BFS:
    def __init__(self, problem: Problem):
        self.problem = problem

    def search(self) -> list:
        node = self.problem.initial_state
        frontier = [node]
        explored = []
        if(self.problem.goal_test(node.state)):
            return node.state
        while(True):
            if(len(frontier)==0):
                return None
            node = frontier.pop(0)
            explored.append(node.state)
            for action in self.problem.actions[node.state]:
                child = Node(self.problem.result(node.state, action), node)
                if (child.state not in explored and child.state not in [f.state for f in frontier]):
                    if (self.problem.goal_test(child.state)):
                        return self.problem.solution(child)
                    frontier.append(child)