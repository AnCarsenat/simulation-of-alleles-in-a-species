import random
import matplotlib.pyplot as plt

class Individual:
    def __init__(self, allele, parents=None):
        self.allele = allele
        self.parents = parents

    def destroy(self):
        if self.parents and self in self.parents:
            self.parents.remove(self)

class Species:
    def __init__(self, initial_population, alleles_data, food_per_generation):
        self.population = [Individual(random.choice(list(alleles_data.keys()))) for _ in range(initial_population)]
        self.alleles_data = alleles_data
        self.food_per_generation = food_per_generation
        self.population_history = []

    def grow(self):
        # Apply mortality rate
        survivors = []
        for individual in self.population:
            mortality_rate = self.alleles_data[individual.allele]['mortality_rate']
            if random.random() > mortality_rate:
                survivors.append(individual)
        self.population = survivors

        # Check if species is extinct
        if len(self.population) < 2:
            print("Species has gone extinct.")
            self.population = []
            return

        # Food distribution
        food = self.food_per_generation
        weighted_population = sorted(self.population, key=lambda ind: self.alleles_data[ind.allele]['survivability'], reverse=True)
        self.population = []
        for individual in weighted_population:
            if food > 0:
                self.population.append(individual)
                food -= 1

        # Apply reproduction rate
        new_individuals = []
        for individual in self.population:
            reproduction_rate = self.alleles_data[individual.allele]['reproduction_rate']
            if random.random() < reproduction_rate:
                weighted_alleles = [allele for allele, data in self.alleles_data.items() for _ in range(data['survivability'])]
                new_individuals.append(Individual(random.choice(weighted_alleles), parents=new_individuals))
        self.population.extend(new_individuals)

        # Record population size
        self.population_history.append(len(self.population))

    def __str__(self):
        allele_count = {allele: 0 for allele in self.alleles_data}
        for individual in self.population:
            allele_count[individual.allele] += 1
        return f"Species: {allele_count}"
    
    destroy = lambda self: [individual.destroy() for individual in self.population]

class Simulation:
    def __init__(self, species_list, generations):
        self.species_list = species_list
        self.generations = generations

    def run(self):
        for generation in range(self.generations):
            print(f"Generation {generation + 1}")
            for species in self.species_list[:]:
                species.grow()
                if len(species.population) < 2:
                    print("Simulation ended early for a species due to extinction.")
                    species.destroy()
                    self.species_list.remove(species)
            if not self.species_list:
                print("All species have gone extinct.")
                break
            for species in self.species_list:
                print(species)
            print()

        # Plotting the population history
        for species in self.species_list:
            plt.plot(species.population_history, label=str(species))
        plt.xlabel('Generations')
        plt.ylabel('Population Size')
        plt.title('Population Size Over Generations')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    initial_population = 40
    generations = 500
    food_per_generation = 400  # Adjust this value as needed
    alleles_data = {
        'Allele1': {'survivability': 2, 'mortality_rate': 0.1, 'reproduction_rate': 0.2},
        'Allele2': {'survivability': 2, 'mortality_rate': 0.1, 'reproduction_rate': 0.2},
        'Allele3': {'survivability': 2, 'mortality_rate': 0.1, 'reproduction_rate': 0.2},
        'Allele4': {'survivability': 2, 'mortality_rate': 0.1, 'reproduction_rate': 0.2}
    }

    species_list = [Species(initial_population, alleles_data, food_per_generation)]
    simulation = Simulation(species_list, generations)
    simulation.run()

    # Collect data for plotting
    generation_numbers = list(range(1, generations + 1))
    data = {allele: [] for allele in alleles_data}

    # Reset the species for data collection
    species = Species(initial_population, alleles_data, food_per_generation)

    for generation in generation_numbers:
        allele_count = {allele: 0 for allele in alleles_data}
        for individual in species.population:
            allele_count[individual.allele] += 1
        for allele, count in allele_count.items():
            data[allele].append(count)
        species.grow()
        if len(species.population) < 2:
            species.destroy()

    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 8))

    for allele in alleles_data:
        ax.plot(generation_numbers[:len(data[allele])], data[allele], label=allele)

    ax.set_title("Species Allele Distribution Over Generations")
    ax.legend()
    plt.xlabel('Generations')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
