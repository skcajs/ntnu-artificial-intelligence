import random
import string
from utils import swap, bin_to_float, float_to_bin
import time
import numpy as np
import math

class GeneticAlgorithm:
    def __init__(self, population, fitness=None, config=None):
        self.population = population
        self.fitness = fitness
        if config:
            self.config = config # JSON
        else:
            self.config = {
                'X': 0.5,
                'pairing': 'tournament',
                'k': 3,
                'boundaries': None,
                'mutation': 0.2
            }
    
    def start(self, count=100):
        tic = time.perf_counter()
        while count > 0:
            weighted_population = self.__fitness()
            weighted_population = self.__selection(weighted_population, self.config['X'])
            children = []
            for _ in range(len(self.population) - len(weighted_population)):
                parent1, parent2 = self.__pairing(weighted_population)
                child = self.__reproduce(parent1, parent2)
                if(random.random() < self.config['mutation']):
                    child = self.__mutate(child)
                children.append(child)
            self.population.clear()
            self.population = children + [population[1] for population in weighted_population]
            count -= 1
            print('i: ', count, '\npopulation_fitness ', self.__population_fitness(), '\nbest_so_far: ', self.__fittest())
            if(self.__fittest()[1] == 1.0): break
        toc = time.perf_counter()
        return {'population_fitness': self.__population_fitness(), 'time_taken': f"{toc - tic:0.4f}", 'fittest': self.__fittest()}

    def __fitness(self):
        if self.config['boundaries']:
            return list(map(lambda x, y:(x,y), self.fitness(self.population, self.config['boundaries']), self.population))
        return list(map(lambda x, y:(x,y), self.fitness(self.population), self.population))
    
    def __selection(self, weighted_population, X):
        return sorted(weighted_population, key = lambda x: x[0], reverse = True)[:int(X*len(self.population))]
    
    def __pairing(self, weighted_population):
        pairing = self.config['pairing']
        if (pairing == 'tournament'):
            k=int(self.config['k'])
            tournament = random.sample(weighted_population, k=(3 * k))
            pairings = sorted([max(tournament[i * k:(i + 1) * k]) for i in range((len(tournament) + k - 1) // k )], key = lambda x: x[0], reverse = True)
            return pairings[0][1], pairings[1][1]
        elif(pairing == 'random'):
            return max(random.choices(weighted_population))[1], max(random.choices(weighted_population))[1]
            
    def __reproduce(self, parent1: str, parent2: str):
        n = len(parent1)
        c = random.randint(1, n)
        return parent1[:c] + parent2[c:]
    
    def __mutate(self, child):
        p = 0.4
        mutant = []
        for g in child:
            r = random.random()
            if (p > r):
                g = swap(g)
            mutant.append(g)
        return ''.join(mutant)
    
    def __fittest(self):
        weights = [x[0] for x in self.__fitness()]
        return self.population[weights.index(max(weights))], max(weights)
    
    def __population_fitness(self):
        weights = [x[0] for x in self.__fitness()]
        return sum(weights)/len(weights)

if __name__ == "__main__":
    
    def generate_population_bin(n: int, s:int):
        population = []
        for _ in range(n):
            gene = []
            for _ in range(s):
                k = random.randint(0, 1)
                gene.append(str(k))
            population.append(''.join(gene))
        return population
    
    def generate_population_float(n: int, s:int, r:list, encode=False):
        population = []
        for _ in range(n):
            gene = []
            for i in range(s):
                k = float('{0:.4f}'.format(random.uniform(*r[i])))
                if(encode):
                    k = float_to_bin(k)
                gene.append(str(k))
            population.append(''.join(gene))
        return population
    
    def generate_population_char(n: int, s:int):
        population = []
        for _ in range(n):
            gene = []
            for _ in range(s):
                k = random.choice(string.ascii_letters + string.digits + string.punctuation + ' ')
                gene.append(str(k))
            population.append(''.join(gene))
        return population
    
    def fitness_simple_bin(population):
        weights = []
        for gene in population:
            weight = len(gene)
            for i in range(len(gene)):
                if gene[i] == '0':
                    weight -= 1
            weights.append(weight/len(gene))
        return weights
    
    def fitness_char(population):
        quote = "The aroma of freshly brewed coffee fills the air."
        weights = []
        for gene in population:
            weight = len(gene)
            for i in range(len(gene)):
                if gene[i] != quote[i]:
                    weight -= 1
            weights.append(weight/len(gene))
        return weights
    
    # --- Test 0 --- #
    # population = generate_population_bin(2000, 128)

    # config = {
    #     'X': 0.2,
    #     'pairing': 'random',
    #     'k': 3
    #     }
    
    # ga = GeneticAlgorithm(population, fitness_simple_bin, config)
    # result = ga.start()
    # to_print = result['fittest'][0]
    # print(to_print)
    # print(result['time_taken'])

    # --- Test 1 --- #
    # quote_char = "The aroma of freshly brewed coffee fills the air."
    # population_char = generate_population_char(2000, len(quote_char))
    # ga=GeneticAlgorithm(population_char, fitness_char)
    # result = ga.start()
    # to_print = result['fittest'][0]
    # print(to_print)
    # print(result['time_taken'])


    # --- Test 2 --- #

    boundaries = [(0,50), [0,50]]
    config = {
        'X': 0.1,
        'pairing': 'tournament',
        'crossover': 'single-point',
        'k': 3,
        'boundaries': boundaries,
        'mutation': 0.2
        }
    
    def fitness(population, boundaries):
        weights = []
        for gene in population:
            ind = int(len(gene)/2)
            x = bin_to_float(gene[:ind])
            if (x < boundaries[0][0]):
                x = boundaries[0][0]
            elif (x > boundaries[0][1]):
                x = boundaries[0][1]
            y = bin_to_float(gene[ind:])
            if (y < boundaries[1][0]):
                y = boundaries[1][0]
            elif (y > boundaries[1][1]):
                y = boundaries[1][1]
            f_xy = x * math.sin(4 * x) + 1.1 * y * math.sin(2*y)
            weights.append(f_xy)
        return weights
        
    population = generate_population_float(1000, 2, boundaries, True)

    ga=GeneticAlgorithm(population, fitness, config)
    result = ga.start(count=100)
    to_print = result['fittest'][0]
    print(to_print)
    print(result['time_taken'])

    # print(' '.join([to_print[i:i+8] for i in range(0, len(to_print), 8)]))


