import numpy as np
equiv = set([(6, 3, 0, 7, 4, 1, 8, 5, 2),
             (8, 7, 6, 5, 4, 3, 2, 1, 0),
             (2, 1, 0, 5, 4, 3, 8, 7, 6),
             (2, 5, 8, 1, 4, 7, 0, 3, 6),
             (0, 1, 2, 3, 4, 5, 6, 7, 8),
             (0, 3, 6, 1, 4, 7, 2, 5, 8),
             (6, 7, 8, 3, 4, 5, 0, 1, 2),
             (8, 5, 2, 7, 4, 1, 6, 3, 0), ])


def my_hash(s):
    return tuple(np.ravel(s))


def rotate(s):
    return np.rot90(s)


def trans(s):
    return s.T


def save(s):
    equiv.add(my_hash(s))


if __name__ == '__main__':
    s_tmp = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    for i in range(4):
        save(s_tmp)
        save(trans(s_tmp))
        s_tmp = rotate(s_tmp)

    for s in equiv:
        print('$', end='')
        for num in s:
            print('a_{', end='')
            print(num//3 + 1, end='')
            print(num % 3 + 1, end='}')
        print('$')
    for s in equiv:
        print(s, ',')
