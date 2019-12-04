import func_min_ga as ga
import benchmark_functions as bf
import numpy as np
import random

d_func = bf.rosen
d_fitness = ga.fitness_rosen

# Initialization
# Defining number of chromosomes in population

CHROMOSOME_LENGTH = 2
POPULATION_SIZE = 30
NUM_ERAS = 50
X_PROB = 0.25
M_PROB = 0.01

# Generating random values of genes x1, x2 for those chromosomes
# For simplicity sake all numbers are integers
chromosome = []

i = 0
while i < POPULATION_SIZE:
    chromosome.append(ga.generate_chromosomes(CHROMOSOME_LENGTH, -10, 10))
    i += 1

chromosomenp = np.array(chromosome)

# Evaluation
# Computing objective function value for given chromosomes
fvalue = []

i = 0
while i < POPULATION_SIZE:
    fvalue.append(d_func(chromosomenp[i]))
    i += 1

# Selection
# Applying fitness function to compute fitness of each chromosome
fitness = []

i = 0
while i < POPULATION_SIZE:
    fitness.append(d_fitness(fvalue[i]))
    i += 1

# summed fitness functions values
total = sum(fitness)

# Then probability for each chromosomes is formulated:
# probability[i] = fitness[i]/TOTAL
probability = []

# Roulette wheel selection
i = 0
previous_probability = 0.0
while i < POPULATION_SIZE:
    probability.append(previous_probability + fitness[i]/total)
    previous_probability = probability[i]
    #if fitness[i]/total > SELECT_TRESHOLD:
    #    print("Chromosome " + (str)(i) + " selected for next population")
    i += 1

# Randomly selecting individual
selection_treshold = random.random()
i = 0
while i < POPULATION_SIZE:
    if selection_treshold > probability[i]:
        print("Chromosome " + (str)(i) + " selected for next population")
    i += 1


# TODO
# Reproduction - create a new population from old population
# Crossover - crossover on new population
# Mutation - mutation on new population

# TODO
# dict(num_eras = 100, population_size = 40, chromosome_length = 4, crossover_probability = 0.35, mutation_probability = 0.04)


