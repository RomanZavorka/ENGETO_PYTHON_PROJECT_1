"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Roman Závorka
email: romanz90zero@gmail.com
discord: romanz90
"""

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
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
garpike and stingray are also present.'''
]

user_login = input("Please insert your username: \n")

if user_login in registered_users:
    if input(60*"-" + "\n"
            f"Please, insert your login password: \n"
        ) == registered_users[user_login]:
        print(f'{60*"-"} \n'
              f"Welcome to the app, {user_login}.\n"
              f"We have 3 texts to be analyzed.\n"
              f'{60*"-"}'
        )
        
        text_choice = str(input("Please enter a number btw. 1 and 3 to select: \n"))
        if text_choice.isnumeric() == True:
            text_choice = int(text_choice) - 1
        
        if text_choice in (0,1,2):
            TEXTS = TEXTS[text_choice]
            print(f'{60*"-"} \n'
                  f'You have chosen text number {text_choice + 1}:\n' 
                  f'"{TEXTS}" \n'
                  f'{60*"-"}'
            )

            titlecase_words = []
            uppercase_words = []
            lowercase_words = []
            numeric_strings = []

            for words in TEXTS.split(" "):
                for word in words.split("\n"):
                    contains_number = 0
                    for letter in word:
                        if letter.isnumeric() == True:
                            contains_number += 1
                    if word[0].isupper() == True:
                        titlecase_words.append(word)
                    if contains_number == 0:
                        if word.isupper() == True:
                            uppercase_words.append(word)
                        if word.islower() == True:
                            lowercase_words.append(word)
                    if word.isnumeric() == True:
                            numeric_strings.append(int(word))
            
            words_length = [[],[],[],[],[],[],[],[],[],[],[]]

            for words in TEXTS.split(" "):
                for word in words.split("\n"):
                    word = word.strip(".").strip(",")
                    if len(word) <= 11:
                        words_length[len(word)-1].append(word)
                    else:
                        words_length[10].append(word)

            print(f"There are {len(TEXTS.split())} words in the selected text.\n"
                  f"There are {len(titlecase_words)} titlecase words.\n"
                  f"There are {len(uppercase_words)} uppercase words.\n"
                  f"There are {len(lowercase_words)} lowercase words.\n"
                  f"There are {len(numeric_strings)} numeric strings.\n"
                  f"The sum of all the numeric strings is {sum(numeric_strings)}\n"
                  f"{60*'-'}\n"
                  f"LEN|{5*' '}OCCURENCES{5*' '}|NR."
            )

            words_sorted = 0

            for number in range(1, 11):
                word_length = 0
                for words in TEXTS.split(" "):
                    for word in words.split("\n"):
                        word = word.strip(".").strip(",")
                        if len(word) == number:
                            word_length += 1
                            words_sorted += 1
                if number == 10:
                    print(f"{1*' '}{number}|{word_length*'*'}{(20-word_length)*' '}|{word_length}")
                else:
                    print(f"{2*' '}{number}|{word_length*'*'}{(20-word_length)*' '}|{word_length}")
            
            print(f"11+|{(len(TEXTS.split()) - words_sorted)*'*'}" 
                  f"{(20-(len(TEXTS.split()) - words_sorted))*' '}"
                  f"|{(len(TEXTS.split()) - words_sorted)}"
            )

            print(60*"-")
            diplay_words = input(
                'Enter "y" to see lists of words by string type and length: \n'
            )
            
            if diplay_words.lower() == "y":
                def heading_break (offset, heading_text, break_length):
                    heading_text_length = len(heading_text)
                    print(f"{offset*'-'} {heading_text} "
                          f"{(break_length-heading_text_length-offset-2)*'-'}"
                    )

                print(60*"-")
                heading_break(3, "List of words by string type", 60)
                print(f"Titlecase words: {titlecase_words}\n"
                      f"Uppercase words: {uppercase_words}\n"
                      f"Lowercase words: {lowercase_words}\n"
                      f"Numeric strings: {numeric_strings}\n"
                      f"{60*'-'}"
                )
                
                heading_break(3, "List of words by length", 60)
                
                print(f"1 letter: {words_length[0]}")
                for number in range (1,10):
                    print(f"{number+1} letters: {words_length[number]}")
                print(f"11+ letters: {words_length[10]}")
        else:
            print(60*"-")
            print("Incorrect choice, shutting down.")
    else:
        print(60*"-")
        print("Incorrect password, terminating the program.")
else:
    print(60*"-")
    print("Unregistered user, terminating the program.")

