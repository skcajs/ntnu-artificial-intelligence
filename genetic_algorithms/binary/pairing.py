import numpy as np
import random

class Pairing:
    def __init__(self, pairing, k):
        self.pairing = pairing
        self.k = k

    def apply(self, population):
        if self.pairing == 'tournament':
            return self.__tournament(population)
        
    def __tournament(self, population):
        parents = []
        population_copy = np.copy(population).tolist()
        for _ in range(int(len(population)/2)):
            tournaments = []
            for _ in range(self.k):
                tournaments.append(max(random.sample(population_copy, k=self.k)))
            tournaments = sorted(tournaments, key= lambda x: x[1])
            try:
                parent1 = population_copy.pop(population_copy.index(tournaments[-1]))
                parent2 = population_copy.pop(population_copy.index(tournaments[-2]))
            except:
                parents.append((parent1,parent2))
                continue
            parents.append((parent1,parent2))
        return parents
