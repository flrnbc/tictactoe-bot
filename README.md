# TICTACTOE-BOT

The aim here is to apply methods of BetaGo/Zero (see [Deep Learning and the Game of Go](https://github.com/maxpumperla/deep_learning_and_the_game_of_go)
which is essentially an open-source implementation of Deepmind's AlphaGo/Zero) to generalized tictactoe games. The advantage of these games is that
the rules are straightforward without any exceptions. One challenge is that there are essentially no avaiable recored games so that we have to rely
on self-play/reinforcement learning for the deep learning bots.

We consider two types and work with black and white stones for the two players (instead of crosses and circles):

1. Any board size (m-by-n) and turn-by-turn as for tictactoe but the players need to connect k stones (k <= m, n).
2. Again any board size with the same goal but the rules are slighlty different: First black places one stone. Then white and black take turns placing _two_ stones each turn.

We will proceed in the following steps:

## TTTboard
Implementation of the boards using TStrings. These are horizontally, vertically or diagonally (maximally) connected stones of a player.
If there is one TString of length k, the game is over.


## Game Tree Search


## BetaGo/Zero
