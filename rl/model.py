import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable


from rl.utils import init


class Flatten(nn.Module):
    def forward(self, x):
        N, C, H, W = x.size()  # read in N, C, H, W
        return x.view(N, -1)


class A2CNet(nn.Module):
    def __init__(self, num_inputs, hidden_size1=64, hidden_size2=64, writer=None):
        super(A2CNet, self).__init__()

        self.num_inputs = num_inputs
        self.writer = writer

        def init_(m): return init(m, nn.init.orthogonal_, lambda x: nn.init.
                                  constant_(x, 0), np.sqrt(2))

        self.mlp = nn.Sequential(
            init_(nn.Linear(num_inputs, hidden_size1)),
            nn.ReLU(),
            init_(nn.Linear(hidden_size1, hidden_size2)),
            nn.ReLU()
        )

        # action space output is 1d vector of [0...1]
        self.actor = init_(nn.Linear(hidden_size2, 1))

        # output of critic is always Value
        self.critic = init_(nn.Linear(hidden_size2, 1))

    def forward(self, x):
        feature = torch.from_numpy(x).float()
        hidden = self.mlp(feature)
        policy = self.actor(hidden)
        value = self.critic(hidden)

        if self.writer is not None:
            self.writer.add_histogram("feature", feature.detach())
            self.writer.add_histogram("policy", policy.detach())
            self.writer.add_histogram("value", value.detach())

        return policy, torch.squeeze(value), feature
