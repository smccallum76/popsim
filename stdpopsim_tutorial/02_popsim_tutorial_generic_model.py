"""
Review stdpopsim tutorial - part 2 - generic model
The generic model will be a model that uses default or user defined settings (i.e., not a published study)

https://popsim-consortium.github.io/stdpopsim-docs/stable/tutorial.html
"""
# sloppy, but the 'warnings' module ignores a couple future warnings in stdpopsim
import warnings
warnings.filterwarnings("ignore")
import stdpopsim

""" 
------------------------------------------------------------------------------------------------------------------------
SPECIES SELECTION
Select the species (humans)
------------------------------------------------------------------------------------------------------------------------
"""
print("-----------------------------------------------------------------------------")
print("SPECIES SELECTION")
print("-----------------------------------------------------------------------------")
species = stdpopsim.get_species("HomSap") # same process as 01_ tutorial

""" 
------------------------------------------------------------------------------------------------------------------------
SET UP GENERIC MODEL
A piecewise constant population size is used (over multiple epochs). Not sure exactly what this means, only that a 
piecewise approach implies that the model might vary through time. 
------------------------------------------------------------------------------------------------------------------------
"""
print("-----------------------------------------------------------------------------")
print("SET UP GENERIC MODEL")
print("-----------------------------------------------------------------------------")
# each species has default population_size, for humans it is 10K
model = stdpopsim.PiecewiseConstantSize(species.population_size)

""" 
------------------------------------------------------------------------------------------------------------------------
CHOOSE A CONTIG AND RECOMBINATION MAP
Any chromosome could be selected, or a fraction of a chromosome. However, in this example a generic contig that is
length 1Mb and uses a constant recombination rate that is the avg rate over all chromosomes for a the species. 
------------------------------------------------------------------------------------------------------------------------
"""
print("-----------------------------------------------------------------------------")
print("CHOOSE A CONTIG AND RECOMBINATION MAP")
print("-----------------------------------------------------------------------------")

contig = species.get_contig(length=1e6)
print("Contig length (base pairs): ", contig.recombination_map.sequence_length)
print("Mean recombination rate: ", contig.recombination_map.mean_rate)  # this flat or constant over time
print("Mutation rate for generic pop: ", contig.mutation_rate)  # default rate for the species

""" 
------------------------------------------------------------------------------------------------------------------------
CHOOSE A SAMPLING SCHEME AND SIMULATE
Set the number of samples to 5 diploids (10 haploids) and set the simulation engine (msprime). There is only
one population for generic PiecwiseConstantSize called pop_0, but sample size can be very large with msprime. 
------------------------------------------------------------------------------------------------------------------------
"""
print("-----------------------------------------------------------------------------")
print("CHOOSE A CONTIG AND RECOMBINATION MAP")
print("-----------------------------------------------------------------------------")

# NEED TO ADD THIS CODE FROM THE TUTORIAL
y=1

