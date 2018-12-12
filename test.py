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

fitnessArray = []

for i in range(MAXPOP):
    gamePlay = Game()
    gamePlay.play(populationArray[i].instructions)
    fitnessArray.append(gamePlay.fitness)


print(fitnessArray)


mostFit = 0

for i in range(len(fitnessArray)):
    if(fitnessArray[i] >= fitnessArray[mostFit]):
        mostFit = i

print (mostFit)

gamePlay.play(populationArray[mostFit].instructions)
gamePlay.display_game()


#x = gf.populationMF(populationArray)
#print(x)


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
