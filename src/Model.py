from src.Generation import *
from src.Hyperparameters import *
from src.Exceptions import ArgumentRangeError, ArgumentTypeError

class Model:
    """The 'agent' in the graph environment."""
    GENERATIONS = []

    @classmethod
    def checkArguments(self, args:list):
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
    def initialize(self, info:list):
        """Initializes the model with CLI arguments defined by the user."""
        HYPER.POPULATION_SIZE, HYPER.NUM_GENERATIONS = self.checkArguments(info)
    
    @classmethod
    def simulate(self):
        """Simulates generational evolution of genetic variability to discover shortest path."""
        for gen in range(0, HYPER.NUM_GENERATIONS + 1):
            if gen == 0:
                Model.GENERATIONS.append(Generation("Initial", None))
                Model.GENERATIONS[gen].showBest()
            else:
                Model.GENERATIONS.append(Generation(str(gen), Model.GENERATIONS[gen-1].population))
                Model.GENERATIONS[gen].showBest()

    @classmethod
    def showOptimalPath(self):
        """Prints the optimal path found by node and city. Reading direction does not matter."""
        print()
        print("The Optimal Solution is:")
        print(Environment.STARTFINISH.getCode() + " " + Environment.STARTFINISH.getName())
        for vertex in Model.GENERATIONS[-1:][0].population[0].gene:
            print(vertex.getCode() + " " + vertex.getName())
        print(Environment.STARTFINISH.getCode() + " " + Environment.STARTFINISH.getName())
        print()
        print("With a fitness of: " + str(Model.GENERATIONS[-1:][0].population[0].fitness))