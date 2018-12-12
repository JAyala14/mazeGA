#Genetic Algorithm Functions
import random
from geneticAlgorithm import run
from pacman import Game

#Initializing population
def initializePopulation(population):
    randomPopulation = []
    for i in range(population):
        randomPopulation.append(run())

    return randomPopulation

#Get index of most fit
def populationMF(population):
    mostFIT = 0

    for i in range(len(population)):

        if(population[i].fitness >= population[i-1].fitness):
            fitIndex = i
    return fitIndex

#Sort fittest to least fit
#def sortFit(population):

#    populationSize = len(population)
#    for i in range(populationSize):
        #Sorts population from most fit to least
#        population.sort(key = population[i].fitness)


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
def populationCrossover(population):

    temp = 4
    newPopulation = []
    populationSize = len(population)

    population = sorted(population, key=population.fitness, reverse=True) #sorts population by fitenss in largest to smallest

    for i in range(10):
        if (i < 5):
            newPopulation[i] = population[i]
        else:
            for j in range(temp):
                newPopulation.append(singleCrossover(population[i-5], population[j+5-temp]))        #crosses over first 5 fittest parents
            temp-=1

    newMutation = 0.3 - (newPopulation.generation*.05)              #Decreases 5% every generation
    newPopulation = populationMutation(newPopulation, newMutation)  #mutates new population at new mutation rate

    return newPopulation


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
