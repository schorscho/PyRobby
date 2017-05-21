'''
Created on 20.11.2013

@author: gopora
'''
import math
import random

from World import World
from Robby import Robby
from Chromosome import Chromosome
from Generation import Generation
from Session import Session


class GeneticAlgorithm(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.updateListener               = None
        self.noOfGenerations              = 1000
        self.noOfChromosomesPerGeneration = 200
        self.noOfSessionsPerChromosome    = 100
        self.noOfActionsPerSession        = 200
        self.sizeOfWorldGrid              = 10

    def setUpdateListener(self, updateListener):
        self.updateListener = updateListener
        
    def run(self):
        world                = World(self.sizeOfWorldGrid, self.sizeOfWorldGrid)
        robby                = Robby()
        curGeneration        = None
        
        random.seed()

        for _iGen in range(self.noOfGenerations):
            curGeneration = self.createNextGeneration(curGeneration)
            
            for iChrom in range(curGeneration.getSize()):
                curChromosome = curGeneration.getChromosomeAt(iChrom)
                
                for iSession in range(self.noOfSessionsPerChromosome):
                    session = Session(curGeneration.getNo(), curChromosome, iSession, world, robby, self.noOfSessionsPerChromosome, self.noOfActionsPerSession)
                    
                    session.run(self.updateListener)
                        
                    curChromosome.updateAvgFitness(session)
                
                self.updateListener.updateChromosome(curChromosome)    
                
                curGeneration.updateMaxAvgFitness(curChromosome.getAvgFitness())
                
            self.updateListener.updateGeneration(curGeneration)    

    
    def createNextGeneration(self, generation):
        if generation == None:
            nextGeneration = Generation(0)
        
            while nextGeneration.getSize() < self.noOfChromosomesPerGeneration:
                chromosome = Chromosome(nextGeneration.getNo(), nextGeneration.getSize())
                
                chromosome.seed()
                
                nextGeneration.addChromosome(chromosome)
        else:
            generation.sortAccordingToFitness()
            
            nextGeneration = Generation(generation.getNo() + 1)
            
            while nextGeneration.getSize() < self.noOfChromosomesPerGeneration:
                i1       = int(math.fabs(math.ceil(random.gauss(0, 0.1) * 199)))
                parent1  = generation.getChromosomeAt(i1)
                i2       = i1
                
                while i2 == i1:
                    i2 = int(math.fabs(math.ceil(random.gauss(0, 0.1) * 199)))
                    
                parent2  = generation.getChromosomeAt(i2)
                
                children = parent1.mate(nextGeneration.getNo(), nextGeneration.getSize(), parent2)
                
                for child in children:
                    child.mutate()

                    nextGeneration.addChromosome(child)
                    
                    
        
        return nextGeneration
    


        
        
        