import random
#Player takes inputs from textfile
#Inputs:
#0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT

#Outputs: Text file with inputs to playerself.

class run:

    def __init__(self):
        self.fitness = 0
        self.instructions = []

        self.initialize()

    #Randomly initialize array of instructions
    def initialize(self):

        for i in range(40):
            randomMove = random.randint(0,3)
            self.instructions.append((randomMove))
