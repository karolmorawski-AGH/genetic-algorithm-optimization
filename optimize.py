from gaft import GAEngine
from gaft.components import BinaryIndividual
from gaft.components import Population
from gaft.operators import TournamentSelection, ExponentialRankingSelection, LinearRankingSelection, RouletteWheelSelection
from gaft.operators import UniformCrossover
from gaft.operators import FlipBitBigMutation

# Rosenbrock function
# Expected solution: [1,1] = 0

# Function boundaries
XB = (-10, 10)
YB = (-10, 10)
# Decrete precision of binary sequence
EPS = 0.0001

# Population size
POPULATION_SIZE = 250

# Selection method
SELECTION = RouletteWheelSelection()

# Crossover method
# pc: probability of crossover (0,1)
PC = 0.8
# pe: probability of gene exchange (0,1)
PE = 0.5

# Mutation
# pm: probability of mutation (0, 1)
PM = 0.05
# pbm: probability of big mutation (5 times bigger than pbm)
PBM = PM * 5
# alpha: intensive factor (0.5, 1)
ALPHA = 0.6

# Run
# ng: Evolution iteration steps (generations number)
NG = 150


# Built-in best fitness analysis.

from gaft.analysis.fitness_store import FitnessStore
from gaft.analysis.console_output import ConsoleOutput

# Define population.


indv_template = BinaryIndividual(ranges=[XB, YB], eps=EPS)
population = Population(indv_template=indv_template, size=POPULATION_SIZE).init()

# Create genetic operators.
selection = SELECTION
crossover = UniformCrossover(pc=PC, pe=PE)
mutation = FlipBitBigMutation(pm=PM, pbm=PBM, alpha=ALPHA)

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
    return (1 - x) * (1 - x) + 100 * (y - x * x) * (y - x * x)


engine.run(ng=NG)
