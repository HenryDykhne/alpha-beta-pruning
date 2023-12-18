# alpha-beta-pruning
# installing scipy, numpy, func-timeout
run in terminal: 
```
python3 -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
pip install func-timeout
```
# running
run in terminal:
`python3 Play.py`

# Notes
* When the machine realizes it is in a lost position, it will not try to extend the game. This is not a bug. It is the lack of a feature.
* if you wish to change the thinking time of the AI, the variable may be modified in the `AI.py` file. The variable is called `thinkTime`.

# Further improvements
* Making the AI resist in lost positions by trying to go for the longest surviving line
* adding the `thinkTime` variable to the list
* refactoring of `Play.ai` code for readability and to reduce unnecessary repetition.
* Optimization of eval code
* Better eval code
* rewrite the whole thing in `rust` or `c++` so it doesn't run like a whale.
* increased usage of transposition table
* addition of `quiescence search`
* improved move ordering (examine if the implementation of last depth eval for move ordering is even correct)
* killer moves search
* current timeout is soft. often runs over by 1 - 4 seconds based on board size. examine ways to harden the limit, or reduce the total thinking time as a catchall based on board size
* let the player pick a side to play instead of always playing X
* let the player pick AI params when watching AI vs AI battle.
