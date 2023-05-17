import numpy as np

class Agent:
    def __init__( self, env, learning_rate=0.1, initial_epsilon=1.0, epsilon_decay=0.001, final_epsilon=0.1, discount_factor=0.95):
        self.q = np.array([  
            [0.009, 0.192, 0.007, 0.009],  
            [0.003, 0.002, 0.003, 0.17],  
            [0.003, 0.002, 0.001, 0.067],  
            [0.001, 0.001, 0.002, 0.037],  
            [0.526, 0.002, 0.001, 0.002],  
            [0., 0., 0., 0.],  
            [0.046, 0., 0., 0.],  
            [0., 0., 0., 0.],  
            [0.002, 0.002, 0.002, 0.709],  
            [0.001, 0.597, 0.001, 0.001],  
            [0.945, 0., 0., 0.],  
            [0., 0., 0., 0.],  
            [0., 0., 0., 0.],  
            [0.02, 0.012, 0.898, 0.016],  
            [0.061, 0.991, 0.092, 0.068],  
            [0., 0., 0., 0.]  
	    ])
        self.epsilon = initial_epsilon
        self.epsilon_decay = epsilon_decay
        self.final_epsilon = final_epsilon
        self.env = env
        self.alpha = learning_rate
        self.gamma = discount_factor

    def get_action(self, obs):
        if (np.random.uniform() < self.epsilon):
            return np.random.randint(3)
        return np.argmax(self.q[obs])

    def update( self, obs, action, reward, next_obs):
        self.q[obs, action] += self.alpha * (reward + ( self.gamma * np.max(self.q[next_obs])) - self.q[obs, action])
    
    def decay_epsilon(self):
        self.epsilon = max(self.final_epsilon, self.epsilon - self.epsilon_decay)