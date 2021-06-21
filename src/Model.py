from src.Generation import *
from src.Hyperparameters import *
from src.Exceptions import ArgumentRangeError, ArgumentTypeError

class Model:
    """The 'agent' in the graph environment."""
    GENERATIONS = []

    @staticmethod
    def checkArguments(args:list):
        """Ensures arguments provided by user are of valid type and are within range."""
        try:
            args[0] = int(args[0])
            args[1] = int(args[1])
        except ValueError as exc:
            raise ArgumentTypeError() from exc

        if args[0] <= 0 or args[1] <= 0:
            raise ArgumentRangeError(args)
        else:
            return args[0], args[1]

    @classmethod
    def initialize(cls, info:list):
        """Initializes the model with CLI arguments defined by the user."""
        HYPER.POPULATION_SIZE, HYPER.NUM_GENERATIONS = cls.checkArguments(info)
    
    @classmethod
    def simulate(cls):
        """Simulates generational evolution of genetic variability to discover shortest path."""
        for gen in range(0, HYPER.NUM_GENERATIONS + 1):
            if gen == 0:
                cls.GENERATIONS.append(Generation("Initial", None))
                cls.GENERATIONS[gen].showBest()
            else:
                cls.GENERATIONS.append(Generation(str(gen), cls.GENERATIONS[gen-1].population))
                cls.GENERATIONS[gen].showBest()

    @classmethod
    def showOptimalPath(cls):
        """Prints the optimal path found by node and city. Reading direction does not matter."""
        print()
        print("The Optimal Solution is:")
        print(Environment.STARTFINISH.getCode() + " " + Environment.STARTFINISH.getName())
        for vertex in cls.GENERATIONS[-1:][0].population[0].gene:
            print(vertex.getCode() + " " + vertex.getName())
        print(Environment.STARTFINISH.getCode() + " " + Environment.STARTFINISH.getName())
        print()
        print("With a fitness of: " + str(cls.GENERATIONS[-1:][0].population[0].fitness))