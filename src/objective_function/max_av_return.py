'''
Created on Aug 15, 2013

@author: Mark Feaver
'''

# from objective_function.ObjectiveFunction import ObjectiveFunction

# class MaxAverageReturn(ObjectiveFunction):
class MaxAverageReturn:
    """ Objective Function, that aims to maximize the daily return. For this problem, there is a realistic constraint that no
    more than eight stocks can be invested in at a time, and no more than 20% of the portfolio can be in a single stock.
    """
    _return_data = []
    
    def calc_fitness(self, vector):
        """ Calculates the fitness, based on the return data. """

        overall_return = 0.0
        for x in xrange(len(vector)):
            overall_return += self._return_data[x]*(abs(vector[x])/len(vector))
        
        return overall_return
            
        
    def __init__(self, csv_return_data):
        f = open(csv_return_data, 'r')
        
        f.readline()
        # Read the second line
        parts = f.readline().strip().split(',')
        for x in xrange(len(parts)):
            self._return_data.append(float(parts[x]))
    
    def select_fittest(self, vector1, vector2):
        """ Return the fittest of the two members and its score, by comparing which has the higher return 
            
        return -- The vector, and the fitness value (the return)
        """
        v1_return = self.calc_fitness(vector1)
        v2_return = self.calc_fitness(vector2)
        
        if v1_return > v2_return:
            return vector1, v1_return
        else:
            return vector2, v2_return
        
    def get_size(self):
        return len(self._return_data)
    