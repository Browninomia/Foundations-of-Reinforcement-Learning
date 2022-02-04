import random
import numpy as np


class Bandit():
    def __init__(self, k: int = 10) -> None:
        self.k = k
        self.q = np.random.normal(0, 1, k)

    def reward(self, action: int) -> float:
        return random.normalvariate(self.q[action], 1)


class BanditNonStationary():
    _q_start = np.array([0.85591312,  0.23193114, -0.43962759,  0.54379396,  0.33924429,
                         1.48170205,  0.83391867, -0.81463182, -0.43322642,  0.8958632])

    def __init__(self, k: int = 10) -> None:
        self.k = k
        self.q = self._q_start

    def reward(self, action: int) -> float:
        self.q += np.random.normal(0, 0.01, self.k)
        return random.normalvariate(self.q[action], 1)

    def get_optimal_action(self) -> int:
        return np.argmax(self.q)
