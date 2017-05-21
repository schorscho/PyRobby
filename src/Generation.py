'''
Created on 20.11.2013

@author: gopora
'''


class Generation(object):
    def __init__(self, no):
        '''
        Constructor
        '''
        self.no            = no
        self.chromosomes   = []
        self.maxAvgFitness = -1000000 
        

    def sortAccordingToFitness(self):
        self.chromosomes.sort(lambda x, y: cmp(x.getAvgFitness(), y.getAvgFitness()), None, True)
        
        
    def addChromosome(self, chromosome):
        self.chromosomes.append(chromosome)
        
        
    def getSize(self):
        return len(self.chromosomes)
    
    
    def getNo(self):
        return self.no
    
    
    def getChromosomeAt(self, index):
        chromosome = None
        
        if (index < len(self.chromosomes)):
            chromosome = self.chromosomes[index]
        
        return chromosome
    

    def updateMaxAvgFitness(self, fitness):
        if self.maxAvgFitness < fitness:
            self.maxAvgFitness = fitness
            
            
    def getMaxAvgFitness(self):
        return self.maxAvgFitness
