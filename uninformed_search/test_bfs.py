import unittest
import bfs

class TestBFS(unittest.TestCase):
    def testThatSimpleSearchWorks(self):
        actions = {'A':['B', 'E'], 'B': ['C','A'], 'C': ['D', 'H', 'E', 'B'], 'D': ['C','J'], 'E':['A', 'C', 'F'], 'F': ['E', 'G'], 'G': ['F', 'H', 'I'], 'H': ['C', 'J', 'I', 'G'], 'J': ['D', 'H', 'I']}
        initial_state = bfs.Node('A')
        goal_state = bfs.Node('I')
        problem = bfs.Problem(initial_state, goal_state, actions)

        actual = bfs.BFS(problem)
        expected = ['I', 'H', 'C', 'B', 'A']
        self.assertEqual(actual, expected)