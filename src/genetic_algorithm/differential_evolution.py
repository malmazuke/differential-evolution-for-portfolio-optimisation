'''
Created on Aug 11, 2013

@author: Mark Feaver
@contact: mark.feaver@gmail.com
@summary: A Python implementation of Differential Evolution, using the DE/rand/1/bin scheme
'''
population = []

def init_population():
    global population
    """ Intialise the population"""
    print "Initialising Population..."

def evolve(select_type="rand", num_diff_vectors=1, crossover_scheme="bin"):
    """ Evolve the population using Differential Evolution.
    
    Keyword arguments:
    select_type -- the base-vector selection method, either 'rand' or 'best' (default 'rand')
    num_diff_vectors -- the number of difference vectors to use (default '1')
    crossover_scheme -- the crossover scheme to use, either 'bin' for experiments based on independent binomial experiments, or 'exp' for exponential crossover (default 'bin') 
    """
    print "Evolving Population..."
    
def main():
    print "Hello DE!"
    init_population()
    evolve()
    
if __name__ == '__main__':
    main()