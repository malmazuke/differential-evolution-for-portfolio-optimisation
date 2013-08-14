'''
Created on Aug 11, 2013

@author: Mark Feaver
@contact: mark.feaver@gmail.com
@summary: A Python implementation of Differential Evolution, using the DE/rand/1/bin scheme
'''

import objective_function.SchwefelFunction
from objective_function.SchwefelFunction import schwefel_function

DEF_POP_SIZE=-1
DEF_CR_RATE=0.4
DEF_SCALE_FACTOR=0.4

class DifferentialEvolver:
    _pop_size = DEF_POP_SIZE
    _cr_rate = DEF_CR_RATE
    _scale_factor = DEF_SCALE_FACTOR
    _population = []
    
    def init_population(self):
        global population
        """ Intialise the population"""
        print "Initialising Population..."
        
    def calc_fitness(self, obj_function):
        """ Calculates the fitness of the current population , using the objective function
        
        Keyword arguments:
        obj_function -- a function that takes a vector, and returns a fitness rating
        """
    
    def evolve(self, select_type="rand", num_diff_vectors=1, crossover_scheme="bin"):
        """ Evolve the population using Differential Evolution.
        
        Keyword arguments:
        select_type -- the base-vector selection method, either 'rand' or 'best' (default 'rand')
        num_diff_vectors -- the number of difference vectors to use (default '1')
        crossover_scheme -- the crossover scheme to use, either 'bin' for experiments based on independent binomial experiments, or 'exp' for exponential crossover (default 'bin') 
        """
        print "Evolving Population..."
        
        self.calc_fitness(schwefel_function)
        
    def start(self, num_dimensions, pop_size=DEF_POP_SIZE, crossover_rate=DEF_POP_SIZE, scaling_factor=DEF_SCALE_FACTOR):
        """ Start the DE process
        
        Keyword arguments:
        num_dimensions -- the number of dimensions in each member of the population
        pop_size -- the number in the population (default '10 * num_dimensions')
        crossover_rate -- the chance of crossover (default '0.4')
        scaling_factor -- the scaling factor (default '0.4')
        """
        self._pop_size =  num_dimensions * 10 if (pop_size == DEF_POP_SIZE) else pop_size
        self._cr_rate = crossover_rate
        self._scale_factor = scaling_factor
        
        self.init_population()
        self.evolve()
    
if __name__ == '__main__':
    evolver = DifferentialEvolver()
    evolver.start()