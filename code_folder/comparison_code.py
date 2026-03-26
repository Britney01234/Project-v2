import re
# Had to add full pathway for VSC to be able to read and open the file.
def dictionary_dogs(dog_breed_database='C:\\Users\\15bcl\\Documents\\Bioinformatics\\Biocomputing\\Project Files\\data_folder\\project_dog_dna\\dog_breeds.fa',mystery_dog_sequence='C:\\Users\\15bcl\\Documents\\Bioinformatics\\Biocomputing\\Project Files\\data_folder\\project_dog_dna\\mystery.fa'):# Correct filepath can be found below in a comment. 

#def dictionary_dogs(dog_breed_database='../data_folder/dog_breeds.fa',mystery_dog_sequence='../data_folder/mystery.fa'):

# Defines variable as an empty dictionary to store the dog breed information from the database.
    dog_dictionary = {}
# Opens the dog breed database file. 
    with open(dog_breed_database, 'r') as f_dog_database: 
# Defines variable as an empty string to add into dictionary later.
        dog_str=''
# Defines variable as an empty string to add into dictionary later.
        dog_dna=''
# Loops over file one line at a time until the nd of the file.   
        for line in f_dog_database:
# Removes any whitespace.
            line=line.strip()
# If the line starts with '>', it indicates the start of a new dog breed. 
            if line.startswith('>'):
# Making it so only the dog breed and isolate name appear in the dictionary key.
                breed_match = re.search(r"breed[=\s]([A-Za-z0-9_-]+)", line)
                isolate_match = re.search(r"isolate[=\s]([A-Za-z0-9_-]+)", line)
                breed = breed_match.group(1) if breed_match else ""
                isolate = isolate_match.group(1) if isolate_match else ""
# Storing the current dog breed information to be used in the dictionary later.
                dog_dna=''
# Everytime a new dog breed in found, the DNA variable is reset to an empty string.
                dog_str=f"{breed},{isolate}"
# Adding a new empty entry called dog_str to the dictionary.
                dog_dictionary[dog_str]=dog_dna
            else:
# If the line does not start with '>', it is part of the DNA sequence for the current dog breed. 
                dog_dna+=line.strip()
# After processing the line, the DNA sequence is updated in the dictionary for the current dog breed.
                dog_dictionary[dog_str]=dog_dna
# Opens the mystery dog sequence file.
    with open(mystery_dog_sequence, 'r') as f_mystery_dog:
# Defines variable as an empty string to have the mystery dog DNA sequence stored in it.
        mystery_str=''
# Loops over file one line at a time until the end of the file.
        for line in f_mystery_dog:
# Ignoring the first line of the mystery sequence as it isn't part of the DNA sequence needed to be compared.
            for line in f_mystery_dog:
                if not line.startswith(">"):
# Adding the next line of the sequence to the string and removing unneceassy characters. 
                   mystery_str += line.strip()

    return mystery_str, dog_dictionary
# Outputs dcitionary as expected, includes mystery sequence on top, underneath shows the various dog breeds with their sequences, can be seen in the terminal. 
# Not sure what wrriten test would be required for this, maybe come back and look at it if time. 


from scipy import stats 

def compare_sequences(mystery_sequence_for_comparison, dog_dictionary_for_comparison):
# Defines variable as an empty dictionary to store the percent identity values for each dog breed.
    percent_identity_dictionary = {}
# Loops through the dictionary until the end of the dictionary is reached.
    for dog_breed in dog_dictionary_for_comparison:  
# Defines variable as an empty string to store the DNA sequence for the current dog breed being compared.
        dog_breed_dna = dog_dictionary_for_comparison[dog_breed]  
# Defines variable as an integer to count the number of matching characters between the mystery sequence and the current dog breed sequence.
        match_count = 0
# Defines variable of the sequence length to compare it and find percntage idenity.
        seq_length = min(len(mystery_sequence_for_comparison), len(dog_breed_dna))
# Loops through the DNA sequence of the current dog breed and compares it to the mystery sequence one character at a time.
        for i in range(seq_length):
# If the characters at the current position in both sequences match, the match count is incremented by 1.
            if mystery_sequence_for_comparison[i] == dog_breed_dna[i]: 
                match_count += 1
# Calculates the p values to be later stored in the dictionary.
        p_value= stats.binom.sf(match_count-1,seq_length,0.25)
# After comparing the sequences, the percent identity is calculated by dividing the match count by the length of the shorter sequence and multiplying by 100 to get a percentage.
        percent_identity = (match_count / seq_length) * 100
# The percent identity value is stored in the percent identity dictionary with the dog breed as the key and the percent identity as the value.
        percent_identity_dictionary[dog_breed] = (percent_identity,p_value,match_count)
# After all dog breeds have been compared, the percent identity dictionary is returned.
    
    return percent_identity_dictionary

mystery, dog_dictionary = dictionary_dogs()
results = compare_sequences(mystery, dog_dictionary)

def highest_percent_identity(percent_identity_dictionary_for_comparison):
# Defines variable as an empty string to store the dog breed with the highest percent identity.
    highest_percent_identity_dog = ''   
# Defines variable as a float to store the highest percent identity value found during the comparison.
    highest_percent_identity_value = 0.0
# Loops through the percent identity dictionary until the end of the dictionary is reached.
    for dog_breed, (percentage , p_value, _) in percent_identity_dictionary_for_comparison.items():
# If the percent identity value for the current dog breed is higher than the highest percent identity value found so far, the highest percent identity value and the corresponding dog breed are updated.
        if percentage > highest_percent_identity_value:
            highest_percent_identity_value = percentage
            highest_percent_identity_dog = dog_breed
# After looping through all the dog breeds, the dog breed with the highest percent identity and its corresponding percent identity value are returned as a tuple.       

    return highest_percent_identity_dog, highest_percent_identity_value

import math
import os
os.makedirs("../results_folder", exist_ok=True)

# Opening a new file to write in.
with open ("../results_folder/dog_results.txt", "w") as f:
# Write the string into the blank file.
    f.write("DNA Comparison Results\n")
# Creating a separation between title and data, as well as putting it on a new line.
    f.write("-"*30+"\n")
# At the end of the result, a new line is created.
    for breed, (percentage,p_value,match_count) in results.items():
# Adding p values into the file, ensuring that the value goes back enough to show numbers rather than 00e.
        if p_value > 0:
            exponent = abs(int(match_count*math.log10(0.25)))
            p_display = f"1.00e-{exponent}"
        else:
            approx_log = abs(match_count * math.log10(0.25))
            p_display = f"< 1e-{int(approx_log)} (Significant)"
        f.write(f"{breed.strip()}:{percentage:.2f}% | p-value: {p_display}\n")
best_dog, best_percentage = highest_percent_identity(results)
# Prints out the cloest match and percentage in the terminal more clearly. 
print(f"Closest match found: {best_dog} at {best_percentage:.2f}%")
# Function called.
dog_results = dictionary_dogs()
compare_sequences(dog_results[0], dog_results[1])
# Outputs file as txt file as expected, can be seen in results_folder.
percent_identity_results = compare_sequences(dog_results[0], dog_results[1])
percentage_results = highest_percent_identity(percent_identity_results)


import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import FormatStrFormatter 

def plot_percent_identity(percent_identity_dictionary_for_plotting):
# Defines variable as an empty list to store the dog breeds for the x-axis of the plot.
    dog_breeds = []
# Defines variable as an empty list to store the percent identity values for the y-axis of the plot.
    percent_identity_values = []
    
# Loops through the percent identity dictionary until the end of the dictionary is reached.
    for dog_breed in percent_identity_dictionary_for_plotting:
        percentage, _, _ = percent_identity_dictionary_for_plotting[dog_breed]
# Appends the current dog breed to the dog breeds list and its corresponding percent identity value to the percent identity values list.
        dog_breeds.append(dog_breed)
        percent_identity_values.append(percentage) 
# Creates a bar plot using the dog breeds as the x-axis and the percent identity values as the y-axis.
    plt.figure(figsize=(12,6))
# Increasing decimal place value on y axis to have the bars be more distinct.
    min_val = min(percent_identity_values)
    max_val = max(percent_identity_values)
    diff=max_val-min_val
    if diff >0:
        plt.ylim([min_val - (diff*0.1),max_val+(diff*0.1)])
    else:
        plt.ylim([min_val - 0.0001, max_val + 0.0001])
    plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.5f'))
# Creates the bars.
    plt.bar(dog_breeds, percent_identity_values,width=0.5)
# Sets the title and labels for the plot, including font size.
    plt.title('Percent Identity of Mystery Dog to Each Dog Breed')
    plt.xlabel('Dog Breeds')
    plt.ylabel('Percent Identity (%)')
    plt.xticks(fontsize = 6,rotation=50,ha="right")
    plt.yticks(fontsize=8)
    plt.tight_layout()
# Displays the plot.
    plt.savefig('../results_folder/Graph_of_dog.png')
    plt.show()
 
    return percent_identity_dictionary_for_plotting
# Outputs bar chart as expected, can be seen in results_folder. 
plot_percent_identity(percent_identity_results)

from scipy import stats 

def calculate_p_value(match_count, total_length):
# Creates a null hypothesis of 1 in 4 chance/
    prob_random_match = 0.25
    
# Want to know the probability of how many success match_count will have.
    p_val = stats.binom.sf(match_count - 1, total_length, prob_random_match)
    return p_val

# Test to ensure p value is able to output a number other than 00.00e
print(f"Test P-Value: {calculate_p_value(5, 20):.4f}")