import random
from copy import deepcopy
import fitnessFunction as ff # Fitness Function and Parameters

# Function 3: Remember Global BEST in the pop;
def MemoriseGlobalBest(pop,bestFitness,bestChromosome):
    #global bestFitness,bestChromosome
    for p in pop:
        if p.fitness < bestFitness:
            bestFitness=p.fitness
            bestChromosome = deepcopy(p.chromosome)
    return bestFitness,bestChromosome


# Function 4: Perform DE Operation
def DEOperation(funEval,popSize,pop,CR,F):
    #global funEval
    for i in range(0,popSize):

        # Choose three random indices
        i1,i2,i3=random.sample(range(0,popSize), 3)

	# Iterate for every Dimension
        newChild=[]
        for j in range(ff.D):
            if (random.random() <= CR):
                k = pop[i1].chromosome[j] + \
                    F * (pop[i2].chromosome[j] - pop[i3].chromosome[j])

                # If new dimention cross LB
                if k < ff.LB:
                    k = random.uniform(ff.LB,ff.UB)

                # If new dimention cross LB
                if k > ff.UB:
                    k = random.uniform(ff.LB,ff.UB)
                
                newChild.append(round(k,2))
                
            else:
                newChild.append(pop[i].chromosome[j])

	# Child Fitness
        newChildFitness=ff.FitnessFunction(newChild)
        funEval = funEval + 1
		
        # Select between parent and child
        if newChildFitness < pop[i].fitness:
            pop[i].fitness=newChildFitness
            pop[i].chromosome=newChild
                

def calling(funEval,CR,F,popSize,pop,iterations,maxFunEval,bestFitness,bestChromosome):
    for i in range(0,iterations):
        DEOperation(funEval,popSize,pop,CR,F)
        bestFitness,bestChromosome=MemoriseGlobalBest(pop,bestFitness,bestChromosome)
            
        if funEval >=maxFunEval:
            break

        #if i%50==0:
            #print ("I:",i,"\t Fitness:", bestFitness)
            
    #print ("I:",i+1,"\t Fitness:", bestFitness)

    return bestFitness
