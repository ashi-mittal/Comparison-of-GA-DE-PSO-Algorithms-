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


# Function 4: Perform Crossover Operation
def Crossover(funEval,popSize,CR,pop):
    #global funEval
    for i in range(0,popSize):

        if (random.random() <= CR):

            # Choose two random indices
            i1,i2=random.sample(range(0,popSize), 2)

            # Parents
            p1=deepcopy(pop[i1])
            p2=deepcopy(pop[i2])

            # Choose a crossover point 
            pt = random.randint(1,ff.D-2)

            # Generate new childs 
            c1=p1.chromosome[0:pt] + p2.chromosome[pt:]
            c2=p2.chromosome[0:pt] + p1.chromosome[pt:]

            # Get the fitness of childs 
            c1Fitness=ff.FitnessFunction(c1)
            funEval = funEval + 1
            c2Fitness=ff.FitnessFunction(c2)
            funEval = funEval + 1

            # Select between parent and child
            if c1Fitness < p1.fitness:
                pop[i1].fitness=c1Fitness
                pop[i1].chromosome=c1
                
            if c2Fitness < p2.fitness:
                pop[i2].fitness=c2Fitness
                pop[i2].chromosome=c2


# Function 5: Perform Mutation Operation
def Mutation(pop,funEval,popSize,MR):
    #global UB, LB, funEval
    for i in range(0,popSize):

        if (random.random() <= MR):
            
            # Choose random index
            r=random.randint(0,popSize-1)

            # Choose a parent
            p=deepcopy(pop[r])

            # Choose mutation point 
            pt = random.randint(0,ff.D-1)    
            
            # Generate new childs
            c=deepcopy(p.chromosome)

            # Mutation
            c[pt] = round(random.uniform(ff.LB,ff.UB),2)

            #Get the fitness of childs
            cFitness=ff.FitnessFunction(c)
            funEval = funEval + 1
            # Select between parent and child
            if cFitness < p.fitness:
                pop[r].fitness=cFitness
                pop[r].chromosome=c

def calling(maxFunEval,pop,funEval,iterations,CR,MR,popSize,bestFitness,bestChromosome):
    for i in range(0,iterations):
        Crossover(funEval,popSize,CR,pop)
        Mutation(pop,funEval,popSize,MR)
        bestFitness,bestChromosome=MemoriseGlobalBest(pop,bestFitness,bestChromosome)
            
        if funEval >=maxFunEval:
            break

        #if i%50==0:
            #print ("I:",i,"\t Fitness:", bestFitness)
            
    #print ("I:",i+1,"\t Fitness:", bestFitness)

    return bestFitness
    
