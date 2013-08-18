'''
Created on Aug 12, 2013

@author: Mark Feaver
'''

# from objective_function.ObjectiveFunction import ObjectiveFunction
from operator import itemgetter

N_TOP_STOCKS = 8

# class MaxAverageReturn(ObjectiveFunction):
class MaxAverageReturn:
    """ Objective Function, that aims to maximize the daily return. For this problem, there is a realistic constraint that no
    more than eight stocks can be invested in at a time, and no more than 20% of the portfolio can be in a single stock.
    """
    _return_data = []
    
    def calc_fitness(self, vector):
        """ Calculate the fitness, based on the return data. 
        
        We can only select N number of stocks.
        Also, if any of the weights are above 20%, return the worst possible fitness.
        This enforces a '20% per stock maximum'. 
        """

        weights = self.weights_for_vector(vector)

        overall_return = 0.0
        for x in xrange(len(weights)):
            if weights[x] >= .2:
                return 0
            overall_return += self._return_data[x]*weights[x]
        
        return overall_return
            
        
    def __init__(self, csv_return_data):
        f = open(csv_return_data, 'r')
        
        f.readline()
        # Read the second line
        parts = f.readline().strip().split(',')
        for x in xrange(len(parts)):
            self._return_data.append(float(parts[x]))
        
        f.close()
    
    def select_fittest(self, vector1, vector2):
        """ Return the fittest of the two members and its score, by comparing which has the higher average daily return
            
        return -- The vector, and the fitness value (the return)
        """
        v1_vol = self.calc_fitness(vector1)
        v2_vol = self.calc_fitness(vector2)
        
        if v1_vol > v2_vol:
            return vector1, v1_vol
        else:
            return vector2, v2_vol
        
    def get_size(self):
        return len(self._return_data)
    
    def weights_for_vector(self, vector):
        """ Calculate the weights for a given vector - in this case, the top N values in the vector are selected, 
        then are normalised to sum to 1
        
        return -- a vector/list containing all weights, N of which are values greater than 0, and all of which sum to 1.
        These returned values represent the percentage of a portfolio to invest in a particular stock 
        """
        
        weights = [] # going to contain N_TOP_STOCKS, and the rest are zeroes
        
        # This will contain tuples, so that we can keep track of the indexes when we sort to find the top N weights
        sorted_vals = []
        for x in xrange(len(vector)):
            vec = (x, vector[x])
            sorted_vals.append(vec)
            # Initialise all the values in weights to 0, so we can simply set the appropriate ones later
            weights.append(0.0)
        
        sorted_vals = sorted(sorted_vals,key=itemgetter(1), reverse=True)
        sorted_vals = sorted_vals[:N_TOP_STOCKS + 1]
        
        # Get the max and min, so we can normalise the values
        max_value = sorted_vals[0][1]
        min_value = sorted_vals[len(sorted_vals) - 1][1]
         
        # Add the top N stock weights to the weights list, normalising as we go (although we still need to normalise so that they sum to 1)
        for x in xrange(N_TOP_STOCKS + 1): # Plus one, so that the 'min_value' index is set to zero, allowing N_TOP_STOCKS to have weights greater than zero
            tup = sorted_vals[x]
            index = tup[0]
            val = abs((tup[1] - min_value)/(max_value - min_value))
            sorted_vals[x] = (index, val)
        
        sum_weights = sum([pair[1] for pair in sorted_vals])
        
        for x in xrange(N_TOP_STOCKS + 1):
            # Now we divide by the sum of the weights, so that they add to 1
            tup = sorted_vals[x]
            index = tup[0]
            val = tup[1]/sum_weights
            weights[index] = val
            
        return weights
        
    def get_model(self, vector):
        """ Returns a representative model of the vector - in this case, the weights that lead to an optimal return """
        return self.weights_for_vector(vector)
    
    def find_best_model(self, scores):
        """ Output the best candidate's index """
        
        best_index = 0
        best_score = 0
        for x in xrange(len(scores)):
            if scores[x] > best_score:
                best_index = x
                best_score = scores[x]
                
        return best_index
         