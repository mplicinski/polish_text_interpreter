#Polish word document interpreter
#Takes a word document with Polish text without the polsih letters 
#a vs ą or z vs ż
#Then generates a word document with the same Polish text but with the correct Polish letters added
#['ą', 'ć', 'ę', 'ł', 'ń', 'm', 'ó', 'ś', 'ź' 'ż']

#by Matthew Plicinski 

#imports
import re

#return a list of lines froma .txt file (with '\n' newline character)
def txt_lines(filename):
    infile = open(filename)
    line_list = infile.readlines()
    infile.close()
    #print(line_list) #comment out !!!only for debugging purposes!!!
    return line_list

#returns a list of lines from a txt file (without '\n' newline character )
def txt_lines_no_newline(filename):
    infile = open(filename)
    line_list = infile.read().splitlines()
    infile.close()
    return line_list

#returns a list of words in a txt file
def get_dictionary_word_list(filename):
    infile = open(filename)
    with open(filename) as f:
        return f.read().split()

#print words from a list
def print_words_list(word_list):
    for word in word_list:
        print(word)

#writes to a txt file. 
#to_write = input to be written to the file.
#new_file = file to be written to 
def write_words(to_write, new_file):
    write_file = open(new_file,'w')
    write_file.write(to_write)
    write_file.close()

#removes words that do not contain at least one special character as seen in special_chars
def remove_nonspecial_char_words(filename, new_file):
    word_list = txt_lines(filename)
    alphabet = 'abcdefghijklmnopqrstuvwxyz\n'
    words_special_chars = set()     #create a set of words with special characters to avoid duplicate words
    special_word_count = 0

    for word in word_list:              #loop through the full list of wordsw
        for char in word:      #loop through the set of special characters
            if char not in alphabet:            #if there is a special character within the word
                words_special_chars.add(word)       #add it to the set
                #print(word)                      #!!for debugging purposes!! commnet out when not needed
                special_word_count += 1
                break                        
 
    
    words_special_list = list(words_special_chars)
    words_special_list.sort()
    words_string = ''.join(words_special_list)
    #print(special_word_count)

    write_words(words_string, new_file)  #use the write_words() to write  

#this fucntion is obselete
def create_regex_file(filename, new_file):
    word_list = txt_lines(filename)
    alphabet = 'abcdefghijklmnopqrstuvwxyz\n'
    regex_words = list()

    for word in word_list:
        i = 0
        char_list = list(word)
        for char in char_list:
            if char not in alphabet:
                char_list[i] = "."
            i += 1
        regex_word = "".join(char_list)
        regex_words.append(regex_word)

    regex_words_string = ''.join(regex_words)
    print(regex_words)
    write_words(regex_words_string, new_file)

#create_regex_file('polish_words_sample_output.txt', "regex_words_sample.txt")

def create_special_match_file(filename, new_file):
    word_list = txt_lines(filename)
    match_words = list()

    for word in word_list:
        i = 0
        char_list = list(word)
        for char in char_list:
            if char == "ą":
                char_list[i] = 'a'
            if char == "ć":
                char_list[i] = 'c'
            if char == "ę":
                char_list[i] = "e"
            if char == "ł":
                char_list[i] = "l"
            if char == "ń":
                char_list[i] = "n"
            if char == "ó":
                char_list[i] = "o"
            if char == "ś":
                char_list[i] = "s"
            if char == "ź":
                char_list[i] = "z"
            if char == "ż":
                char_list[i] = "z"
            i += 1
        match_word = "".join(char_list)
        match_words.append(match_word)
    
    match_words_string = "".join(match_words)
    print(match_words_string)
    write_words(match_words_string, new_file)


#dictionary version not working (dictionary too big I think)
def convert_words(filename, new_file):
    match_words = txt_lines_no_newline("match_words.txt")
    polish_words = txt_lines_no_newline("polish_words_output.txt")
    
    polish_dict = {}
    for key in match_words:
        for value in polish_words:
            polish_dict[key] = value
            polish_words.remove(value)
            break
    
    for key, value in polish_dict.items():
        print(key, value)
    #print(polish_dict)

def convert_words_lists(filename, new_file):
    match_words = txt_lines_no_newline("match_words.txt")
    polish_words = txt_lines_no_newline("polish_words_output.txt")

    for word in match_words:
        return 0


#match_words = txt_lines_no_newline("match_words.txt")
#print(match_words)


print()
convert_words("polish_letter.txt", "polish_letter_output.txt")
print()

#words = get_dictionary_word_list("polish_letter.txt")
#words_polish = get_dictionary_word_list("polish_letter_translated.txt")

#create_special_match_file("polish_words_output.txt", "match_words.txt")

#['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź' 'ż']
#create a dictionary with each word matching
#if char == "ó", char == o