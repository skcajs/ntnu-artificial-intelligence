import torch
import random
import numpy as np
from collections import deque
from q_model import Linear_QNet, QTrainer


MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self, initial_epsilon=0.4, epsilon_decay=0.005, final_epsilon=0.000, discount_factor=0.9):
        self.episodes = 0
        self.epsilon = initial_epsilon # randomness
        self.epsilon_decay = epsilon_decay
        self.final_epsilon = final_epsilon
        self.gamma = discount_factor # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        self.model = Linear_QNet(11, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done)) # popleft if MAX_MEMORY is reached

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            batch_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            batch_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*batch_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        # random moves: tradeoff exploration / exploitation
        action = [0,0,0]
        if np.random.uniform() < self.epsilon:
            idx = random.randint(0, 2)
            action[idx] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            idx = torch.argmax(prediction).item()
            action[idx] = 1
        return action
    
    def decay_epsilon(self):
        self.epsilon = max(self.final_epsilon, self.epsilon - self.epsilon_decay)