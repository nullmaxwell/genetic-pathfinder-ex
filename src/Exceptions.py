class ArgumentTypeError(Exception):
    """Exception raised for errant argument types."""
    def __init__(self, value):
        self.value = value
        self.message = "Provided argument(s) inavlid. Expected: main.py <city_file> <milage_file> <POPULATION_SIZE> <NUM_GENERATIONS>"
        super().__init__(self.message)

class ArgumentRangeError(Exception):
    """Exception raised for when either POPULATION_SIZE or NUM_GENERATIONS is out of range of 1 to inf."""
    def __init__(self, value):
        self.value = value
        self.message = "Provided argument inavlid. Number POPULATION_SIZE and NUM_GENERATIONS must be grater than 0."
        super().__init__(self.message)