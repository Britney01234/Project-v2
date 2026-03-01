# Had to add full pathway for VSC to be able to read and open the file.
def compare_sequences(dog_breed_database='C:\\Users\\15bcl\\Documents\\Bioinformatics\\Biocomputing\\Project Files\\project_dog_dna\\project_dog_dna\\dog_breeds.fa',mystery_dog_sequence='C:\\Users\\15bcl\\Documents\\Bioinformatics\\Biocomputing\\Project Files\\project_dog_dna\\project_dog_dna\mystery.fa'):
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
# If the line starts with '>', it indicates the start of a new dog breed. 
            if line.startswith('>'):
# Storing the current dog breed information to be used in the dictionary later.
                dog_str=line
# Everytime a new dog breed in found, the DNA variable is reset to an empty string.
                dog_dna=''
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
            if line.startswith('>')==False: 
# Adding the next line of the sequence to the string and removing unneceassy characters. 
                mystery_str+=line.strip()



    return mystery_str, dog_dictionary

compare_sequences()