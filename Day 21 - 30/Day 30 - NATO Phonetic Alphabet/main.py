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

# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
phonetic_alphabet_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
PAD_dict = {row.letter: row.code for (index, row) in phonetic_alphabet_dict.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def user_text():
    user_input = input("Enter a word: ").upper()
    try:
        user_list = [PAD_dict.get(char) for char in user_input]
        for ele in user_list:
            if ele != None:
                pass
            else:
                raise KeyError
    except KeyError:
        print("Only Alphabet in letters!")
        user_text()
    else:
        print(user_list)

user_text()




