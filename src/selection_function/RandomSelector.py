'''
Created on Aug 14, 2013

@author: markfeaver
'''

import random

def rand_selector(population, num_to_select=3):
    """ Select a number (default '3') of random individuals from the population, excluding the parent"""
    return random.sample(population, num_to_select)