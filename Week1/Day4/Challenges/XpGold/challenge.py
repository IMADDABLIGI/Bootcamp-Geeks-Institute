import random

class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])

    def mutate(self):
        # Flip the gene (0 ↔ 1)
        self.value = 1 - self.value

    def __str__(self):
        return str(self.value)


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  # 50% chance to mutate each gene
                gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)

    def __str__(self):
        return ''.join(str(g) for g in self.genes)


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def is_all_ones(self):
        return all(chrom.is_all_ones() for chrom in self.chromosomes)

    def __str__(self):
        return '\n'.join(str(ch) for ch in self.chromosomes)


class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment  # Probability of mutation per generation

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_all_ones()


# --------- Simulation ---------

def evolve(environment=0.3, max_generations=10000):
    generations = 0
    organism = Organism(DNA(), environment)

    while not organism.is_perfect():
        generations += 1
        organism.mutate()
        
        if generations >= max_generations:
            print(f"Stopped after {generations} generations. Perfect DNA not achieved.")
            print("Last DNA state:")
            print(organism.dna)
            return

    print(f"\nEvolved to perfect DNA in {generations} generations!")
    print(organism.dna)


# Run the simulation
if __name__ == "__main__":
    evolve()
