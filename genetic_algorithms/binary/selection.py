class Selection:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate

    def apply(self, population):
        return sorted(population, key = lambda x: x[0], reverse = True)[:int(self.sample_rate*len(population))]
