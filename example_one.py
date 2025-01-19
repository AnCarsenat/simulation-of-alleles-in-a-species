from main import Species, Simulation
from matplotlib import pyplot as plt

initial_population = 40 # Adjust this value as needed this is how many individuals are in the start population
generations = 500 # Adjust this value as needed this is how many generations the simulation will run for
food_per_generation = 400  # Adjust this value as needed this is how much food is available per generation
alleles_data = {
    'Allele1': {'fitness_score': 5, 'mortality_rate': 0.1, 'reproduction_rate': 0.2}, # fitness_score is the number of times the allele is repeated in the weighted_population ==> How much likely he can eat food
    'Allele2': {'fitness_score': 2, 'mortality_rate': 0.1, 'reproduction_rate': 0.2}, # mortality_rate is the probability of the individual dying
    'Allele3': {'fitness_score': 2, 'mortality_rate': 0.1, 'reproduction_rate': 0.2}, # reproduction_rate is the probability of the individual reproducing
    'Allele4': {'fitness_score': 2, 'mortality_rate': 0.1, 'reproduction_rate': 0.2}  # survivability, mortality_rate, and reproduction_rate can be adjusted as needed
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
