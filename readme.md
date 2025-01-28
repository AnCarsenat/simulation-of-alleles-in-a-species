![Figure_1](https://github.com/user-attachments/assets/cbddc2eb-0a72-4aa0-b4cd-ff7e3a5b9721)
# Simulation of Alleles in a Species
a md template ;-;

This project simulates the distribution of alleles in a species over time. It uses various parameters to model genetic drift, selection, mutation, and migration.
If you to try with no instalation ==> [CLIK HERE FOR JUPITER LAB](https://jupyter.org/try-jupyter/lab/index.html?path=notebooks%2FIntro.ipynb)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
Understanding the genetic variation within a species is crucial for studying evolution and population genetics. This simulation provides insights into how alleles change frequency over generations under different evolutionary forces.

## Features
- [X] **Genetic Drift**: Random changes in allele frequencies.
- [X] **Selection**: Differential survival and reproduction.
- [ ] **Mutation**: Introduction of new alleles.
- [X] **Migration**: Movement of individuals between populations.

## Installation
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
To run the simulation, use the following command:
```bash
python simulate.py --config config.yaml
```
You can customize the simulation parameters by editing the `example_one.py` file.

## Nice images
example of an ecosystem where no allele is advantageous
<img src="https://github.com/user-attachments/assets/6c618d33-3ed4-4f7b-9ed4-3c2db62fa806" alt="example1_speciesSize" width="500"/>  
<img src="https://github.com/user-attachments/assets/fbf2d0a7-6109-4ecc-a1f0-04cec9bec33c" alt="example1_speciesAlleleDistribution" width="500"/>  
example of an fit allele : 
```python
'Allele1': {'fitness_score': 5, 'mortality_rate': 0.1, 'reproduction_rate': 0.5}
```  
<img src="https://github.com/user-attachments/assets/bfe9c855-2c4d-41b3-b4fa-047ce96722a2" alt="example2_speciesSize" width="400"/>  
<img src="https://github.com/user-attachments/assets/5ca9fbd4-7731-4823-9cf4-caa3be966e1b" alt="example12_speciesAlleleDistribution" width="400"/>  




