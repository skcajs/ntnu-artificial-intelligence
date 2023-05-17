import gym
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True,render_mode="human")
obs, info = env.reset()

state, info = env.reset()

# Init utilities
# u = []
# for i in range(16):
#     u.append(0)

# u = [0.41,0.38,0.35,0.34,0.43,0,0.12,0,0.45,0.48,0.43,0,0,0.59,0.71,1]

iterations = 5000
alpha = 0.9
gamma = 0.9

# Init rewards
r = []
for _ in range(15):
    r.append(-0.5)
r.append(1)
r[5] = r[7] = r[11] = r[12] = -1

# Init q's
q = []
for i in range(16):
    q.append([0,0,0,0])

for x in range(iterations):
    print(x)
    state, info = env.reset()
    done = False
    while not done:
        a = q[state].index(max(q[state]))
        next_states = [env.P[state][a][i][1] for i in range(len(env.P[state][a]))]
        q_max = max(max(q[i]) for i in next_states)
        # q_max = max([env.P[state][a][i][2] for i in range(len(env.P[state][a]))])
        q[state][a] = q[state][a] + alpha * (r[state] + q_max - q[state][a])
        state, reward, terminated, truncated, info = env.step(a)
        # print(state, reward, terminated, truncated, info)  # Add some diagnostic output so that you can see your decision
        done = terminated or truncated


def Q_function(state, gamma):
    actions = env.P[state]
    U_s = []
    for i in range(4):
        U_s.append(sum([
            actions[i][0][0] * (actions[i][0][2] + gamma*u[actions[i][0][1]]), 
            actions[i][1][0] * (actions[i][1][2]  + gamma*u[actions[i][1][1]]), 
            actions[i][2][0] * (actions[i][2][2]  + gamma*u[actions[i][2][1]])
        ]))
    return U_s.index(max(U_s))

while True:

    state, info = env.reset()
    done = False

    while not done:
        action = Q_function(state, 0.9)

        # Find the expected utility following each action and choose the best one.

        state, reward, terminated, truncated, info = env.step(action)

        print(state, reward, terminated, truncated, info)  # Add some diagnostic output so that you can see your decision

        done = terminated or truncated