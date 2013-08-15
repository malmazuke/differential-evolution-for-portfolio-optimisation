'''
Created on Aug 15, 2013

@author: feaver
'''
from abc import ABCMeta, abstractmethod  

class ObjectiveFunction(object):
    
    __metaclass__ = ABCMeta
    
    @abstractmethod 
    def calc_fitness(self, vector):
        """ Calculate the fitness of a member of the population """
        pass
    
    @abstractmethod
    def select_fittest(self, vector1, vector2):
        """ Select the fittest of the two members"""
        pass