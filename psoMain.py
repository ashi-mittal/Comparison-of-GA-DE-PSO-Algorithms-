#-------------------------------------------------------------
#               Particle Swarm Optimization (PSO)
#-------------------------------------------------------------
# To solve optimization problem (minimization) using PSO.
#-------------------------------------------------------------
# Python version used: 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------
import random
import time
from copy import deepcopy
import fitnessFunction as ff # Fitness Function and Parameters
import pso
import math

startTime = time.time()
arr = []
#-------------------------------------------------------------
# Step 2: Parameters
#-------------------------------------------------------------

# 2.1 PSO Parameters
algoName    = "PSOBasic"# Algo Name
c1	    = 1.5       # Acceleration constant
c2	    = 1.5       # Acceleration constant
w	    = 0.8       # Inertia weight
vLB         = -1        # Velocity Lower Bound
vUB         = 1         # Velocity Upper Bound

# 2.2 Global Parameters
iterations  = 50       # Number of iterations
popSize     = 10       # Population Size(i.e Number of Chromosomes)
pop         = []        # Store Population with Fitness
maxFunEval  = 100000    # Maximum allowable function evaluations
funEval	    = 0		# Count function evaluations
gBest       = []        # Rember Global Best chromosome
gBestFitness = []       # Rember fitness of Global Best chromosome


# 2.3 Result Saving Parameters
##resultFileName="result"+algoName+".csv"


# 2.4 Stores Particle, ParticleFitness, Velocity, PBest,PBestFitness collectively;
class Individual:
    def __init__(self, P, PF, V, PB, PBF):
        self.particle=P
        self.particleFitness=PF
        self.velocity=V
        self.pBest=PB
        self.pBestFitness=PBF


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
        particle=[]
        velocity=[]
        for j in range(0,ff.D):
            particle.append(round(random.uniform(ff.LB,ff.UB),2))
            velocity.append(round(random.uniform(vLB,vUB),2))
        
        particleFitness = round(ff.FitnessFunction(particle),2)
        funEval = funEval + 1
        newIndividual = Individual(particle, particleFitness, velocity, deepcopy(particle), particleFitness)
        pop.append(newIndividual)

#-------------------------------------------------------------
# Step 4: Start Program
#-------------------------------------------------------------
##pso.pso1(gBest,gBestFitness,pop,funEval,popSize,w,c1,c2,vLB,vUB)

#print("here")
for u in range(0,5):
    Init()
    #for k in range(1,100):
        #pop[k].particle = (pop[k].particle)
    gBest=pop[0].pBest
    gBestFitness=pop[0].pBestFitness
    pso.MemoriseGlobalBest(gBest,gBestFitness,pop)
    #print("here1")
    #print("g=",gBestFitness)
    #print(gBest)

    a=pso.Calling(pop,funEval,popSize,w,c1,c2,vLB,vUB,gBest,gBestFitness,iterations,maxFunEval)
    
# Saving Result
    ##fp=open(resultFileName,"w");
    ##fp.write("Iteration,Fitness,Chromosomes\n")

# Running till number of iterations
    
            ##fp.write(str(i) + "," + str(gBestFitness) + "," + str(gBest) + "\n")

    ##print ("I:",i+1,"\t Fitness:", gBestFitness)
    ##fp.write(str(i+1) + "," + str(gBestFitness) + "," + str(gBest))
    ##fp.close()

    ##print ("Done")
    ##print ("BestFitness:(U:",u,")", gBestFitness)

    ##funEval=0

    ##gBest=pop[0].pBest
    ##gBestFitness=pop[0].pBestFitness
    ##MemoriseGlobalBest()
    ##arr.append(gBestFitness)
    ##print ("Best particle:", gBest)
    ##print ("Total Function funEval: ",funEval)
    ##print ("Result is saved in", resultFileName)
    ##print ("Total Time Taken: ", round(time.time() - startTime,2), " sec\n")

    #print ("returned=",a)
    ##print("finished ",u)
    arr.append(a)

print(arr)

mean=0
for j in range(0,5):
    mean=mean+arr[j]
    #print(mean)
mean = mean / 5
print("M=",mean)

var=0
for j in range(0,5):
    var = var + (mean-arr[j] * mean-arr[j])
var = var/5
print("V=",var)
sd=var**0.5
print("SD=",sd)

f=open("Results.txt","a+")
f.write("\nPSO\n")
f.write("Mean = " + str(mean))
f.write("\nSD = " + str(sd))
f.close()
