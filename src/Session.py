'''
Created on 20.11.2013

@author: gopora
'''
from Chromosome import Chromosome


class Session(object):
    
    def __init__(self, generationNo, chromosome, no, world, robby, noOfPiecesOfLitter, maxNoOfActions):
        self.generationNo       = generationNo
        self.no                 = no
        self.world              = world
        self.robby              = robby
        self.chromosome         = chromosome
        self.noOfPiecesOfLitter = noOfPiecesOfLitter
        self.maxNoOfActions     = maxNoOfActions
        self.fitness            = 0
        self.actionNo           = 0
                

    def run(self, updateListener):
        self.fitness = 0
        
        self.world.clean()
        self.world.litter(self.noOfPiecesOfLitter)
        
        self.robby.setChromosome(self.chromosome)
        self.robby.startCleaning(self.world)
        
        nextAction = None

        while self.actionNo < self.maxNoOfActions and (nextAction == None or nextAction.isSuccessful() or nextAction.getDeclaredAction() == Chromosome.MoveRandom):
            nextAction = self.robby.nextAction()
            
            self.fitness += self.calculateFitness(nextAction)
            
            self.actionNo +=1
            
        updateListener.updateSession(self)
            
    
    def getGenerationNo(self):
        return self.generationNo        
    
    
    def getChromosomeNo(self):
        return self.chromosome.getNo()
    
    
    def getNo(self):
        return self.no
    
    
    def getActionNo(self):
        return self.actionNo


    def calculateFitness(self, actionResult):
        if actionResult.getExecutedAction() == Chromosome.Collect:
            if actionResult.isSuccessful():
                return 10
            else:
                return -1
        elif not actionResult.isSuccessful():
            return -5
        else:
            return 0
        
        
    def getFitness(self):
        return self.fitness
