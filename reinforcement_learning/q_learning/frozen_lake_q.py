import matplotlib.pyplot as plt
from agent import Agent

import gym

env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True,render_mode="array")

done = False
all_rewards = []
epsilons = []
observation, info = env.reset()

action = env.action_space.sample()
observation, reward, terminated, truncated, info = env.step(action)

agent = Agent( env, learning_rate=0.15, initial_epsilon=1.0, epsilon_decay=0.001, final_epsilon=0.0001, discount_factor=0.99 )

for episode in range(10000):
    obs, info = env.reset()
    done = False

    # play one episode
    while not done:
        action = agent.get_action(obs)
        next_obs, reward, terminated, truncated, info = env.step(action)

        # update the agent
        agent.update(obs, action, reward, next_obs)

        # update if the environment is done and the current obs
        done = terminated or truncated

        if(done):
            all_rewards.append(reward)

        obs = next_obs

    agent.decay_epsilon()
    epsilons.append(agent.epsilon)

print(agent.q)

sample = 100

groups = [all_rewards[x:x+sample] for x in range(0, len(all_rewards), sample)]
means = [sum(group)/len(group) for group in groups]

top = means[75:]
print("Average Rewards: ", sum(top)/len(top))

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(means)
ax2.plot(epsilons)
plt.show()

