#Genetic Algorithm Functions
import random
from geneticAlgorithm import run

#Initializing population
def initializePopulation(population):
    randomPopulation = []

    for i in range(population):
        randomPopulation.append(run())

    return randomPopulation

#Sort fittest to least fit
#def sortFit(population):

    #Sorts population from most fit to least


#Single Crossover between two parents
def singleCrossover(parent1,parent2):

    child = run()

    for i in range(41):
        geneDecision = random.randint(0,1)
        #Parent1 Gene
        if(geneDecision == 0):
            child.instructions[i] = parent1.instructions[i]
        #Parent2 Gene
        else:
            child.instructions[i] = parent2.instructions[i]

    return child

#Crossover Functions
#def populationCrossover(population):

    #newPopulation = []
    #populationSize = len(population)

    #for i in range(populationSize):

        #Sort from most fit to least fit?

    #return newPopulation


#Mutate single gene
def singleMutate(mutationRate):

    val = random.uniform(0,1)
    if(val <= mutationRate):
        return True

    else:
        return False

#Mutates population Function
def populationMutation(population, mutationRate):

    populationSize = len(population)

    for i in range(populationSize):

        for j in range(40):

            if(singleMutate(mutationRate) == True):
                population[i].instructions[j] = random.randint(0,3)
