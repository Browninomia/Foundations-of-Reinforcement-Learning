# Foundations of Reinforcement Learning
This repo contains the code for programming questions in the coursework.
## Tic-Tac-Toe
```sh
cd CW_tictactoe
for i in first second
do
    for j in 1 2 3
    do
        python train.py $i $j
    done
done
```
## 10-Armed Bandit
```sh
cd CW_armedbandit
python ex1.py
python ex2.py
```
## stdout
### tic-tac-toe
```
==========
RLPlayer vs Type1Player
epoch10000, win_rate: 0.978, oppo_win_rate: 0.015
epoch20000, win_rate: 0.981, oppo_win_rate: 0.011
epoch30000, win_rate: 0.981, oppo_win_rate: 0.012
epoch40000, win_rate: 0.981, oppo_win_rate: 0.011
epoch50000, win_rate: 0.986, oppo_win_rate: 0.006
==========
RLPlayer vs Type2Player
epoch10000, win_rate: 0.967, oppo_win_rate: 0.023
epoch20000, win_rate: 0.970, oppo_win_rate: 0.013
epoch30000, win_rate: 0.974, oppo_win_rate: 0.011
epoch40000, win_rate: 0.984, oppo_win_rate: 0.009
epoch50000, win_rate: 0.991, oppo_win_rate: 0.007
==========
RLPlayer vs Type3Player
epoch10000, win_rate: 0.894, oppo_win_rate: 0.074
epoch20000, win_rate: 0.909, oppo_win_rate: 0.067
epoch30000, win_rate: 0.913, oppo_win_rate: 0.064
epoch40000, win_rate: 0.904, oppo_win_rate: 0.066
epoch50000, win_rate: 0.915, oppo_win_rate: 0.058
==========
 Type1Player vs RLPlayer
epoch10000, win_rate: 0.820, oppo_win_rate: 0.145
epoch20000, win_rate: 0.879, oppo_win_rate: 0.106
epoch30000, win_rate: 0.912, oppo_win_rate: 0.067
epoch40000, win_rate: 0.935, oppo_win_rate: 0.046
epoch50000, win_rate: 0.932, oppo_win_rate: 0.046
==========
 Type2Player vs RLPlayer
epoch10000, win_rate: 0.791, oppo_win_rate: 0.157
epoch20000, win_rate: 0.832, oppo_win_rate: 0.133
epoch30000, win_rate: 0.847, oppo_win_rate: 0.119
epoch40000, win_rate: 0.903, oppo_win_rate: 0.070
epoch50000, win_rate: 0.907, oppo_win_rate: 0.065
==========
 Type3Player vs RLPlayer
epoch10000, win_rate: 0.397, oppo_win_rate: 0.525
epoch20000, win_rate: 0.412, oppo_win_rate: 0.497
epoch30000, win_rate: 0.444, oppo_win_rate: 0.453
epoch40000, win_rate: 0.429, oppo_win_rate: 0.482
epoch50000, win_rate: 0.448, oppo_win_rate: 0.456
```
### 10-armed bandit
The plots are in ./IMG directory