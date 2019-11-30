import numpy as np
from scipy.optimize import Bounds
from scipy.optimize import minimize
import math

# Ackley function formula
# Global minimum f(0,0)=0
def ackley(x,y):
    return -20*math.exp(-0.2*math.sqrt(0.5*(x*x+y*y))) - math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(math.pi*2*y)))  + math.e + 20

# Search domain
xbounds = [-5,5]
ybounds = [-5,5]
bounds = Bounds(xbounds, ybounds)
