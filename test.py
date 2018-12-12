import random
import geneticFunctions as gf
#Define max population
MAXPOP = 15
#Define mutation rate
MUTATIONRATE = 0.1
#Array of instances of run
populationArray = []

populationArray = gf.initializePopulation(MAXPOP)

print(populationArray[5].instructions, '\n')

gf.populationMutation(populationArray, MUTATIONRATE)

print(populationArray[5].instructions, '\n')


#parent1 = populationArray[5]
#parent2 = populationArray[6]


#print (parent1.instructions, '\n')
#print (parent2.instructions, '\n')

#child = gf.singleCrossover(parent1, parent2)

#print (child.instructions, '\n')
<<<<<<< HEAD









#for i in range(MAXPOP):
#    print(populationArray[i].instructions, '\n')
=======
>>>>>>> 07cdd02c50f54f8c83b9b4d5dbe53b953f490cd7
