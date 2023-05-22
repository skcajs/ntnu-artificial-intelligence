import gym
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True,render_mode="human")
env.reset()
state, info = env.reset()

alpha = 0.9
epsilon = 1e-10
iterations = 500

mdp = env.P


# utilities = [0.41,0.38,0.35,0.34,0.43,0,0.12,0,0.45,0.48,0.43,0,0,0.59,0.71,1]
done = False


def value_iteration(mdp):
    V = {}
    for key, value in mdp.items():
        V[key] = 0.

    def Q(state, action):
        return sum((i[0] * (i[2] + alpha * V[i[1]]) for i in mdp[state][action]))
    
    for _ in range(iterations):
        new_V = {}
        for key, value in mdp.items():
            if key == 15:
                new_V[key] = 0.
            else:
                new_V[key] = max(Q(key, action) for action in value)

        V = new_V

        # Read policy
        pi = {}
        for key, value in mdp.items():
            if key == 15:
                pi[key] = 'none'
            else:
                pi[key] = max((Q(key, action), action) for action in value)[1]

    return [v for v in V.values()]

utilities = value_iteration(mdp)

while not done:

    action = env.P[state]
    
    # Find the expected utility following each action and choose the best one.

    state, reward, terminated, truncated, info = env.step(action)

    print()  # Add some diagnostic output so that you can see your decision

    done = terminated or truncated