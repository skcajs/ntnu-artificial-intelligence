class Population:
    def __init__(self, chromosones: list):
        self.chromosones = chromosones

    def evaluate_fitness(self, fitness_fn):
        return fitness_fn(self.chromosones)
    
    def update_population(self, chromosones):
        self.chromosones = chromosones


class Chromosone:
    def __init__(self, gene: list):
        self.gene = gene
        self.fitness = None