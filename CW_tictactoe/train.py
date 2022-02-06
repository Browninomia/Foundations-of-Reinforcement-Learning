import random
import players
import sys

epoch_batch_size = 10000
epoch_batch_num = 5

assert sys.argv[1] in ['first', 'second']
first = sys.argv[1] == 'first'

oppo_type = sys.argv[2]
if oppo_type == '1':
    oppo = players.Type1Player('O')
elif oppo_type == '2':
    oppo = players.Type2Player('O')
elif oppo_type == '3':
    oppo = players.Type3Player('O')
else:
    raise ValueError()

ally = players.RLPlayer('X', 0.1, 0.01)
win_num = 0
oppo_win_num = 0
if first:
    print(f"==========\nRLPlayer vs {type(oppo).__name__}")
else:
    print(f"==========\n {type(oppo).__name__} vs RLPlayer")
for i in range(epoch_batch_size * epoch_batch_num):
    s = ['']*9
    if first:
        greedy_flag = random.uniform(0, 1) > ally.epsilon
        a = ally.react(s, greedy_flag)
        s[a] = ally.side
        if greedy_flag:
            ally.update_V(s, ['']*9)
    while not ally.is_end(s):
        # St is the state before opponent moves
        s_old = s.copy()
        a_oppo = oppo.react(s)
        s[a_oppo] = oppo.side
        # if the game over after opponent moves
        if ally.is_end(s):
            ally.update_V(s, s_old)
        else:
            # then we move
            greedy_flag = random.uniform(0, 1) > ally.epsilon
            a = ally.react(s, greedy_flag)
            s[a] = ally.side
            # update Value function
            if greedy_flag:
                ally.update_V(s, s_old)
    if ally.is_win(s):
        win_num += 1
    if oppo.is_win(s):
        oppo_win_num += 1
    if (i+1) % epoch_batch_size == 0:
        print("epoch%d, win_rate: %.3f, oppo_win_rate: %.3f"
              % (i+1, win_num/epoch_batch_size, oppo_win_num/epoch_batch_size))
        win_num = 0
        oppo_win_num = 0
