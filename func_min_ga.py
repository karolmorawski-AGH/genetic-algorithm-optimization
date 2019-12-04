from random import seed
from random import randint
import numpy as np


# Generates random chromosomes (n sized arrays)
def generate_chromosomes(dimensions, sdmin, sdmax):
    chromosome = [None] * dimensions

    i = 0
    while i < dimensions:
        chromosome[i] = randint(sdmin, sdmax)
        i += 1
    return chromosome

def fitness_rosen(x):
    return 1./x
