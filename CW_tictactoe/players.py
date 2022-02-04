from abc import abstractmethod, ABCMeta
from random import randrange
import numpy as np
from symmetry import equiv


class Player(metaclass=ABCMeta):
    def __init__(self, side: str) -> None:
        assert (side in ['X', 'O'])
        self.side = side
        self.oppo_side = 'O' if self.side == 'X' else 'X'

    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]

    def has_line(self, s, side) -> str:
        for i1, i2, i3 in self.lines:
            if s[i1] == s[i2] and s[i2] == s[i3] and s[i3] == side:
                return True
        return False

    def is_win(self, s) -> bool:
        return self.has_line(s, self.side)

    def is_lose(self, s) -> bool:
        return self.has_line(s, self.oppo_side)

    def any_blank(self, s) -> bool:
        return (np.array(s) == '').any()

    def random(self, s) -> int:
        if not self.any_blank(s):
            return None
        num = randrange(9)
        while s[num] != '':
            num = randrange(9)
        return num

    @abstractmethod
    def react(self, s) -> int:
        if not self.any_blank(s):
            raise ValueError('no blank')
        pass


class Type1Player(Player):
    def __init__(self, side: str) -> None:
        super().__init__(side)

    def react(self, s) -> int:
        super().react(s)
        return self.random(s)


class Type2Player(Player):
    def __init__(self, side: str) -> None:
        super().__init__(side)

    def react(self, s) -> int:
        super().react(s)
        for a in range(9):
            if s[a] != '':
                continue
            s_new = s.copy()
            s_new[a] = self.side
            if self.is_win(s_new):
                return a
        return self.random(s)


class Type3Player(Player):
    def __init__(self, side: str) -> None:
        super().__init__(side)

    def react(self, s) -> int:
        super().react(s)
        for a in range(9):
            if s[a] != '':
                continue
            s_new = s.copy()
            s_new[a] = self.side
            if self.is_win(s_new):
                return a
        for a in range(9):
            if s[a] != '':
                continue
            s_new = s.copy()
            s_new[a] = self.oppo_side
            if self.is_lose(s_new):
                return a
        return self.random(s)


class RLPlayer(Player):
    def __init__(self, side, alpha: float, epsilon: float) -> None:
        super().__init__(side)
        self.alpha = alpha
        self.epsilon = epsilon
        self.V = {}
        self.labels = {}
        self.state_label_cnt = 0

    def get_lb(self, s):
        return self.labels[tuple(s)]

    def set_lb(self, s, l):
        self.labels[tuple(s)] = l

    def init_V(self, s):
        if tuple(s) not in self.labels:
            for equiv_index in equiv:
                s_equiv = tuple([s[i] for i in equiv_index])
                self.set_lb(s_equiv, self.state_label_cnt)
            self.state_label_cnt += 1
        if self.is_win(s):
            self.V[self.get_lb(s)] = 1
        elif self.is_lose(s):
            self.V[self.get_lb(s)] = 0
        elif not self.any_blank(s):
            self.V[self.get_lb(s)] = 0
        else:
            self.V[self.get_lb(s)] = 0.5

    def update_V(self, s_new, s_old):
        if tuple(s_old) not in self.labels:
            self.init_V(s_old)
        if tuple(s_new) not in self.labels:
            self.init_V(s_new)
        self.V[self.get_lb(s_old)] = (
            self.V[self.get_lb(s_old)]
            + self.alpha*(self.V[self.get_lb(s_new)]-self.V[self.get_lb(s_old)]))

    def react(self, s, greedy: bool) -> int:
        if not greedy:
            return self.random(s)
        super().react(s)
        max_V = -float('inf')
        for a in range(9):
            if s[a] == '':
                s_new = s.copy()
                s_new[a] = self.side
                if tuple(s_new) not in self.labels:
                    self.init_V(s_new)
                if self.V[self.get_lb(s_new)] >= max_V:
                    max_V = self.V[self.get_lb(s_new)]
                    a_opt = a
        return a_opt

    def is_end(self, s) -> bool:
        if self.is_win(s) or self.is_lose(s) or (not self.any_blank(s)):
            return True
        else:
            return False
