import unittest
from itertools import permutations
from dfs import DFS
from utils import Problem, Node

class TestBFS(unittest.TestCase):
    def test_that_a_simple_tree_search_returns_optimised_path(self):
        actions = {'A':['B', 'G'], 'B': ['C', 'A'], 'C': ['D', 'B'], 'D': ['E','C'], 'E':['F', 'D'], 'F': ['G', 'E'], 'G': ['F', 'A']}
        initial_state = Node('A')
        goal_state = Node('F')
        problem = Problem(initial_state, goal_state, actions)
        dfs = DFS(problem)

        actual = dfs.search(10)
        expected = ['F', 'E', 'D', 'C', 'B', 'A']
        self.assertEqual(actual, expected)