from gaft import GAEngine
from gaft.components import BinaryIndividual
from gaft.components import Population
from gaft.operators import TournamentSelection
from gaft.operators import UniformCrossover
from gaft.operators import FlipBitBigMutation

import math

# Built-in best fitness analysis.
from gaft.analysis.fitness_store import FitnessStore
from gaft.analysis.console_output import ConsoleOutput

# Define population.
indv_template = BinaryIndividual(ranges=[(-2, 2), (-2, 2)], eps=0.001)
population = Population(indv_template=indv_template, size=50).init()

# Create genetic operators.
#selection = RouletteWheelSelection()
selection = TournamentSelection()
crossover = UniformCrossover(pc=0.8, pe=0.5)
mutation = FlipBitBigMutation(pm=0.1, pbm=0.55, alpha=0.6)

# Create genetic algorithm engine.
# Here we pass all built-in analysis to engine constructor.
engine = GAEngine(population=population, selection=selection,
                  crossover=crossover, mutation=mutation,
                  analysis=[ConsoleOutput, FitnessStore])


# Define fitness function.
@engine.fitness_register
@engine.minimize
def fitness(indv):
    x, y = indv.solution
    return (1-x)* (1-x) + 100 * (y-x*x) * (y-x*x)

engine.run(ng=150)
