from utils import Problem, Node

class DepthFirstSearch:

    def __init__(self, problem: Problem, depth: int = 50):
        self.problem = problem
        self.depth = depth

    def search(self, depth: int = None) -> list:
        explored = []
        if not depth:
            depth = self.depth
        return self.__search(self.problem.initial_state, explored, depth)

    def __search(self, node: Node, explored: list, depth: int):
        if(self.problem.goal_test(node.state)):
            return self.problem.solution(node)
        if(depth == 0):
            return None
        explored.append(node.state)
        for action in self.problem.actions[node.state]:
            child = Node(self.problem.result(node.state, action), node)
            result = None
            if(child.state not in explored):
                result = self.__search(child, explored, depth-1)
            if result:
                return result
        return None


if __name__ == "__main__":
    actions = {'A':['G', 'B'], 'B': ['C'], 'C': ['D'], 'D': ['E', 'H'], 'E':['F'], 'F': [], 'G': []}
    initial_state = Node('A')
    goal_nodes = [Node('H')]
    problem = Problem(initial_state, goal_nodes, actions)
    dfs = DFS(problem)

    print(dfs.search())