import torch
import torch.nn as nn

class EnhanceNetwork(nn.Module):
    def __init__(self):
        super(EnhanceNetwork, self).__init__()
        self.out_conv = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, stride=1, padding=1),
            nn.Sigmoid()
        )

    def forward(self, input):
        fea = self.out_conv(input)
        illu = fea + input
        illu = torch.clamp(illu, 0.0001, 1)

        return illu


class Network(nn.Module):

    def __init__(self):
        super(Network, self).__init__()
        self.enhance = EnhanceNetwork()

    def forward(self, input):
        i1 = self.enhance(input)
        r1 = input / i1
        r1 = torch.clamp(r1, 0, 1)
        return r1
