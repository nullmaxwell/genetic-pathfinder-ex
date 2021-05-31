import random
from src.Chromosome import *
from src.Hyperparameters import *

class Generation:
    """Named collection of a population."""
    def __init__(self, name:str, prev_population):
        if prev_population == None:
            self.name = name
            self.population = self.genesis()
        else:
            self.name = name
            self.population = self.newPopulation(prev_population)
    
    def showBest(self):
        """Prints the name and best fitness of the population."""
        print("Generation: " + self.name + " best = " + str(self.population[0].fitness))
        return

    def genesis(self):
        """Synthesizes a new population from no previous population."""
        temp = []
        for x in range(0, HYPER.POPULATION_SIZE):
            temp.append(Chromosome(None))
        temp.sort(key = chromosomeFitness, reverse = True)
        return temp
        
    def newPopulation(self, prev_pop):
        """Generates a new population based on the previous generation within the environment."""
        newPop = []
        tempSubset = []
        chro1 = None
        chro2 = None

        prev_pop.sort(key = chromosomeFitness, reverse = True)

        # Taking best 10
        for x in range(0, 9):
            newPop.append(prev_pop[x])

        # Crossing over remaining chromosomes in population
        for x in range(10, len(prev_pop)-1):

            # Taking 10 random for genetic variance
            for x in range(0, 10):
                tempSubset.append(prev_pop[random.randint(0, len(prev_pop)-1)])
            
            # Taking top 5 performers by fitness of the random 10
            tempSubset.sort(key = chromosomeFitness, reverse = True)
            tempSubset = tempSubset[:5]

            # Select 2 from the subset randomly
            chro1 = tempSubset.pop(random.randint(0,4))
            chro2 = tempSubset.pop(random.randint(0,3))

            # Commiting Crossover on the two
            newPop.append(self.crossover(chro1, chro2))

            # Reset the subset array for other loops
            tempSubset[:] = []
        newPop.sort(key = chromosomeFitness, reverse = True)
        return(newPop)

    def crossover(self, chromosome_A, chromosome_B):
        """Given two chromosomes, simulates crossing over and defines a new chromosome with the new gene and its fitness."""
        # Generate Crossover point
        crossoverPoint = random.randint(0, len(chromosome_A.gene))
        s1 = chromosome_A.gene[:crossoverPoint]
        s2 = chromosome_B.gene[crossoverPoint:]
        
        # Assembly of new gene
        newGene = s1+s2

        available = Environment.CITIES[:]

        # Rebuild gene from available verticies
        for x in range(0,len(newGene)):
            if len(available) <= 2:
                newGene[x] = available[0]
            if newGene[x] in available:
                available.remove(newGene[x])
            else:
                newGene[x] = available[random.randint(0, len(available)-1)]
                available.remove(newGene[x])

        return(Chromosome(newGene))

def chromosomeFitness(chromosome):
    """Proprietary search key used to sort by chromosome fitness."""
    return(chromosome.fitness)