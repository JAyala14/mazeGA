import random
import geneticFunctions as gf
from pacman import Game
#Define max population
MAXPOP = 15
#Define mutation rate
MUTATIONRATE = 0.1
#Array of instances of run
populationArray = []

populationArray = gf.initializePopulation(MAXPOP)

test_instructions = populationArray[4]


for i in range(MAXPOP):
    gamePlay = Game(populationArray[i])
    gamePlay.play(populationArray[i].instructions)

x = gf.populationMF(populationArray)
print(x)


#gf.sortFit(populationArray)

    #gamePlay.showLAST(populationArray[i].instructions)



#populationArray = gf.initializePopulation(MAXPOP)
#print(populationArray[5].instructions, '\n')
#gf.populationMutation(populationArray, MUTATIONRATE)
#print(populationArray[5].instructions, '\n')

#parent1 = populationArray[5]
#parent2 = populationArray[6]

#print (parent1.instructions, '\n')
#print (parent2.instructions, '\n')
#child = gf.singleCrossover(parent1, parent2)
#print (child.instructions, '\n')
