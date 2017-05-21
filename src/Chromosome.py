'''
Created on 20.11.2013

@author: gopora
'''
import random


class Chromosome(object):
    '''
    classdocs
    '''
    Collect    = 'C'
    MoveNorth  = 'N'
    MoveSouth  = 'S'
    MoveEast   = 'E'
    MoveWest   = 'W'
    MoveRandom = 'R'
    StayPut    = 'P'
    Actions    = (Collect, MoveNorth, MoveSouth, MoveEast, MoveWest, MoveRandom, StayPut)

    def __init__(self, generationNo, no):
        '''
        Constructor
        '''
        self.rules        = []
        self.avgFitness   = 0
        self.generationNo = generationNo
        self.no           = no
        self.sessionNo    = 0
        
    def seed(self):             
        self.rules = [random.choice(Chromosome.Actions) for _i in range(243)]
        
        
    def getActionForSituation(self, situation):
        return self.rules[situation]
    
    
    def mate(self, generationNo, chromosomeNo, mate):
        sep    = random.randint(0, 243)
        child1 = Chromosome(generationNo, chromosomeNo)
        child2 = Chromosome(generationNo, chromosomeNo + 1)
        
        child1.rules.extend(self.rules[0:sep])
        child1.rules.extend(mate.rules[sep:243])
        
        child2.rules.extend(mate.rules[0:sep])
        child2.rules.extend(self.rules[sep:243])
        
        return [child1, child2]
    
    
    def mutate(self):
        for _i in range(10):
            n = random.randint(0, 242)
            
            if n < 243:
                action = self.rules[n]
                
                while action == self.rules[n]:
                    action = random.choice(Chromosome.Actions)
                    
                    
    def getAvgFitness(self):
        return self.avgFitness
    
    
    def updateAvgFitness(self, session):
        self.avgFitness = (self.avgFitness * session.getNo()  + session.getFitness()) / (session.getNo() + 1)
        self.sessionNo  = session.getNo()
        
        
    def getGenerationNo(self):
        return self.generationNo
    
    
    def getNo(self):
        return self.no
    
    
    def getSessionNo(self):
        return self.sessionNo
                
    