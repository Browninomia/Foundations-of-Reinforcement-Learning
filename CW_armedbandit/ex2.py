from multiprocessing import Pool
import numpy as np
from bandit import BanditNonStationary
from agent import AgentStepSzie
import matplotlib.pyplot as plt

run_num = 2000
step = 10000


def run(pid):
    if pid % 200 == 0:
        print(f"epoch {pid}")
    rewards = np.zeros((2, step))
    is_optimal = np.zeros((2, step))
    bandit = BanditNonStationary()
    agent1 = AgentStepSzie(epsilon=0.1)
    agent2 = AgentStepSzie(epsilon=0.1, alpha=0.1)
    rewards[0], is_optimal[0] = agent1.train(bandit, step)
    rewards[1], is_optimal[1] = agent2.train(bandit, step)
    return (rewards, is_optimal)


if __name__ == '__main__':
    with Pool(4) as p:
        ans = p.map(run, range(run_num))
    x = np.arange(step)
    rewards = np.mean((np.array(ans)[:, 0]), axis=0)
    is_optimal = np.mean((np.array(ans)[:, 1]), axis=0)
    fig, ax = plt.subplots()
    ax.plot(x, rewards[0], label='sample average', color='gray')
    ax.plot(x, rewards[1], label='constant step size', color='b')
    ax.set(ylabel='Average reward', xlabel='Steps')
    plt.legend()
    plt.savefig('ex2-reward.pdf', format='pdf')

    fig, ax = plt.subplots()
    ax.plot(x, is_optimal[0], label='sample average', color='gray')
    ax.plot(x, is_optimal[1], label='constant step size', color='b')
    ax.set(ylabel='Optimal action %', xlabel='Steps')
    plt.legend()
    plt.savefig('ex2-action.pdf')
