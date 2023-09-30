"""
Review stdpopsim tutorial

https://popsim-consortium.github.io/stdpopsim-docs/stable/tutorial.html
"""
# sloppy, but the 'warnings' module ignores a couple future warnings in stdpopsim
import warnings
warnings.filterwarnings("ignore")
import stdpopsim as std

""" 
------------------------------------------------------------------------------------------------------------------------
SPECIES AND DEMOGRAPHIC MODELS
Select the species, review the demographic models from the species, and inspect the selected demographic model
------------------------------------------------------------------------------------------------------------------------
"""
print("-----------------------------------------------------------------------------")
print("SPECIES AND DEMOGRAPHIC MODELS")
print("-----------------------------------------------------------------------------")
species = std.get_species("HomSap")  # select humans

for x in species.demographic_models:  # take a look at the model options
    print(x.id)

model = species.get_demographic_model("OutOfAfrica_3G09")  # pick a demoographic model for humans
print("pops: ", model.num_populations)  # number of populations
print("sample pops: ", model.num_sampling_populations)  # num of populations from which you can sample
print("pop names \n", [pop.name for pop in model.populations])  # name of each of the populations

""" 
------------------------------------------------------------------------------------------------------------------------
SET UP THE CONTIG
A 'contig' is segment of sequencing that overlaps with another segment. A collection of overlapping contigs are used
to make up a contiguous genetic sequence.  
------------------------------------------------------------------------------------------------------------------------
"""
print("\n", "-----------------------------------------------------------------------------")
print("CONTIG")
print("-----------------------------------------------------------------------------")

contig = species.get_contig("chr22")  # chromosome 22 (~51M base-pairs, immune system, mental disorders...)
# default is a flat genetic map
print("mean recombination rate: ", f"{contig.recombination_map.mean_rate:.3}")
# default mutation rate is based on teh species default
print("mean mutation rate (default rate): ", contig.mutation_rate)
# note that the mutation rate differs from the model's assumed rate
print("model mutation rate: ", model.mutation_rate)

# Mutation rate matters, and the rate from a study specific to the population of interest should supersede the
# stdpopsim default rate. This modification to contig is shown below.
contig = species.get_contig("chr22", mutation_rate=model.mutation_rate)
print("mean mutation rate from the demographic model: ", contig.mutation_rate)
print(contig.mutation_rate==model.mutation_rate)