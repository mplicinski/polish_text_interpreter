# polish_text_interpreter
A python script that converts a text file with plain polish text written into polish text that includes all necessary special characters that are part of the polish language.

This program takes input in the form of txt file that contains some text written in polish 
and converts all characters ment to be some special character ['ą', 'ć', 'ę', 'ł', 'ń', 'm', 'ó', 'ś', 'ź' 'ż']
from the regular characters ['a', 'c', 'e', 'l', 'n', 'm', 'o', 's', 'z']

The script is still a work in progress and is more a proof of concept as I want to run a web application with a python backend to serve this program.
The hope is that polish speakers who need to regularly write in polish can simply use the converter tool instead of using cumbersome online keyboards and
writing tools to write correctly in polish. 

The main function of the program is located at polish_text_interpreter_object_oreinted/text_interpret.py. It is ready to run as it as on a sample text file.

The polish_text_interpreter_tools/ directory contains scripts that I used to create the large text files match_words.txt and special_char_words.txt.
match_words.txt and special_char_words.txt are identical with the only difference being that special_char.words.txt contains all the words with the proper special polish characters in place.
match_words.txt is used to find words in your text that need to be converted and then matches it to possible options to be converted to in special_char_words.txt.
All those options are then shown to the user (the first option being to not convert the word adding no special characters) and the user may choose the correct one.