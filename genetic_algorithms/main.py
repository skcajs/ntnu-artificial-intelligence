import random
import string
from utils import swap, bin_to_float, float_to_bin
import time
import numpy as np
import math
from GA import GeneticAlgorithm

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
    
    # # --- Test 0 --- #
    # population = generate_population_bin(2000, 128)

    # config = {
    #     'X': 0.2,
    #     'pairing': 'random',
    #     'k': 3,
    #     'boundaries': None,
    #     'mutation': 0.2
    #     }
    
    # ga = GeneticAlgorithm(population, fitness_simple_bin, config)
    # result = ga.start()
    # to_print = result['fittest'][0]
    # print(to_print)
    # print(result['time_taken'])

    # #--- Test 1 --- #

    config = {
        'X': 0.7,
        'pairing': 'random',
        'k': 3,
        'boundaries': None,
        'mutation': 0.2
        }
    quote_char = "The aroma of freshly brewed coffee fills the air."
    population_char = generate_population_char(5000, len(quote_char))
    ga=GeneticAlgorithm(population_char, fitness_char)
    result = ga.start(count=50)
    to_print = result['fittest'][0]
    print(to_print)
    print(result['time_taken'])


    # --- Test 2 --- #

    # boundaries = [(0,10), [0,10]]
    # config = {
    #     'X': 0.5,
    #     'pairing': 'tournament',
    #     'crossover': 'single-point',
    #     'k': 3,
    #     'boundaries': boundaries,
    #     'mutation': 0.2
    #     }
    
    # def fitness(population, boundaries):
    #     weights = []
    #     for gene in population:
    #         ind = int(len(gene)/2)
    #         x = bin_to_float(gene[:ind])
    #         if (x <= boundaries[0][0]):
    #             x = boundaries[0][0]
    #         elif (x >= boundaries[0][1]):
    #             x = boundaries[0][1]
    #         y = bin_to_float(gene[ind:])
    #         if (y <= boundaries[1][0]):
    #             y = boundaries[1][0]
    #         elif (y >= boundaries[1][1]):
    #             y = boundaries[1][1]
    #         f_xy = x * math.sin(4 * x) + 1.1 * y * math.sin(2*y)
    #         if(math.isnan(f_xy)):
    #             weights.append(0)
    #         weights.append(f_xy)
    #     return weights
        
    # population = generate_population_float(100, 2, boundaries, True)

    # ga=GeneticAlgorithm(population, fitness, config)
    # result = ga.start(count=100)
    # to_print = result['fittest'][0]
    # print(to_print)
    # print(result['time_taken'])
