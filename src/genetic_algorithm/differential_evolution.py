'''
Created on Aug 11, 2013

@author: Mark Feaver
@contact: mark.feaver@gmail.com
@summary: A Python implementation of Differential Evolution, using the DE/rand/1/bin scheme
'''

import random
from selection_function.random_selector import rand_selector
from objective_function.one_max import OneMax
from objective_function.max_av_return import MaxAverageReturn

DEF_POP_SIZE=-1
DEF_CR_RATE=0.4
DEF_SCALE_FACTOR=0.4
DEF_SELECTOR=rand_selector
DEF_NUM_DIFF_VECTORS=1
DEF_CR_SCHEME="bin"
DEF_OBJ_FUNCT=OneMax()
DEF_MAX_GENS=1000


def add_vectors(vector1, vector2):
    """ Utility function to add two vectors. Assumes that vectors are same length"""
    out_vector = []
    for x in xrange(len(vector1)):
        out_vector.append(vector1[x] + vector2[x])
    
    return out_vector
    
    
def subtract_vectors(vector1, vector2):
    """ Utility function to subtract two vectors. Assumes that vectors are same length """
    out_vector = []
    for x in xrange(len(vector1)):
        out_vector.append(vector1[x] - vector2[x])
    
    return out_vector

def multiply_vector(vector, scalar):
    """ Utility function to multiply a vector with a scalar """
    out_vector = []
    for x in xrange(len(vector)):
        out_vector.append(vector[x] * scalar)
        
    return out_vector

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
            
            # Calculate the score for the current value
            self._scores.append(self.calc_fitness(curr))
    
    def calc_fitness(self, vector):
        """ Calculate the fitness of a vector """
        
        return self._obj_function.calc_fitness(vector)
        
    def start(self):
        """ Start the DE Evolution process """
        # Generate randomly an initial population of solutions, and calculate the fitnesses/scores
        self.init_population()
        
        curr_gen = 0
        # Repeat
        while curr_gen < self._max_gens:
            # For each parent, select three solutions at random. Create one offspring (variant vector) using the DE operators.
            offspring = []
            for i in xrange(self._pop_size):
                variant = self.get_variant_vector(i)
                offspring.append(variant)
                
            # Create the trial vectors, using crossover
            for i in xrange(self._pop_size):
                trial = self.get_trial_vector(self._population[i], offspring[i])
                offspring[i] = trial
             
            # For each member of the next generation
            for i in xrange(self._pop_size):
                # Get the fitter of the two value, and its fitness value
                fittest, fitness = self._obj_function.select_fittest(self._population[i], offspring[i])
                self._population[i] = fittest
                self._scores[i] = fitness
#                 fitness_parent = self.calc_fitness(self._population[i])
#                 fitness_offspring = self.calc_fitness(offspring[i])
#                 if fitness_offspring < fitness_parent:
#                     self._scores[i] = fitness_offspring
#                     self._population[i] = offspring[i]
            
            # Until a stop condition is satisfied.
            curr_gen += 1
        
        self.print_results()
        
    def get_variant_vector(self, index):
        """  Calculate the variant vector for the parent at the given index. Uses the following formula: Vj(t + 1) = Xm(t) + F(Xk(t) - Xl(t)) """
        parent = self._population[index]
                
        pop_without_parent = list(self._population) # Make sure that we don't select the parent vector
        pop_without_parent.remove(parent)
        
        num_to_select = 1 + self._num_diff_vectors*2 #first number '1' is the base vector, others are the difference vectors in pairs
        rand_vectors = self._selector(self._population, num_to_select)
        
        base_vector = rand_vectors[0]
        
        diff_vector_tuples = []
        # Create tuples of the difference vectors
        for x in xrange(1, len(rand_vectors), 2):
            diff_vector_tuples.append((rand_vectors[x], rand_vectors[x+1]))
        
        # Calculate the "difference vector" part of the equation, starting with the first F(Xk(t) - Xl(t))
        diff_vector_tuple = diff_vector_tuples[0]
        diff_vector_final = multiply_vector(subtract_vectors(diff_vector_tuple[0], diff_vector_tuple[1]), self._scale_factor)
        
        # Add the other difference vectors, if there are any
        for x in xrange(1, len(diff_vector_tuples)):
            diff_vector_tuple = diff_vector_tuples[x]
            temp_vector = multiply_vector(subtract_vectors(diff_vector_tuple[0], diff_vector_tuple[1]), self._scale_factor)
            diff_vector_final = add_vectors(diff_vector_final, temp_vector)
            
        # Add it to the base vector, and return the result
        return add_vectors(base_vector, diff_vector_final)
    
    def get_trial_vector(self, parent, variant):
        """ Get the trial vector by performing crossover between the parent, j, and its variant"""
        
        out_vector = []
        # Get a random index, so we are guaranteed at least one cross-over
        rand_index = random.randint(0, self._num_dimensions-1)
        
        # For each attribute, determine whether we crossover or not
        for x in xrange(self._num_dimensions):
            rand = random.random()
            # Vjk(t + 1), if (rand <= CR) or (x = rnbr(ind))
            if (rand <= self._cr_rate) or (x == rand_index):
                out_vector.append(variant[x]) 
            # Xjk(t), if (rand > CR) and (x != rnbr(ind))
            else:
                out_vector.append(parent[x])
        
        return out_vector
    
    def print_results(self):
        print "For d:" + str(self._num_dimensions) + " pop_size: " + str(self._pop_size) + " max_gens:" + str(self._max_gens) + " scale_factor: " + str(self._scale_factor) + \
        " crossover_rate: " + str(self._cr_rate)
        print "fitness,values"
        for x in xrange(self._pop_size):
            print str(self._scores[x]) + "," + str(self._population[x])
        
    def __init__(self, num_dimensions, max_gens=DEF_MAX_GENS, pop_size=DEF_POP_SIZE, crossover_rate=DEF_CR_RATE, scaling_factor=DEF_SCALE_FACTOR, selector=DEF_SELECTOR, num_diff_vectors=DEF_NUM_DIFF_VECTORS, crossover_scheme=DEF_CR_SCHEME, obj_function=DEF_OBJ_FUNCT):
        """ Initialise the DE
        
        Keyword arguments:
        num_dimensions -- the number of dimensions in each member of the population
        max_gens -- the maximum number of generations to run (default '10000')
        pop_size -- the number in the population (default '10 * num_dimensions')
        crossover_rate -- the chance of crossover (default '0.4')
        scaling_factor -- the scaling factor (default '0.4')
        selector -- the base-vector selection method, either 'rand_selector' or 'best_selector' (default 'rand_selector')
        num_diff_vectors -- the number of difference vectors to use (default '1')
        crossover_scheme -- the crossover scheme to use, either 'bin' for experiments based on independent binomial experiments, or 'exp' for exponential crossover (default 'bin')
        obj_function -- a function that takes a vector, and returns a fitness rating (default 'schwefel_function')
        """
        
        self._num_dimensions = num_dimensions
        self._max_gens = max_gens
        self._pop_size =  num_dimensions * 10 if (pop_size == DEF_POP_SIZE) else pop_size
        self._cr_rate = crossover_rate
        self._scale_factor = scaling_factor
        self._selector = selector
        self._num_diff_vectors = num_diff_vectors
        self._cr_scheme = crossover_scheme
        self._obj_function = obj_function
        self._scores = []
        
if __name__ == '__main__':
    objective_function = MaxAverageReturn("../../data/av_daily_returns_2011.csv")
#     objective_function = OneMax() 
    
    evolver = DifferentialEvolver(30, num_diff_vectors=1, obj_function=objective_function, max_gens=100)
    evolver.start()