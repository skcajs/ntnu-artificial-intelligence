import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self,  x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        # Don't need an actuation function
        return x
    
    def save(self, file_name='model.pth'):
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)

    def load(self, file_name='model.pth'):
        model_folder_path = './model'
        file_name = os.path.join(model_folder_path, file_name)
        if os.path.exists(file_name):
            print("Loading ", file_name)
            self.load_state_dict(torch.load(file_name))

class QTrainer:
    def __init__(self, model, lr, gamma):
        self.model = model
        self.lr = lr # learning rate
        self.gamma = gamma
        self.optimiser = optim.Adam(model.parameters(), lr=self.lr) # choose an optimiser, in this case Adam
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        # if multiple values, the shape is correct

        # if only have one dimension
        if len(state.shape) == 1:
            # needs to be (1, x)
            state = torch.unsqueeze(state, 0) # appends one dimension at the start
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done, )

        # 1: predicted Q values with current state
        pred = self.model(state)

        target = pred.clone()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx]:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state))

            target[idx][torch.argmax(action).item()] = Q_new # Item so returns value not a tensor

        # 2: Q_new = r + gamma * max(next_predicted_QValue) -> only do this if not done
        # pred.clone()
        # preds[argmax(action)] = Q_new
        # loss = (Q_new - Q)**2 -> Mean Squared
        self.optimiser.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimiser.step()




