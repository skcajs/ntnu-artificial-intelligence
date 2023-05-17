import numpy as np

class Agent:
    def __init__( self, env, learning_rate=0.1, initial_epsilon=1.0, epsilon_decay=0.001, final_epsilon=0.01, discount_factor=0.95):
        self.env = env
        self.q = np.zeros((16,4))
        self.epsilon = initial_epsilon
        self.epsilon_decay = epsilon_decay
        self.final_epsilon = final_epsilon
        self.alpha = learning_rate
        self.gamma = discount_factor

    def get_action(self, obs):
        if (np.random.uniform() < self.epsilon):
            return self.env.action_space.sample()
        return np.argmax(self.q[obs])

    def update( self, obs, action, reward, next_obs):
        self.q[obs, action] += self.alpha * (reward +  self.gamma * np.max(self.q[next_obs]) - self.q[obs, action])
    
    def decay_epsilon(self):
        self.epsilon = max(self.final_epsilon, self.epsilon - self.epsilon_decay)

    def load_q_tables(self, location):
        self.q = np.loadtxt(location)

    def write_q_table(self, location, x, episode, route):
        with open(location, "a") as f:
            f.write("\n\n")
            f.write(f"Epsiode:  {episode}")
            f.write("\n")
            f.write(f"Route:  {route}")
            f.write("\n")
            np.savetxt(f, x)