from multiprocessing import Pool
import numpy as np
from bandit import Bandit
from agent import AgentUCB
import matplotlib.pyplot as plt

run_num = 2000
step = 2000


def run(pid):
    if pid % 200 == 0:
        print(f"epoch {pid}")
    rewards = np.zeros((3, step))
    is_optimal = np.zeros((3, step))
    bandit = Bandit()
    agent1 = AgentUCB(epsilon=0, init_value=5)
    agent2 = AgentUCB(epsilon=0.1, init_value=0)
    agent3 = AgentUCB(epsilon=0.01, init_value=0)
    rewards[0], is_optimal[0] = agent1.train(bandit, step)
    rewards[1], is_optimal[1] = agent2.train(bandit, step)
    rewards[2], is_optimal[2] = agent3.train(bandit, step)
    return (rewards, is_optimal)


if __name__ == '__main__':
    with Pool(4) as p:
        ans = p.map(run, range(run_num))
    x = np.arange(step)
    rewards = np.mean((np.array(ans)[:, 0]), axis=0)
    is_optimal = np.mean((np.array(ans)[:, 1]), axis=0)
    ax = plt.subplot(211)
    ax.plot(x, rewards[0], label=r'$\epsilon=0$', color='g')
    ax.plot(x, rewards[1], label=r'$\epsilon=0.1$', color='b')
    ax.plot(x, rewards[2], label=r'$\epsilon=0.01$', color='r')
    ax.set(ylabel='Average reward')
    ax.legend()

    ax = plt.subplot(212)
    ax.plot(x, is_optimal[0], label=r'$\epsilon=0$', color='g')
    ax.plot(x, is_optimal[1], label=r'$\epsilon=0.1$', color='b')
    ax.plot(x, is_optimal[2], label=r'$\epsilon=0.01$', color='r')
    ax.set(ylabel='Optimal action %', xlabel='Steps')
    ax.legend()
    plt.savefig('ex1.pdf')
