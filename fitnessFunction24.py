import math as mt

#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2   # Problem Dimension
LB      = -20  # Set Size Lower Bound
UB      = 20  # Set Size Upper Bound
Name	= "decker-aarts"

#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------
def FitnessFunction (x):
		return (10**5)*x[0]*x[0]+x[1]*x[1]+(x[0]*x[0]+x[1]*x[1])*(x[0]*x[0]+x[1]*x[1])+(10.0**-5)*(x[0]*x[0]+x[1]*x[1])**4














