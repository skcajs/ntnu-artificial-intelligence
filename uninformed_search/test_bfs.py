import unittest
from itertools import permutations
import bfs

class TestBFS(unittest.TestCase):
    def test_that_a_simple_tree_search_returns_optimised_path(self):
        actions = {'A':['B', 'E'], 'B': ['C','A'], 'C': ['D', 'H', 'E', 'B'], 'D': ['C','J'], 'E':['A', 'C', 'F'], 'F': ['E', 'G'], 'G': ['F', 'H', 'I'], 'H': ['C', 'J', 'I', 'G'], 'J': ['D', 'H', 'I']}
        initial_state = bfs.Node('A')
        goal_state = bfs.Node('I')
        problem = bfs.Problem(initial_state, goal_state, actions)

        actual = bfs.BFS(problem)
        expected = ['I', 'H', 'C', 'B', 'A']
        self.assertEqual(actual, expected)

    def test_that_an__unsolvable_6_puzzle_returns_empty_list(self):
        def result(state, action):
            state_list = list(state)
            a, b = state_list.index('0'), action
            state_list[b], state_list[a] = state_list[a], state_list[b]
            return ''.join(state_list)
        
        actions = {}
        keys = {0: [1, 3], 1: [2,4,0], 2: [5,1], 3: [0,4], 4: [1,5,3], 5: [2,4]}

        for perm in [''.join(map(str, p)) for p in permutations(range(6))]:
            actions[perm] = keys[perm.index('0')]
                
        initial_state = bfs.Node('320514')
        goal_state = bfs.Node('123450')
        problem = bfs.Problem(initial_state, goal_state, actions, result)

        actual = bfs.BFS(problem)

        expected = []
        self.assertEqual(actual, expected)

    def test_that_a_solvable_6_puzzle_returns_correct_result(self):
        def result(state, action):
            state_list = list(state)
            a, b = state_list.index('0'), action
            state_list[b], state_list[a] = state_list[a], state_list[b]
            return ''.join(state_list)
        
        actions = {}
        keys = {0: [1, 3], 1: [2,4,0], 2: [5,1], 3: [0,4], 4: [1,5,3], 5: [2,4]}

        for perm in [''.join(map(str, p)) for p in permutations(range(6))]:
            actions[perm] = keys[perm.index('0')]
                
        initial_state = bfs.Node('120345')
        goal_state = bfs.Node('123450')
        problem = bfs.Problem(initial_state, goal_state, actions, result)

        actual = bfs.BFS(problem)

        expected = ['123450', '123405', '123045', '023145', '203145', '230145', '235140', '235104', '205134', '025134', '125034', '125304', '125340', '120345']
        self.assertEqual(actual, expected)

    def test_that_the_8_puzzle_correctly_shows_correct_route(self):
        def result(state, action):
            state_list = list(state)
            a, b = state_list.index('0'), action
            state_list[b], state_list[a] = state_list[a], state_list[b]
            return ''.join(state_list)
        
        actions = {}
        keys = {0: [1, 3], 1: [2,4,0], 2: [5,1], 3: [0,4,6], 4: [1,5,7,3], 5: [2,8,4], 6: [3,7], 7: [4,8,6], 8: [5,7]}

        for perm in [''.join(map(str, p)) for p in permutations(range(9))]:
            actions[perm] = keys[perm.index('0')]
                
        initial_state = bfs.Node('123405678')
        goal_state = bfs.Node('123456780')
        problem = bfs.Problem(initial_state, goal_state, actions, result)

        actual = bfs.BFS(problem)
        expected = ['123456780', '123456708', '123456078', '123056478', '123506478', '123560478', '123568470', '123568407', '123508467', '123058467', '123458067', '123458607', '123458670', '123450678', '123405678']
        self.assertEqual(actual, expected)