'''
Created on Aug 11, 2013

@author: Mark Feaver
@contact: mark.feaver@gmail.com
@summary: A Python implementation of Differential Evolution, using the DE/rand/1/bin scheme
'''
DEF_POP_SIZE=50
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
        
    def calc_fitness(self):
        """ Calculates the fitness of the current population """
    
    def evolve(self, select_type="rand", num_diff_vectors=1, crossover_scheme="bin"):
        """ Evolve the population using Differential Evolution.
        
        Keyword arguments:
        select_type -- the base-vector selection method, either 'rand' or 'best' (default 'rand')
        num_diff_vectors -- the number of difference vectors to use (default '1')
        crossover_scheme -- the crossover scheme to use, either 'bin' for experiments based on independent binomial experiments, or 'exp' for exponential crossover (default 'bin') 
        """
        print "Evolving Population..."
        
    def start(self, pop_size=DEF_POP_SIZE, crossover_rate=DEF_POP_SIZE, scaling_factor=DEF_SCALE_FACTOR):
        self._pop_size = pop_size
        self._cr_rate = crossover_rate
        self._scale_factor = scaling_factor
        
        self.init_population()
        self.evolve()
    
if __name__ == '__main__':
    evolver = DifferentialEvolver()
    evolver.start()