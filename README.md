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
epoch5000, win_rate: 0.971, oppo_win_rate: 0.021
epoch10000, win_rate: 0.977, oppo_win_rate: 0.016
epoch15000, win_rate: 0.978, oppo_win_rate: 0.014
epoch20000, win_rate: 0.980, oppo_win_rate: 0.013
epoch25000, win_rate: 0.983, oppo_win_rate: 0.011
epoch30000, win_rate: 0.983, oppo_win_rate: 0.011
epoch35000, win_rate: 0.983, oppo_win_rate: 0.015
epoch40000, win_rate: 0.985, oppo_win_rate: 0.011
epoch45000, win_rate: 0.987, oppo_win_rate: 0.007
epoch50000, win_rate: 0.984, oppo_win_rate: 0.015
==========
RLPlayer vs Type2Player
epoch5000, win_rate: 0.874, oppo_win_rate: 0.081
epoch10000, win_rate: 0.943, oppo_win_rate: 0.022
epoch15000, win_rate: 0.984, oppo_win_rate: 0.008
epoch20000, win_rate: 0.993, oppo_win_rate: 0.005
epoch25000, win_rate: 0.988, oppo_win_rate: 0.008
epoch30000, win_rate: 0.990, oppo_win_rate: 0.007
epoch35000, win_rate: 0.990, oppo_win_rate: 0.007
epoch40000, win_rate: 0.989, oppo_win_rate: 0.008
epoch45000, win_rate: 0.990, oppo_win_rate: 0.007
epoch50000, win_rate: 0.989, oppo_win_rate: 0.007
==========
RLPlayer vs Type3Player
epoch5000, win_rate: 0.886, oppo_win_rate: 0.082
epoch10000, win_rate: 0.896, oppo_win_rate: 0.076
epoch15000, win_rate: 0.909, oppo_win_rate: 0.069
epoch20000, win_rate: 0.890, oppo_win_rate: 0.080
epoch25000, win_rate: 0.912, oppo_win_rate: 0.067
epoch30000, win_rate: 0.910, oppo_win_rate: 0.067
epoch35000, win_rate: 0.888, oppo_win_rate: 0.088
epoch40000, win_rate: 0.875, oppo_win_rate: 0.095
epoch45000, win_rate: 0.902, oppo_win_rate: 0.070
epoch50000, win_rate: 0.891, oppo_win_rate: 0.077
==========
 Type1Player vs RLPlayer
epoch5000, win_rate: 0.773, oppo_win_rate: 0.185
epoch10000, win_rate: 0.846, oppo_win_rate: 0.126
epoch15000, win_rate: 0.881, oppo_win_rate: 0.094
epoch20000, win_rate: 0.894, oppo_win_rate: 0.084
epoch25000, win_rate: 0.913, oppo_win_rate: 0.070
epoch30000, win_rate: 0.912, oppo_win_rate: 0.070
epoch35000, win_rate: 0.918, oppo_win_rate: 0.069
epoch40000, win_rate: 0.918, oppo_win_rate: 0.066
epoch45000, win_rate: 0.914, oppo_win_rate: 0.065
epoch50000, win_rate: 0.924, oppo_win_rate: 0.061
==========
 Type2Player vs RLPlayer
epoch5000, win_rate: 0.756, oppo_win_rate: 0.185
epoch10000, win_rate: 0.838, oppo_win_rate: 0.126
epoch15000, win_rate: 0.846, oppo_win_rate: 0.119
epoch20000, win_rate: 0.853, oppo_win_rate: 0.115
epoch25000, win_rate: 0.845, oppo_win_rate: 0.124
epoch30000, win_rate: 0.874, oppo_win_rate: 0.103
epoch35000, win_rate: 0.906, oppo_win_rate: 0.066
epoch40000, win_rate: 0.911, oppo_win_rate: 0.062
epoch45000, win_rate: 0.899, oppo_win_rate: 0.066
epoch50000, win_rate: 0.906, oppo_win_rate: 0.061
==========
 Type3Player vs RLPlayer
epoch5000, win_rate: 0.389, oppo_win_rate: 0.528
epoch10000, win_rate: 0.378, oppo_win_rate: 0.537
epoch15000, win_rate: 0.429, oppo_win_rate: 0.483
epoch20000, win_rate: 0.451, oppo_win_rate: 0.453
epoch25000, win_rate: 0.450, oppo_win_rate: 0.460
epoch30000, win_rate: 0.458, oppo_win_rate: 0.446
epoch35000, win_rate: 0.415, oppo_win_rate: 0.503
epoch40000, win_rate: 0.415, oppo_win_rate: 0.511
epoch45000, win_rate: 0.455, oppo_win_rate: 0.445
epoch50000, win_rate: 0.441, oppo_win_rate: 0.465
```
### 10-armed bandit
The plots are in ./IMG directory