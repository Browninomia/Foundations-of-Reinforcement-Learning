from multiprocessing import Pool
import numpy as np
from bandit import BanditNonStationary
from agent import AgentStepSzie
import matplotlib.pyplot as plt

run_num = 2000
step = 10000

EPSILON = 0.1
ALPHA = 0.1


def run(pid):
    if pid % 200 == 0:
        print(f"epoch {pid}")
    rewards = np.zeros((2, step))
    is_optimal = np.zeros((2, step))
    bandit = BanditNonStationary(nonstation_std=0.01)
    agent1 = AgentStepSzie(epsilon=EPSILON)
    agent2 = AgentStepSzie(epsilon=EPSILON, alpha=ALPHA)
    rewards[0], is_optimal[0] = agent1.train(bandit, step)
    bandit.reset()
    rewards[1], is_optimal[1] = agent2.train(bandit, step)
    return (rewards, is_optimal)


if __name__ == '__main__':
    with Pool(4) as p:
        ans = p.map(run, range(run_num))
    x = np.arange(step)
    rewards = np.mean((np.array(ans)[:, 0]), axis=0)
    is_optimal = np.mean((np.array(ans)[:, 1]), axis=0)

    ax = plt.subplot(211)
    ax.plot(x, rewards[0], label='sample average', color='gray')
    ax.plot(x, rewards[1], label='constant step size', color='b')
    ax.set(ylabel='Average reward', title=rf'$\epsilon={EPSILON}$, $\alpha$={ALPHA}')
    ax.legend()

    ax = plt.subplot(212)
    ax.plot(x, is_optimal[0], label='sample average', color='gray')
    ax.plot(x, is_optimal[1], label='constant step size', color='b')
    ax.set(ylabel='Optimal action %', xlabel='Steps')
    ax.legend()
    plt.savefig('ex2.pdf')
