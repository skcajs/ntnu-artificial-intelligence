from utils import Problem, Node

class GBFS:
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
                child = Node(child_state, node, h=self.problem.heuristic(child_state))
                if (child.state not in explored and child.state not in [f.state for f in frontier]):
                    frontier.append(child)
                elif (child.state in [f.state for f in frontier if f.h > child.h]):
                    frontier[next(i for i, x in enumerate(frontier) if x.state == child.state)] = child
            frontier.sort(key=lambda x: x.h)