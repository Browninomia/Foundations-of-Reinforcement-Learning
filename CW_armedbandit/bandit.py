import random
import numpy as np


class Bandit():
    def __init__(self, k: int = 10) -> None:
        self.k = k
        self.q = np.random.normal(0, 1, k)

    def reward(self, action: int) -> float:
        return random.normalvariate(self.q[action], 1)


class BanditNonStationary():
    def __init__(self, nonstation_std: float, init_value: float = 0., k: int = 10) -> None:
        self.k = k
        self.init_value = init_value
        self.nonstation_std = nonstation_std
        self.q = np.array([init_value for _ in range(self.k)])

    def reward(self, action: int) -> float:
        self.q += np.random.normal(0, self.nonstation_std, self.k)
        return random.normalvariate(self.q[action], 1)

    def get_optimal_action(self) -> int:
        return np.argmax(self.q)

    def reset(self) -> None:
        self.q = np.array([self.init_value for _ in range(self.k)])
