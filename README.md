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
epoch5000 win_rate: 0.975
epoch10000 win_rate: 0.979
epoch15000 win_rate: 0.976
epoch20000 win_rate: 0.977
epoch25000 win_rate: 0.976
epoch30000 win_rate: 0.982
epoch35000 win_rate: 0.985
epoch40000 win_rate: 0.988
==========
RLPlayer vs Type2Player
epoch5000 win_rate: 0.964
epoch10000 win_rate: 0.966
epoch15000 win_rate: 0.975
epoch20000 win_rate: 0.977
epoch25000 win_rate: 0.981
epoch30000 win_rate: 0.987
epoch35000 win_rate: 0.982
epoch40000 win_rate: 0.982
==========
RLPlayer vs Type3Player
epoch5000 win_rate: 0.884
epoch10000 win_rate: 0.902
epoch15000 win_rate: 0.916
epoch20000 win_rate: 0.914
epoch25000 win_rate: 0.9
epoch30000 win_rate: 0.884
epoch35000 win_rate: 0.91
epoch40000 win_rate: 0.911
==========
 Type1Player vs RLPlayer
epoch5000 win_rate: 0.823
epoch10000 win_rate: 0.876
epoch15000 win_rate: 0.88
epoch20000 win_rate: 0.898
epoch25000 win_rate: 0.903
epoch30000 win_rate: 0.913
epoch35000 win_rate: 0.905
epoch40000 win_rate: 0.898
==========
 Type2Player vs RLPlayer
epoch5000 win_rate: 0.778
epoch10000 win_rate: 0.842
epoch15000 win_rate: 0.855
epoch20000 win_rate: 0.857
epoch25000 win_rate: 0.856
epoch30000 win_rate: 0.904
epoch35000 win_rate: 0.897
epoch40000 win_rate: 0.908
==========
 Type3Player vs RLPlayer
epoch5000 win_rate: 0.402
epoch10000 win_rate: 0.401
epoch15000 win_rate: 0.433
epoch20000 win_rate: 0.419
epoch25000 win_rate: 0.427
epoch30000 win_rate: 0.471
epoch35000 win_rate: 0.454
epoch40000 win_rate: 0.449
```
### 10-armed bandit
#### Ex1: Stationary Bandit, $\epsilon$-greedy Agent with UCB
![image](https://github.com/Browninomia/Foundations-of-Reinforcement-Learning/blob/master/IMG/ex1-action.pdf)
![image](https://github.com/Browninomia/Foundations-of-Reinforcement-Learning/blob/master/IMG/ex1-reward.pdf)
#### EX2: Non-stationary Bandit, $\epsilon$-greedy Agent with step-size
![image](https://github.com/Browninomia/Foundations-of-Reinforcement-Learning/blob/master/IMG/ex2-action.pdf)
![image](https://github.com/Browninomia/Foundations-of-Reinforcement-Learning/blob/master/IMG/ex2-reward.pdf)