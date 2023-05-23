import gym
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True,render_mode="human")
env.reset()
state, info = env.reset()

alpha = 0.9
epsilon = 1e-10
iterations = 500

mdp = env.P

done = False


def value_iteration(mdp):
    V = {}
    P = {}
    for state in mdp.keys():
        V[state] = 0.

    def Q(state, action):
        return sum((i[0] * (i[2] + alpha * V[i[1]]) for i in mdp[state][action]))
    
    for _ in range(iterations):
        # Value iteration
        new_V = {}
        for state, actions in mdp.items():
            if state == 15:
                new_V[state] = 0.
            else:
                new_V[state] = max(Q(state, action) for action in actions)

        V = new_V

        # Policy iteration
        pi = {}
        for state, actions in mdp.items():
            if state == 15:
                pi[state] = None
            else:
                pi[state] = max((Q(state, action), action) for action in actions)[1]

        P = pi

    return [p for p in P.values()]

policies = value_iteration(mdp)

while not done:

    action = policies[state]
    
    # Find the expected utility following each action and choose the best one.
    print('current state: ', state, 'policy: ', action)

    state, reward, terminated, truncated, info = env.step(action)

    done = terminated or truncated