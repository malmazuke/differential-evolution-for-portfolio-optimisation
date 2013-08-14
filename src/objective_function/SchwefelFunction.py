'''
Created on Aug 14, 2013

@author: Mark Feaver
'''

import math

def schwefel_function(vector):
    """ Calculate the fitness of a vector from a population using the Schwefel function"""
    length = len(vector)
    fitness = 0
    for i in xrange(0,length):
        fitness = fitness + vector[i]*math.sin(math.sqrt(math.fabs(vector[i])))
    fitness = 418.9828872724337998*(length*1.0) - fitness
    
    return fitness