class Vertex:
    """Synonymous with 'city'. Stores the name and code of a particular city."""
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def getCode(self):
        return(str(self.code))
    
    def getName(self):
        return(str(self.name))

class Edge:
    """Synonymous with 'path'. Encodes connections between graph verticies."""
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance

class Environment:
    """Compilation of graph problem and their features."""
    CITIES = None
    MILAGE = None
    STARTFINISH = None

    @classmethod
    def initialize(cls, info:list):
        """Initializes the graph environment into verticies and edges with city and milage data text files."""
        cls.CITIES = initVerticies(info[0])
        cls.MILAGE = initEdges(info[1])
        cls.STARTFINISH = cls.CITIES.pop(0) # Take the first city off as it is starting point and end point

def initVerticies(filename):
    """Converts cities from given text file into verticies stored in an array."""
    arr = []
    num = 0
    with open('data/' + str(filename)) as cities_file:
        lines = cities_file.readlines()
        for line in lines:
            num = num + 1
            arr.append(Vertex(num, line.strip()))
    cities_file.close()
    return(arr)

def initEdges(filename):
    """Converts cities from given text file into edges stored in an array."""
    arr = []
    with open('data/' + str(filename)) as mileage_file:
        info = mileage_file.readlines()

        for line in info:
            temp = line.split()
            arr.append(Edge(temp[0], temp[1], int(temp[2])))

    mileage_file.close()
    return(arr)
# ------------------------------------------------------------------------------