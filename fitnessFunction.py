import math as mt
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 20   # Problem Dimension
LB      = -10   # Set Size Lower Bound
UB      = 10   # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------
def FitnessFunction (x):
		sum = 0.0
		for i in range(D):
			sum+= (mt.sin(5*mt.pi*x[i]))**6
		return (-1.0/D)*sum















