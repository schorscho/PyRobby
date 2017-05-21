from GeneticAlgorithm import GeneticAlgorithm
from GADrawer import GADrawer

def main():
    ga       = GeneticAlgorithm()
    gaDrawer = GADrawer()
    
    ga.setUpdateListener(gaDrawer)
    ga.run()
    


if __name__ == "__main__":
    main()