# Project-v2

Aim of project:
- compare a sequence of DNA (see dog_breeds.fa) to the one provided (see mystery.fa  in data folder) 
- code should produce the most similiar sequence AND the difference between the result and the provided sequence 

Additional aims:
- look at possibilities across databases
- create p-values
- reconstruct phylogeny



Functions Present in comparison_code:
- First function creates a dictionary of the dog breeds found in the data file dog_breeds.fa, and extracts the DNA sequence from the data file mystery.fa
- Second function creates a dictinoary of similiarity percentage between the mystery sequence and each dog breed found in the dictionary. 
- Third function finds the most similar sequence via the highest percentage. 
- Fourth function outputs the results in results_folder, results. 