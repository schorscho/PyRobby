'''
Created on 24.11.2013

@author: gopora
'''
import unittest

from unittest import TestCase
from World import World
from Robby import Robby
from Chromosome import Chromosome


class RobbyTest(TestCase):


    def testName(self):
        world    = World(10, 10)
        strategy = Chromosome()
        robby    = Robby()

        print(world)

        world.litter(50)
        
        print(world)

        strategy.seed()
        
        robby.setStrategy(strategy)
        robby.startCleaning(world)
        
        print(world)
        
        robby.nextAction()
        print(world)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()