class MDP:
    def __init__(self, N):
        self.N = N
        self.startState = 1
        self.endState = N
        self.discount = 1.
        self.states = range(1, N+1)
        self.epsilon = 1e-10

    def isEnd(self, state):
        return state == self.endState
    
    def transition_and_reward(self, state, action):
        # Returns (a', T, R)
        # T(s, a, s'), R(s, a, s')
        result = []
        if action=='walk':
            result.append((state+1, 1., -1))
        elif action=='tram':
            result.append((state*2, 0.5, -2))
            result.append((state, 0.5, -2))
        return result
    