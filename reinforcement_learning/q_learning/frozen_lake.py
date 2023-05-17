import matplotlib.pyplot as plt
from agent import Agent

import gym

env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True,render_mode="human")

done = False
observation, info = env.reset()

rewards = []

action = env.action_space.sample()
observation, reward, terminated, truncated, info = env.step(action)

agent = Agent( env, initial_epsilon=0 )
agent.load_q_tables('reinforcement_learning\q_learning\q.txt')

for episode in range(30):
    obs, info = env.reset()
    done = False

    # play one episode
    while not done:
        action = agent.get_action(obs)
        next_obs, reward, terminated, truncated, info = env.step(action)

        # update if the environment is done and the current obs
        done = terminated or truncated
        obs = next_obs
        if(done):
            rewards.append(reward)

# sample = 100

# groups = [rewards[x:x+sample] for x in range(0, len(rewards), sample)]
# means = [sum(group)/len(group) for group in groups]

# print("Average Rewards: ", sum(means)/len(means))

plt.plot(rewards)
plt.show()