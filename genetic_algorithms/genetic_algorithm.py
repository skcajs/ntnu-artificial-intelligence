import random

class GeneticAlgorithm:
    def __init__(self, population, fitness=None):
        self.population = population
        self.fitness = fitness
    
    def start(self):
        count = 100
        while count > 0:
            weights = self.__fitness()
            population_fitness = self.__population_fitness(weights)
            population_2 = []
            for _ in range(2*len(self.population)):
                parent1, parent2 = self.__selection(weights)
                child = self.__reproduce(parent1, parent2)
                if(random.randint(0, 100) < 10):
                    child = self.__mutate(child)
                population_2.append(child)
            for i in range(len(self.population)):
                self.population[i] = population_2[i]
            count -= 1
        return self.__fittest(self.population)

    def __fittest(self, population):
        weights = self.__fitness(population, self.fitness)
        return population[weights.index(max(weights))]

    def __fitness(self):
        weights = []
        for gene in self.population:
            weight = len(gene)
            for i in range(len(gene)):
                if gene[i] == '0':
                    weight -= 1
            weights.append(weight)
        return weights
    
    def __selection(self, weights):
        fittest_portion = int(0.25 * len(weights))
        best = sorted(range(len(weights)), key=lambda i: weights[i], reverse=True)[:fittest_portion]
        weight_1 = best[random.randint(0, fittest_portion-1)]
        weight_2 = 0
        while True:
            weight_2 = best[random.randint(0, fittest_portion-1)]
            if weight_1 != weight_2: break
        return self.population[weight_1], self.population[weight_2]
        
    def __reproduce(self, parent1: str, parent2: str):
        n = len(parent1)
        c = random.randint(1, n)
        return parent1[:c] + parent2[c:n]
    
    def __mutate(self, child):
        n = len(child)
        c = random.randint(1, n)
        mutation = 0
        if (child[c-1] == 0):
            mutation = 1
        return child[:c-1] + str(mutation) + child[c+1:n]
    
    def __population_fitness(self, weights):
        return sum(weights)/len(weights)
    

if __name__ == "__main__":
    def generate_population(s: int, n:int):
        population = []
        for _ in range(s):
            gene = []
            for _ in range(n):
                k = random.randint(0, 1)
                gene.append(str(k))
            population.append(''.join(gene))
        return population

    population = generate_population(100, 16)

    ga=GeneticAlgorithm(population)
    print(ga.start())
