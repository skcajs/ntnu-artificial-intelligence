class Agent:
    def __init__( self, env, learning_rate=0.1,
        initial_epsilon=1.0, epsilon_decay=10**(-50000),
        final_epsilon=0.1, discount_factor=0.95):
        pass
    def get_action(self, obs):
        pass
    def update( self, obs, action, reward, terminated, next_obs):
        pass
    def decay_epsilon(self):
        pass