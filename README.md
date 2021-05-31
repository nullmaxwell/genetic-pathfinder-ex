# General Problem:
The traveling salesman problem is an infamous programming challenge usually solved by Dijkstra's algorithm or by branching and bounding. In this problem, we attempt to visit each node/city within the environment once beginning and ending at the same city by iteratively creating new generations using a genetic algorithm. 

The genetic solution to this problem has the advantage over a branch and bounding solution as its time complexity is entirely dependent on the number of generations to simulate requested by the user.
***
# How the problem is solved:
Given a list of cities and the milage between each of them, we construct vertices and edges of a graph. 

A generation within the environment is created containing a population of chromosomes that store genes constituting possible solutions to the graph problem. 
The model then simulates evolution from the initial generation by creating new populations through genetic crossover based on the previous generation until the number of generations specified by the user have been created. The model is incentivized to prioritize solutions (genes) that have the best fitness. In our case, the model is using a maximization function to determine the gene with the best fitness. At the end of each iteration, the fitness of the best gene is shown.
***

## The Genetic Algorithm
The genetic algorithm works as described below and is executed for every new member of the population within the generation.
1. The population of chromosomes is sorted by fitness.
2. The 10 with the best fitness are ported straight into the next generation's population.
3. 10 random chromosomes are chosen from the previous generation's population to allow for some genetic variance.
4. 2 of the 5 chromosomes with the best fitness within this subset are chosen and undergo a crossover process.
***

# Usage
In the cloned directory there are a couple of ways to run the experiment:
*Note: this project has no dependencies outside of vanilla Python 3.8*
- **A. Conventional running with commandline arguments with:**
	1. ```python3 main.py <cities_XX.txt> <cities_milage_XX.txt> <POPULATION_SIZE> <NUM_GENERATIONS>```	

		*Note: If running program back to back, it is **highly** recommended you clear the cache files from the project with ```make clean``` before running again.*
- **B. With the provided Makefile:**
	1. ```make run-15``` for 15 city solution or ```make run-20``` for 20 city solution. 
	
		*Note: Cache cleaning is done for you with this method. Additionally, the optimal number of population members and generations is fixed.*
***
# Results:
```
> python3 main.py cities_15.txt city_milage_15.txt 1500 40 4
['cities_15.txt', 'city_milage_15.txt', '1500', '40', '4']
Generation: Initial best = -11620
Generation: 1 best = -11620
Generation: 2 best = -10990
.
.
.
Generation: 39 best = -7810
Generation: 40 best = -7810

Optimal Solution:
1 El_Paso
13 Los_Angeles
7 Seattle
3 Salt_Lake_City
2 Denver
15 Omaha
11 Kansas_City
14 Chicago
12 Cleveland
4 Buffalo
8 Boston
9 Miami
10 Birmingham
5 Memphis
6 Dallas
1 El_Paso

With a fitness of: -7810
```
*Note: The fitness appears as negative due to the fact our algorithm is using a maximization function.*