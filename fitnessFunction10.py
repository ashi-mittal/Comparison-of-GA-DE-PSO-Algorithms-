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
		s=0
		p=1
		for i in range(0, D):
			s = s + abs(x[i])
		for i in range(0, D):
			p= p * abs(x[i])
		return s + p














