# author
"""
author = Martin Kucirek
email = martin.kucirek89@gmail.com
Discord = Martin K.#3205
"""
# TEXTS
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

#registred users
reg_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# initialization of variables
separator = "-" * 40
title_words = 0
upper_words = 0
lower_words = 0
num_strings = []
words_dict = {}

# login
username = input("username")
password = input("password")
if (username, password) in reg_users.items():
    print(separator, 'Welcome to the app, ' + username, 'We have 3 texts to be analyzed.', separator, sep='\n')
else:
    print("unregistered user, terminating the program..")
    quit()


# choice of text
txt_choice = input("Enter a number btw. 1 and 3 to select: ")
if not txt_choice.isnumeric() or int(txt_choice) not in range(1, 4):
    print("Wrong number, terminating the program..")
    quit()

# statistics - no. of words
split_text = (TEXTS[int(txt_choice)-1]).split()
clean_words = [word.strip(".,-:!?") for word in split_text]
print(f'There are {len(split_text)} words in the selected text.')

# statistics - titlecase words, uppercase, lowercase, number strings, sum of numbers
title_words = 0
upper_words = 0
lower_words = 0
num_strings = []

for clean_word in clean_words:
    for letter in clean_word:
        if letter.isupper():
            title_words += 1
    if clean_word.isupper() and clean_word.isalpha():
        upper_words += 1
    elif clean_word.islower():
        lower_words += 1
    elif clean_word.isnumeric():
        num_strings.append(int(clean_word))

# statistics - occurrences
words_dict = {}

for clean_word in clean_words:
    length_word = len(clean_word)
    if length_word not in words_dict:
        words_dict[length_word] = 1
    else:
        words_dict[length_word] += 1

# Print the first set of statistics
print(
    f'There are {title_words} titlecase words.',
    f'There are {upper_words} uppercase words.',
    f'There are {lower_words} lowercase words.',
    f'There are {len(num_strings)} numeric strings.',
    f'The sum of all numbers {sum(num_strings)}.',
    sep="\n"
)

# Print the second set of statistics with column graphs
separator = '-' * 26
print(
    separator,
    f'{"LEN":>3}|{"OCCURRENCES":^18}|{"NR.":<3}',
    separator,
    sep="\n"
)

for x in range(1, max(words_dict.keys()) + 1):
    occurrences = words_dict.get(x, 0)
    print(f'{x:>3}|{"*" * occurrences:<18}|{occurrences:<3}')
