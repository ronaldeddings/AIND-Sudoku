# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Constraint propagation was used in this problem by eliminating values with the naked twins technique.  More specifically, when a box has two possible combinations and share the same combination with another peer, naked twins function eliminates both of the value combinations from other peers.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Constraint propagation was used by eliminating values with eliminate, only choice and search strategies.  First, eliminate strategy was used by removing value possibilities that are already assigned to another peer.  Second, only choice strategy was used as a constraint by searching for boxes that have only one value possibility and removing value from peers.  Lastly, search strategy was used as the algorithm to satisfy our constraint satisfaction problem 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - My Completed Solution.
* `solution_test.py` - Test solution by running `python solution_test.py`.
* `PySudoku.py` -  This is code for visualizing your solution.
* `visualize.py` - This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py
