'''
Created on 21.11.2013

@author: gopora
'''
import World

class GADrawer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def updateSession(self, session):
        print('Session - ' + str(session.getGenerationNo()) + ', ' + str(session.getChromosomeNo()) + ', ' + str(session.getNo()) + ', ' + str(session.getActionNo()) + ': ' + str(session.getFitness()))
        

    def updateChromosome(self, chromosome):                   
        print('Chromosome - ' + str(chromosome.getGenerationNo()) + ', ' + str(chromosome.getNo()) + ', ' + str(chromosome.getSessionNo()) + ': ' + str(chromosome.getAvgFitness()))


    def updateGeneration(self, generation):
        print('Generation - ' + str(generation.getNo()) + ':' + str(generation.getMaxAvgFitness()))        

   
    def __str__(self):
        ret = ''
        pos = self.robby.currentPos() if self.robby != None else [-1, -1]
        s   = ''
        
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                s = self.lettuce[x][self.sizeY - y - 1]
                
                if pos[0] == x and pos[1] == self.sizeY - y - 1:
                    if s == World.World.Littered:
                        s = 'R'
                    else:
                        s = 'r'
                
                ret += s + ' '
            ret +='\n'
        
        return ret
                