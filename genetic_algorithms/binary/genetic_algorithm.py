from selection import Selection
from crossover import Crossover
from pairing import Pairing

import numpy as np

class GeneticAlgorithm:
    def __init__(self, initial_population, f_fitness, config={}):
        self.population = self.init_population(initial_population)
        self.fitness = f_fitness
        self.config = self.validate_config(config)
        self.selection = Selection(config['sample_rate'])
        self.pairing = Pairing(config['pairing'], config['k'])
        self.crossover = Crossover(config['crossover'])
        self.generations = config['generations']

    def init_population(self, initial_population):
        return np.array([(chromosone, float('inf')) for chromosone in initial_population])

    def run(self):
        for _ in range(self.generations):
            self.__update_fitness()
            self.population = self.selection.apply(self.population)
            parents = self.pairing.apply(self.population)

    def __update_fitness(self):
        for chromosone in self.population:
            chromosone[1] = self.fitness(chromosone[0])

    def validate_config(self, config):
        if 'pairing' not in config.keys():
            config['pairing'] = 'tournament'
        if 'k' not in config.keys():
            config['k'] = 3
        if 'crossover' not in config.keys():
            config['crossover'] = 'single_point'
        if 'sample_rate' not in config.keys():
            config['sample_rate'] = 0.5
        if 'elitism' not in config.keys():
            config['elitism'] = 0
        if 'generations' not in config.keys():
            config['generations'] = 100


    
