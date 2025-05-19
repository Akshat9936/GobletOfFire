# GobletOfFire

This project contains:
1. *main.py* : Main file to run the program. It initializes the game enviornment and Q-learning agent. It runs multiple training episodes and saves the data in q_table.pkl
2. *game.py* : This class handles the grid world, obstacles (walls), Harry, Death Eater, Cup, and all game logic.
3. *agent.py* : Implements the core Q-learning logic.
4. *bfs.py* : Breadth-First Search Pathfinding.
5. *map.txt* : Contains the map on which grid is made.
6. *q_table.pkl* : Automatically saved memory of learned behaviour, updated every 1000 episodes.


The assumptions and logic used in the project: 
1. Making the game enviornment using Pygame.
2. Harry (blue colored cell) to reach the cup (green colored cell) before death eater (red colored cell) reached to Harry.
3. Harry uses Q-learning approach to optomise and learn its path.
4. Death eater uses bfs to track the optimal path to reach Harry.
5. Assumptions :
   **alpha=0.5, gamma=0.98**: Faster learning and more long-term reward focus.
   **epsilon=0.2**: Balances exploration/exploitation well.
   **SHOW_GAME = True** in *main.py*, by which the game is visible and you can make it **False** for making training much faster.

To run the program, go to *main.py* and run.
