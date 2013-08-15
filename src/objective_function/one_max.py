'''
Created on Aug 14, 2013

@author: markfeaver
'''
# from objective_function.objective_function import ObjectiveFunction

# class OneMax(ObjectiveFunction):
class OneMax:
    def calc_fitness(self, vector):
        """ Calculate the fitness of a vector, based on how close the values average to 1. """
    
        total = sum(vector)
        
        diff = abs(total - 1)
        return diff
    
    def select_fittest(self, vector1, vector2):
        """ Select the fittest of the two vectors - i.e. the one that is closest to the number 1"""
        v1_return = self.calc_fitness(vector1)
        v2_return = self.calc_fitness(vector2)
        
        if v1_return < v2_return:
            return vector1, v1_return
        else:
            return vector2, v2_return