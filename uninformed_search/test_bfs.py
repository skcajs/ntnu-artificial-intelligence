import unittest
from itertools import permutations
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

    def testThat8PuzzleSearchWorks(self):
        def result(state, action):
            state_list = list(state)
            a, b = state_list.index('0'), action
            state_list[b], state_list[a] = state_list[a], state_list[b]
            return ''.join(state_list)
        
        actions = {}
        keys = {0: [1, 3], 1: [2,4,0], 2: [5,1], 3: [0,4,6], 4: [1,5,7,3], 5: [2,8,4], 6: [3,7], 7: [4,8,6], 8: [5,7]}
        
        for perm in [''.join(map(str, p)) for p in permutations(range(9))]:
            actions[perm] = keys[perm.index('0')]
                
        initial_state = bfs.Node('123456708')
        goal_state = bfs.Node('123456780')
        problem = bfs.Problem(initial_state, goal_state, actions, result)

        actual = bfs.BFS(problem)
        expected = ['123456780', '123456708']
        self.assertEqual(actual, expected)