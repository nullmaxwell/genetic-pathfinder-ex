import random
from src.Environment import Environment
from src.Hyperparameters import *

class Chromosome:
    """Singular gene and its fitness."""
    def __init__(self, gene):
        if gene == None:
            self.gene = self.generateSequence()
        else:
            self.gene = gene
        self.fitness = self.calculateFitness()

    def generateSequence(self):
        """Generates a possible solution of problem by shuffling an array of the available verticies."""
        random.shuffle(Environment.CITIES)
        cp = Environment.CITIES[:]
        return(cp)

    def calculateFitness(self):
        """Calculates the distance of travel path provided by the chromosome's gene. Note: Negative int returned."""
        success = False
        counter = 0
        distance = 0

        while(success == False):
            try:
                allele_a = self.gene[counter].name
                allele_b = self.gene[counter + 1].name

                for Edge in Environment.MILAGE:
                    if(Edge.source == allele_a and Edge.destination == allele_b):
                        distance += Edge.distance
                counter += 1
            except:
                success = True
                continue
        
        # First to second node.
        for Edge in Environment.MILAGE:
            if(Edge.source == Environment.STARTFINISH.name and Edge.destination == self.gene[0].name):
                distance += Edge.distance

        # Last to first node.
        for Edge in Environment.MILAGE:
            if(Edge.source == Environment.STARTFINISH.name and Edge.destination == self.gene[len(self.gene)-1].name):
                distance += Edge.distance

        return(distance * (-1))