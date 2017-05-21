'''
Created on 19.11.2013

@author: gopora
'''
import random

class World(object):
    '''
    classdocs
    '''
    Tidy               = '0'
    Littered           = '+'
    Wall               = 'w'
    states             = (Tidy, Littered, Wall)
    possibleSituations = {}
    
    @staticmethod
    def generatePossibleSituations():
        cnt        = 0
        situations = {}
        
        for stateCenter in World.states:
            for stateNorth in World.states:
                for stateSouth in World.states:
                    for stateEast in World.states:
                        for stateWest in World.states:
                            situations[(stateCenter, stateNorth, stateSouth, stateEast, stateWest)]  = cnt
                            cnt                                                                     += 1
        
        return situations


    def __init__(self, sizeX, sizeY):
        '''
        Constructor
        '''
        self.sizeX     = sizeX
        self.sizeY     = sizeY
        self.lettuce   = range(sizeX)
        self.cntLitter = 0
        self.robby     = None
        
        for x in range(sizeX):
            self.lettuce[x] = [World.Tidy for _y in range(sizeY)] 
            
        if len(World.possibleSituations) == 0:
            World.possibleSituations = World.generatePossibleSituations()
        
    def litter(self, noCans):
        i = 0
        
        while i < noCans:
            rnd = random.randint(0, self.sizeX * self.sizeY - 1)
            x   = rnd // self.sizeX
            y   = rnd - x * self.sizeX
            
            if self.lettuce[x][y] != World.Littered:
                self.lettuce[x][y]  = World.Littered
                i                  += 1
                
            self.cntLitter += noCans
                
    def clean(self):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                self.lettuce[x][y] = World.Tidy
        
        self.cntLitter = 0
                
    def cleanAt(self, x, y):
        if not self.isTidyAt(x, y):
            self.lettuce[x][y]  = World.Tidy
            self.cntLitter     -= 1
    
    def isTidy(self):        
        return self.cntLitter == 0
    
    def isTidyAt(self, x, y):
        return self.lettuce[x][y] == World.Tidy
    
    def canMoveNorthAt(self, x, y):
        return y < self.sizeY - 1    

    def canMoveSouthAt(self, x, y):
        return y > 1    

    def canMoveEastAt(self, x, y):
        return x < self.sizeX - 1
    
    def canMoveWestAt(self, x, y):
        return x > 1
    
    def situationAt(self, x, y):
        stateCenter = self.lettuce[x][y]
        stateNorth  = self.lettuce[x][y + 1] if y < self.sizeY - 1 else World.Wall
        stateSouth  = self.lettuce[x][y - 1] if y > 0 else World.Wall
        stateEast   = self.lettuce[x + 1][y] if x < self.sizeX - 1 else World.Wall
        stateWest   = self.lettuce[x - 1][y] if x > 0 else World.Wall
        
        return World.possibleSituations[(stateCenter, stateNorth, stateSouth, stateEast, stateWest)]   
        
