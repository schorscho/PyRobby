'''
Created on 19.11.2013

@author: gopora
'''
import random

from Chromosome import Chromosome

class ActionResult(object):
    def __init__(self, declaredAction, executedAction, success):
        self.declaredAction = declaredAction
        self.executedAction = executedAction
        self.success        = success
        
    
    def getDeclaredAction(self):
        return self.declaredAction
    
    
    def getExecutedAction(self):
        return self.executedAction
    

    def isSuccessful(self):
        return self.success
    

class Robby(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.chromosome = None
        self.world      = None
        self.currentX   = 0
        self.currentY   = 0
        
    def setChromosome(self, chromosome):
        self.chromosome = chromosome
        
    def startCleaning(self, world):
        self.world    = world
        self.currentX = 0
        self.currentY = 0
        
    def currentPos(self):
        return [self.currentX, self.currentY]
    
    def nextAction(self):
        success        = True
        declaredAction = self.chromosome.getActionForSituation(self.world.situationAt(self.currentX, self.currentY))
        executedAction = declaredAction
        
        if declaredAction == Chromosome.MoveRandom:
            executedAction = random.choice([Chromosome.MoveNorth, Chromosome.MoveSouth, Chromosome.MoveEast, Chromosome.MoveWest])
        
        if executedAction != Chromosome.StayPut:
            if executedAction == Chromosome.MoveNorth and self.world.canMoveNorthAt(self.currentX, self.currentY):
                self.currentY += 1
            elif executedAction == Chromosome.MoveSouth and self.world.canMoveSouthAt(self.currentX, self.currentY):
                self.currentY -= 1
            elif executedAction == Chromosome.MoveEast and self.world.canMoveEastAt(self.currentX, self.currentY):
                self.currentX += 1
            elif executedAction == Chromosome.MoveSouth and self.world.canMoveWestAt(self.currentX, self.currentY):
                self.currentX -= 1
            elif executedAction == Chromosome.Collect and not self.world.isTidyAt(self.currentX, self.currentY):
                self.world.cleanAt(self.currentX, self.currentY)
            else:
                success = False
            
        return ActionResult(declaredAction, executedAction, success)
            
            
            
            
            
        