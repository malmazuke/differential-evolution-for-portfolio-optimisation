'''
Created on Aug 11, 2013

@author: Mark Feaver
@contact: mark.feaver@gmail.com
@summary: A Python implementation of Differential Evolution, using the DE/rand/1/bin scheme
'''

from objective_function.SchwefelFunction import schwefel_function
from selection_function.RandomSelector import rand_selector
import random

DEF_POP_SIZE=-1
DEF_CR_RATE=0.4
DEF_SCALE_FACTOR=0.4
DEF_SELECTOR=rand_selector
DEF_NUM_DIFF_VECTORS=1
DEF_CR_SCHEME="bin"
DEF_OBJ_FUNCT=schwefel_function

class DifferentialEvolver:
    _population = []
    _num_dimensions = 0
    _pop_size = DEF_POP_SIZE
    _cr_rate = DEF_CR_RATE
    _scale_factor = DEF_SCALE_FACTOR
    _selector = DEF_SELECTOR
    _num_diff_vectors = DEF_NUM_DIFF_VECTORS
    _cr_scheme = DEF_CR_SCHEME
    _obj_function = DEF_OBJ_FUNCT
    _scores = []
    
    def init_population(self):
        """ Initialise the population. """
        
        for i in xrange(self._pop_size):
            # Create a random vector/member of the population
            curr = []
            for x in xrange(self._num_dimensions):
                # Create a random value
                curr.append(random.random())
            self._population.append(curr)
        
    def calc_fitness(self):
        """ Calculate the fitness of the current population, using the objective function. """
        
        for x in xrange(self._pop_size):
            curr = self._population[x]
            self._scores[x] = self._obj_function(curr)
    
    def evolve(self):
        """ Evolve the population using Differential Evolution. """
        
        print "Evolving Population..."
        self.calc_fitness()
        
    def __init__(self, num_dimensions, pop_size=DEF_POP_SIZE, crossover_rate=DEF_POP_SIZE, scaling_factor=DEF_SCALE_FACTOR, selector=DEF_SELECTOR, num_diff_vectors=DEF_NUM_DIFF_VECTORS, crossover_scheme=DEF_CR_SCHEME, obj_function=DEF_OBJ_FUNCT):
        """ Initialise the DE
        
        Keyword arguments:
        num_dimensions -- the number of dimensions in each member of the population
        pop_size -- the number in the population (default '10 * num_dimensions')
        crossover_rate -- the chance of crossover (default '0.4')
        scaling_factor -- the scaling factor (default '0.4')
        selector -- the base-vector selection method, either 'rand_selector' or 'best_selector' (default 'rand_selector')
        num_diff_vectors -- the number of difference vectors to use (default '1')
        crossover_scheme -- the crossover scheme to use, either 'bin' for experiments based on independent binomial experiments, or 'exp' for exponential crossover (default 'bin')
        obj_function -- a function that takes a vector, and returns a fitness rating (default 'schwefel_function')
        """
        
        self._num_dimensions = num_dimensions
        self._pop_size =  num_dimensions * 10 if (pop_size == DEF_POP_SIZE) else pop_size
        self._cr_rate = crossover_rate
        self._scale_factor = scaling_factor
        self._selector = selector
        self._num_diff_vectors = num_diff_vectors
        self._cr_scheme = crossover_scheme
        self._obj_function = obj_function
        
        # initialise the scores to 0
        self._scores = []
        for x in xrange(self._pop_size):
            self._scores.append(0)
        
    def start(self):
        """ Start the DE process """
        self.init_population()
        self.evolve()
    
if __name__ == '__main__':
    evolver = DifferentialEvolver(20)
    evolver.start()