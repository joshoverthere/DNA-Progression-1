import random
import copy
from colorama import Fore, Back, Style
import matplotlib.pyplot as plt

changes = []
generationsDone = 0
volrand = [50]

def runSimulation():
    allOrganisms = []
    global generationsDone
    generationsDone = 0
    
    
    def printR(text):
        print(Fore.RED + text)
        print(Style.RESET_ALL)
        
    def findSimilarity(dna1, dna2):
        similarityPoints = 0
        
        for i in range(0,len(dna1)):
            if dna1[i] == dna2[i]:
                similarityPoints += 1
        
        return int((similarityPoints/len(dna1))*100)
    
    class organism():
        def __init__(self, parentDna):
            allOrganisms.append(self)
            
            if parentDna == "0":
                self.giveDna()
            else:
                self.inherit(parentDna)
            
            global generationsDone
            if generationsDone < 300:
                generationsDone += 1
                self.mytosis()
        
        def giveDna(self):
            dnaString = ""
            for i in range(100):
                dnaString += random.choice(["A", "C", "G", "T"])
            self.dna = dnaString
            
        def mytosis(self):
            childCreature = organism(self.dna)
            
        def inherit(self, parentDna):
            self.dna = parentDna
            
            if volrand[0] < 1:
            
                voll = 1/volrand[0]
                if random.randint(1,voll)==voll:
                    volatility = 1
                else:
                    volatility = 0

            else:
                volatility = volrand[0]
                
            for i in range(volatility):
                self.dna = self.dna.replace(self.dna[random.randint(0,len(self.dna)-1)], random.choice(["A", "C", "G", "T"]), 1)
         
    
    #begin cycle
    newCreature = organism("0")
    #create list of similarities
    similarities = []
    for i in range(0,len(allOrganisms)-1):
        similarities.append(findSimilarity(allOrganisms[0].dna, allOrganisms[i].dna))
    global changes
    changes += [similarities]
    

#similarities = []
#for i in range(0,800):
    #similarities.append(100)
#changes += [similarities]
#print("added ancestor baseline")

#baseline = []
#for i in range(0,800):
    #baseline.append(0)
#print("added baseline")
    
    
for i in range(100):
    volrand[0] = 0.01
    runSimulation()
    print("Simulation ", i, " completed.")
    
for i in range(50):
    volrand[0] = 1
    runSimulation()
    print("Simulation ", i, " completed.")

for i in range(20):
    volrand[0] = 500
    runSimulation()
    print("Simulation ", i, " completed.")

    
for e in range(len(changes)):
    plt.plot([i for i in range(300)], changes[e-1])

#plt.plot([i for i in range(800)], baseline)

plt.title('Genetic divergence from ancestor DNA sequence over generations')
plt.xlabel('generation')
plt.ylabel('similarity to ancestor / %')
plt.show()

print(len(changes))

