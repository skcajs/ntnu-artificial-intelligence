import random
import string
from utils import string2bin, swap

class GeneticAlgorithm:
    def __init__(self, population, fitness=None):
        self.population = population
        self.fitness = fitness
    
    def start(self):
        count = 50
        while count > 0:
            self.__population_fitness()
            weights = self.__fitness()
            pop_weights = list(map(lambda x, y:(x,y), weights, self.population))
            population_2 = []
            for _ in range(2*len(self.population)):
                parent1, parent2 = self.__selection(pop_weights)
                child = self.__reproduce(parent1, parent2)
                if(random.randint(0, 100) < 10):
                    child = self.__mutate(child)
                population_2.append(child)
            for i in range(len(self.population)):
                self.population[i] = population_2[i]
            count -= 1
            # print({'i': count, 'population_fitness': self.__population_fitness()})
            print('i ', count, ' population_fitness ', self.__population_fitness(), '\nbest_so_far\n', self.__fittest())
        return {'population_fitness': self.__population_fitness(), 'fittest': self.__fittest()}

    def __fittest(self):
        weights = self.__fitness()
        return self.population[weights.index(max(weights))], max(weights)

    def __fitness(self):
        return self.fitness(self.population)
    
    def __selection(self, pop_weights):
        k = 3
        return max(random.choices(pop_weights, k=k))[1], max(random.choices(pop_weights, k=k))[1]
        
    def __reproduce(self, parent1: str, parent2: str):
        n = len(parent1)
        c = random.randint(1, n)
        return parent1[:c] + parent2[c:]
    
    def __mutate(self, child):
        p = 1/len(child)*100
        mutant = []
        for g in child:
            r = random.random()
            if (p > r):
                g = swap(g)
            mutant.append(g)
        return ''.join(mutant)
    
    def __population_fitness(self):
        weights = self.__fitness()
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
    
    def generate_population_char(s: int, n:int):
        population = []
        for _ in range(s):
            gene = []
            for _ in range(n):
                k = random.choice(string.ascii_lowercase + string.digits + string.punctuation + ' ')
                gene.append(str(k))
            population.append(''.join(gene))
        return population
    
    # def fitness(population):
    #     weights = []
    #     for gene in population:
    #         weight = len(gene)
    #         for i in range(len(gene)):
    #             if gene[i] == '0':
    #                 weight -= 1
    #         weights.append(weight)
    #     return weights
    
    def fitness(population):
        weights = []
        for gene in population:
            weight = len(gene)
            for i in range(len(gene)):
                if gene[i] != quote[i]:
                    weight -= 1
            weights.append(weight/len(gene))
        return weights
    

    

    
    # quote = "I've seen things you people wouldn't believe. Attack ships on fire off the shoulder of Orion. I watched C-beams glitter in the dark near the Tannhauser gate. All those moments will be lost in time... like tears in rain... Time to die."
    quote = "hello, i'm sam and I created this genetic algorithm"
    # quote = string2bin(quote)

    population = generate_population_char(10000, len(quote))

    ga=GeneticAlgorithm(population, fitness)

    result = ga.start()

    to_print = result['fittest'][0]
    print(to_print)
    # print(' '.join([to_print[i:i+8] for i in range(0, len(to_print), 8)]))