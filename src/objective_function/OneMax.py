'''
Created on Aug 14, 2013

@author: markfeaver
'''

def one_max(vector):
    """ Calculate the fitness of a vector, based on how close the values average to 1. If the value is greater than 1, return 0 """
    
    total = 0
    n = len(vector)
    for x in xrange(n):
        total += vector[x]
    
    val = total/float(n)
    if val > 1:
        return 0
    return val