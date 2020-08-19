import re

def txt_lines(filename):
    infile = open(filename)
    line_list = infile.readlines()
    infile.close()
    #print(line_list) #comment out !!!only for debugging purposes!!!
    return line_list

def print_script(word_list):
    for word in word_list:
        print(word)

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(key, value)
        print()

def check_special_chars(word_list):
    verified = {}

    for word in word_list:
        for char in word:
            if char not in 'abcdefghijklmnopqrstuvwxyz\n':
                verified[word] = True
                break    
   
    for word in word_list:
        if word not in verified:
            verified[word] = False

    return verified

def check_true_count(word_dict):
    true_count = 0
    for value in word_dict:
        if word_dict[value] == True:
            true_count += 1

    print(f'Dictionary Length: {len(word_dict)}')
    print(f'True count: {true_count}')


polish_word_list = ['abakańskich', 'abażurka', 'abażurki']

def create_regex_list(input_list):
    alphabet = 'abcdefghijklmnopqrstuvwxyz\n'
    regex_words = list()

    for word in input_list:
        char_list = list(word)
        for char in char_list:
            if char not in alphabet:
                char = "."
        regex_word = "".join(char_list)
        regex_words.append(regex_word)
    
    print(regex_words)

letter_nums = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d",
    5 : "e",
    6 : "f",
    7 : "g",
    8 : "h",
    9 : "i",
    10 : "j",
    11 : "k",
    12 : "l",
    13 : "m",
    14 : "n",
    15 : "o",
    16 : "p",
    17 : "q",
    18 : "r",
    19 : "s",
    21 : "t",
    22 : "u",
    23 : "v",
    24 : "w",
    25 : "x",
    26 : "y",

    }

def string_split(filename, new_file):
    word_list = txt_lines(filename)

    


#create_regex_list(polish_word_list)

####################################
######### tests for regex ##########
#word = "abaków"
#word1 = "abakow"
#word2 = "hello"

#x = re.search("abak.w", word)
#x1 = re.search("abak*w", word1)
#x2 = re.search("he..o", word2)
####################################


#####################################
### tests for check_special_chars ###

#print(f"Polish Words Length: {len(polish_words)}")
#print(f"Verified Dicionary Length: {len(words_dict)}")
#print()
#print(f"Length Test Passed: {len(polish_words) == len(words_dict)}")
#print_dict(words_dict)
#####################################


#####################################
### tests for check true count ###

#check_true_count(words_dict)
#####################################



