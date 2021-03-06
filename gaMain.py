#-------------------------------------------------------------
#               Genetic Algorithm (GA)
#-------------------------------------------------------------
# To solve optimization problem (minimization) using GA.
#-------------------------------------------------------------
# Python version used: 2.6 / 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------
import random
from copy import deepcopy
import fitnessFunction as ff # Fitness Function and Parameters
import ga


#-------------------------------------------------------------
# Step 2: Parameters
#-------------------------------------------------------------

# 2.1 GA Parameters
algoName    = "GABasic" # Algo Name
CR 	    = 0.9  	# Crossover Rate
MR 	    = 0.1       # Mutation Rate

# 2.2 Global Parameters
iterations  = 200       # Number of iterations
popSize     = 100       # Population Size(i.e Number of Chromosomes)
pop         = []        # Store Population with Fitness
maxFunEval  = 100000    # Maximum allowable function evaluations
funEval	    = 0		# Count function evaluations
bestFitness = 99999999  # Store Best Fitness Value
bestChromosome = []     # Store Best Chromosome

arr=[]

# 2.4 Stores Chromosome and its fitness collectively
class Individual:
    def __init__(self, C, F):
        self.chromosome=C
        self.fitness=F

# 2.5 Problem parameters
# Problem Parameters are defined in in fitnessFunction.py file


#-------------------------------------------------------------
# Step 3: Functions Definitions
#-------------------------------------------------------------

# Function 1: Fitness Function
# FitnessFunction is defined in fitnessFunction.py file


# Function 2: Generate Random Initial Population
def Init():
    global funEval
    for i in range (0, popSize):
        chromosome = []
        for j in range(0,ff.D):
            chromosome.append(round(random.uniform(ff.LB,ff.UB),2))
        fitness = ff.FitnessFunction(chromosome)
        funEval = funEval + 1
        newIndividual = Individual(chromosome,fitness)
        pop.append(newIndividual)

#-------------------------------------------------------------
# Step 4: Start Program
#-------------------------------------------------------------
for u in range(0,20):
    Init()
    bestChromosome=pop[0].chromosome
    bestFitness=pop[0].fitness
    #SMemoriseGlobalBest()

    a=ga.calling(maxFunEval,pop,funEval,iterations,CR,MR,popSize,bestFitness,bestChromosome)

    print("U=",u)
    #print ("Done")
    print("Returned=",a)
    #print "\nBestFitness:", bestFitness
    #print "Best chromosome:", bestChromosome

    arr.append(a)


print(arr)
mean=0
for j in range(0,20):
    mean=mean+arr[j]
    #print(mean)
mean = mean / 20
print("M=",mean)

var=0
for j in range(0,20):
    var = var + (mean-arr[j] * mean-arr[j])
var = var/20
print("V=",var)
sd=var**0.5
print("SD=",sd)

f=open("Results.txt","a+")
f.write("Fitness Function 1 :\nGA\n")
f.write("Mean = " + str(mean))
f.write("\nSD = " + str(sd))

f.close()

