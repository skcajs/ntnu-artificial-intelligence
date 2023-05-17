import matplotlib.pyplot as plt
from agent import Agent

import gym

env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False,render_mode="array")

done = False
all_rewards = []
epsilons = []
observation, info = env.reset()

action = env.action_space.sample()
observation, reward, terminated, truncated, info = env.step(action)

agent = Agent( env )

for episode in range(2000):
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

print(all_rewards)

plt.plot(epsilons)
plt.show()
