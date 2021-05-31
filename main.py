# Traveling Salesman
#
# Author: Maxwell Rahmani
# Date: September  18, 2020
# Version: 1.0.0
# Python Version: 2.7.16
# Description:
# ------------------------------------------------------------------------------

# Imports
import sys
from src.Model import *
from src.Environment import *
from src.Hyperparameters import *

def main(argv):
    print(argv)

    Environment.initialize(argv[:2])
    Model.initialize(argv[2:])
    Model.simulate()
    Model.showOptimalPath()

if __name__ == '__main__':
    main(sys.argv[1:])
