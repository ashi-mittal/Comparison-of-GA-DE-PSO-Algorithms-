import fitnessFunction as ff
from copy import deepcopy
import random

# Function 3: Remember Global BEST in the pop;
def MemoriseGlobalBest(gBest,gBestFitness,pop):
    ##global gBest, gBestFitness
    for p in pop:
        if p.pBestFitness < gBestFitness:
            gBest = deepcopy(p.pBest)
            gBestFitness=p.pBestFitness
    return gBest,gBestFitness
            

# Function 4: Perform PSO Operation
def PSOOperation(pop,funEval,popSize,w,c1,c2,vLB,vUB,gBest,gBestFitness):
    ##global funEval
    #print("h=",gBestFitness)
    for i in range(0,popSize):
        for j in range(0,ff.D):

            # Choose two random numbers
            r1=random.random()
            r2=random.random()
            
            ##if (i%10==0,j==1):
                ##print("in pso : i ",i," j ",j)

            # Velocity update
            pop[i].velocity[j] = w * pop[i].velocity[j] + \
                                c1 * r1 * (pop[i].pBest[j] - pop[i].particle[j]) + \
                                c2 * r2 * (gBest[j] - pop[i].particle[j])

            if pop[i].velocity[j] < vLB:
                pop[i].velocity[j] = random.uniform(vLB, vUB)
                                                    
            if pop[i].velocity[j] > vUB:
                pop[i].velocity[j] = random.uniform(vLB, vUB)

            # Particle update
            pop[i].particle[j] = round(pop[i].particle[j] + pop[i].velocity[j],2)

            if pop[i].particle[j] < ff.LB:
                pop[i].particle[j] =  round(random.uniform(ff.LB, ff.UB),2)

            if pop[i].particle[j] > ff.UB:
                pop[i].particle[j] =  round(random.uniform(ff.LB, ff.UB),2)


        pop[i].particleFitness = round(ff.FitnessFunction(pop[i].particle),2)
        funEval = funEval + 1

        # Select between particle and pBest
        if pop[i].particleFitness <= pop[i].pBestFitness:
            pop[i].pBest=pop[i].particle
            pop[i].pBestFitness=pop[i].particleFitness

    for p in pop:
        #print(p.pBestFitness)
        if p.pBestFitness < gBestFitness:
            gBest = deepcopy(p.pBest)
            gBestFitness=p.pBestFitness
            #print("m = ",gBestFitness)
    return gBest,gBestFitness


def Calling(pop,funEval,popSize,w,c1,c2,vLB,vUB,gBest,gBestFitness,iterations,maxFunEval):    
    for i in range(0,iterations):
        ##print(gBestFitness)
        gBest,gBestFitness=PSOOperation(pop,funEval,popSize,w,c1,c2,vLB,vUB,gBest,gBestFitness)
        #MemoriseGlobalBest(gBest,gBestFitness,pop)
	
        if funEval >=maxFunEval:
            break

        ##print("here2")
        
        #if i%10==0:
            #print ("I:",i,"\t Fitness:", gBestFitness)
    return gBestFitness
