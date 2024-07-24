# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv", index_col=False)

dictu={value[0]:value[1] for key, value in df.iterrows()}
print(dictu)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

User=list(input("Enter a word : ").upper())
output=[dictu[x] for x in User ]
print(output)

