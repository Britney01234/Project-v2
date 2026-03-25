#### Project V2 ####


Functions Present in comparison_code:

- First function creates a dictionary of the dog breeds found in the data file dog_breeds.fa, and extracts the DNA sequence from the data file mystery.fa (dictionary_dogs).
- Second function creates a dictinoary of similiarity percentage between the mystery sequence and each dog breed found in the dictionary (compare_sequences).
- Third function finds the most similar sequence via the highest percentage (highest_percentage_identity).
- Fourth function creates a bar chart and saves it as a file in results_folder (plot_percnetage_identity).
- Fifth function creates the p values for the different identity matches (calculate_p_value). 

Includes script to output dictionary into a new file that can be found in results_folder.


Tests and functions present in test_comparison_code:
- Tests for compare_sequences -- one test to compare the mystery sequence to an exact copy to ensure it outputs 100% identity match, which has been placed into a txt file in the folder, second test to compare the sequence to a false sequence to ensure it outputs a 0% indentity match.
- Tests for highest_percentage_identity -- using pytest, one test creates a sample dictionary to ensure highest percentage is being outputted, second test to ensure that, if the dicitionary is empty, a empty sequence and 0% identity is output, third test to see how the function behaves if the percentage match is the same, the test ensures that the function would output the first one it came across.
- Tests for calculate_p_value -- using pytest, one test to ensure the p values are as expected using a simple sample, second test to ensure that if the count is 0, the probability of the answer being more than 0 should be 1.
- Test for dicitonary_dogs -- using pytest, creates a false dictionary and false mystery sequence to ensure that it parses the dicitoanry as expected. 