from math import sqrt, log
import random
import numpy as np
from bandit import Bandit, BanditNonStationary


class AgentUCB():
    def __init__(self, epsilon: float, init_value: float, c: float = 2, k: int = 10) -> None:
        self.epsilon = epsilon
        self.c = c
        self.k = k
        self.Q = np.array([init_value]*k, dtype=np.float32)
        self.N = np.zeros(k, dtype=int)
        self.UCB = np.array([np.inf]*k, dtype=np.float32)

    def train(self, bandit: Bandit, step: int):
        assert self.k == bandit.k
        rewards = np.zeros(step)
        is_optimal = np.zeros(step)
        optimal_a = np.argmax(bandit.q)
        for i in range(step):
            greedy_flag = random.uniform(0, 1) > self.epsilon
            if greedy_flag:
                a = np.argmax(self.Q)
            else:
                a = np.argmax(self.UCB)
            self.N[a] += 1
            rewards[i] = bandit.reward(a)
            is_optimal[i] = int(a == optimal_a)
            self.Q[a] = self.Q[a] + 1/self.N[a]*(rewards[i]-self.Q[a])
            self.UCB[a] = self.Q[a] + self.c * sqrt(log(i+1)/self.N[a])
        return rewards, is_optimal


class AgentStepSzie():
    def __init__(self, epsilon: float, k: int = 10, alpha: float = None) -> None:
        self.epsilon = epsilon
        self.k = k
        self.Q = np.zeros(k, dtype=int)
        self.N = np.zeros(k, dtype=int)
        self.alpha = alpha

    def train(self, bandit: BanditNonStationary, step: int):
        assert self.k == bandit.k
        rewards = np.zeros(step)
        is_optimal = np.zeros(step)
        for i in range(step):
            greedy_flag = random.uniform(0, 1) > self.epsilon
            if greedy_flag:
                a = np.argmax(self.Q)
            else:
                a = random.randrange(self.k)
            self.N[a] += 1
            rewards[i] = bandit.reward(a)
            is_optimal[i] = int(a == bandit.get_optimal_action())
            if self.alpha is None:
                self.Q[a] = self.Q[a] + 1/self.N[a]*(rewards[i]-self.Q[a])
            else:
                self.Q[a] = self.Q[a] + self.alpha*(rewards[i]-self.Q[a])
        return rewards, is_optimal
