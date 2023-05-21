from genetic_algorithm import GeneticAlgorithm
from utils import *
import random

if __name__ == "__main__":

    def generate_population_char(n: int, s:int):
        population = []
        for _ in range(n):
            gene = []
            for _ in range(s):
                k = random.choice(string.ascii_letters + string.digits + string.punctuation + ' ')
                gene.append(str(k))
            population.append(''.join(gene))
        return population
    
    def fitness_char(chromosone):
        quote = "The aroma of freshly brewed coffee fills the air."
        weight = len(chromosone)
        for i in range(len(chromosone)):
            if chromosone[i] != quote[i]:
                weight -= 1
        return weight

    quote_char = "The aroma of freshly brewed coffee fills the air."
    population_char = generate_population_char(2000, len(quote_char))
    ga=GeneticAlgorithm(population_char, fitness_char)
    result = ga.run()
    to_print = result['fittest'][0]
    print(to_print)
    print(result['time_taken'])