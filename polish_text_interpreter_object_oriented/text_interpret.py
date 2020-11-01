### Polish txt file interpreter ###
### This program takes input in the form of txt file that contains some text written in polish 
#   and converts all characters ment to be some special character ['ą', 'ć', 'ę', 'ł', 'ń', 'm', 'ó', 'ś', 'ź' 'ż']
#   from the regular characters ['a', 'c', 'e', 'l', 'n', 'm', 'o', 's', 'z']
### By Matthew Plicinski ###

import string
import re

class polish_txt:

    def __init__(self, filename):

        word_regex = re.compile(r'[a-zA-Z]+') #regex object that matches only words in strings

        #create word list from txt to be interpreted
        with open(filename) as infile:
            text = infile.read()
        infile.close()

        word_regex = re.compile(r'[a-zA-Z]+')   #regex expression to find words only (no numbers)
        word_list = word_regex.findall(text)

        self.capatalized_words = word_list      #list of words with some words capatalized (depending on how they appear in the original text)

        word_list = [item.lower() for item in word_list]        #convert all words to be lower case
        self.words = word_list                                  #copy of the original list of words in the txt file

        #create a string of the text as it appear in the original text with all capitilization, formatting, and punctuation
        infile = open(filename)
        original_text = infile.read()
        self.original_text = original_text        

        #creating a list of polish word -WITHOUT- special characters to match with words in the text to be converted
        match_words_infile = open('match_words.txt')
        match_words_list = match_words_infile.read().splitlines()
        match_words_infile.close()
        self.match_words = match_words_list

        #creating a list of polish words -WITH- special characters to swap into the original text
        special_char_words_infile = open('special_char_words.txt')
        polish_words = special_char_words_infile.read().splitlines()
        special_char_words_infile.close()
        self.polish_words = polish_words

    ### The following 3 functions are the main functions of program that do the bulk of the work

    #replace the words in self.words that need special characters
    #unnecessarily bloated becuase there is a command line interaction loop for choosing the correct version of each word that needs to be converted 
    def convert_words(self):
        match_indexes_list = []             #list of lists, where each list contains the indexes of words that match the current word (w) in self.match_words     
        words_to_convert_indexes = []       #list to save indexes of words that need to be converted in self.words #set to avoid duplicates        

        for w in range(len(self.words)):                #loop through the list of lowercase words from original text

            match_indexes = []                          #list of match indexes for the current word #if there is/are matche(s) matches_indexes will be added to match_indexes_list
            for mw in range(len(self.match_words)):     #mw = match_word #looping through the entire match word dictionary looking for matches    

                if self.words[w] == self.match_words[mw]:       #if the current word matches a word in the match dictionary
                    match_indexes.append(mw)                    #add the index of the matched word into match_indexes
    
            if len(match_indexes) > 0:                          #if there are any matches 
                match_indexes_list.append(match_indexes)        #add the list of match indexes for the 
                words_to_convert_indexes.append(w)              #add the index of the word in self.words to a list of all the convert indexes
                
        ### PROOF OF CONCEPT ###
        ### The rest of this function's code loops through all the words that need to be converted and asks the user what version of the word should be used
        ### This will need to be recreated into some kind of pop up dialouge box in the web application 
        ### Pretty ugly but it works for using the program in the terminal        

        for i in range(len(words_to_convert_indexes)):

            convert_index = words_to_convert_indexes[i]

            print(f"Please choose one of the following options for {self.words[convert_index]}")
            print(f"1: {self.words[convert_index]}")
            index = 2
            for mi in match_indexes_list[i]:
                print(f"{index}: {self.polish_words[mi]}")
                index = index + 1
            user_choice = input("Enter a number: ")
            print()

            user_choice = int(user_choice)

            while user_choice - 1  > len(match_indexes_list[i]):
                print("Please type a valid number")
                user_choice = input("Enter a number: ")
                user_choice = int(user_choice)

            if user_choice == 1:
                print(self.words[convert_index])
            else:
                true_choice = user_choice - 2
                correct_index = match_indexes_list[i][true_choice]
                print(self.polish_words[correct_index])
            print()

            if user_choice > 1:
                self.words[convert_index] = self.polish_words[correct_index]

    
    #check for capital letters in self.capatalized_words and capatalize any characters in self.words that should be capatalized
    def restore_case(self):
        for w in range(len(self.capatalized_words)):    #using ints to loop through the list of words that we can access the same word in both lists with one iterator
            word = self.capatalized_words[w]            #save the current word to a variable -word- for easy accessing of the current word in the rest of the function 
           
            for c in range(len(word)):                  #loop through every character in the word again using an int iterator so that we can access the same character in both versions of the word
                if word[c].isupper():                   #if a character is uppercase
                    result = self.words[w]              #save the current word (with a character that needs to be capatalized) to a variable -result-
                    chars = list(result)                #convert the word into a list of characters -chars-
                    chars[c] = chars[c].upper()         #set the char -c- to uppercase
                    result = ''.join(chars)             #join the character list back into a string -resutl-
                    self.words[w] = result              #set the current word equal to our new upper cased word stored in result
        
    #Insert polish words into original formatted text
    def insert_polish_words(self):

        polish_char_words = self.strip_nonspecial_char_words(self.words)
        replacement_indexes = self.polish_word_indexes()

        converted_text = self.original_text
        print(converted_text)                   #prints the full formated text before being converted #for debugging purposes

        for i in range(len(polish_char_words)):
            word_to_replace = self.capatalized_words[replacement_indexes[i]]                #find the word to replace by accessing each replacement index with the iterator
            word_speical_chars = polish_char_words[i]                                       #get the word we will be using to replace the original word
            converted_text = converted_text.replace(word_to_replace, word_speical_chars)    #use string.replace() method to swap in the correct polish word

        print()                                 
        print(converted_text)                   #prints the full formated text after being converted



    ### HELPER FUNCTIONS BELOW THAT ARE USED IN OTHER FUNCTIONS ###

    #Function that strips self.words down to only the words that contain special characters (these are the only words we have to replace)
    def strip_nonspecial_char_words(self, all_words):
        polish_char_words = []                      #create a list to store the words from the text that have special polish characters in them
        for word in self.words:

            for char in word:                       #loop through the characters in the word
                if char in 'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ':    #check each char against a list of each special char in the polish language
                    polish_char_words.append(word)
                    break                           #break out of the character loop so that if a word has mutiple special characters it is not added to the list twice
        
        return polish_char_words                    #return a list of only the words that have special chars in them

    #Function to get indexes of words that need to be converted
    def polish_word_indexes(self):
        polish_char_words = self.strip_nonspecial_char_words(self.words) #create a list that only contains words with special characters
        indexes = []

        i = 0       #iterator for all words appearing the original text 
        j = 0       #iterator for words with special characters
    
        while j < (len(polish_char_words)):             
            if self.words[i] == polish_char_words[j]:   #if word in the full text matches a word in the list of only polish words w/ special characters  
                indexes.append(i)                       #save the index
                i = i + 1                               #go to the next word in the full text
                j = j + 1                               #go to the next word in the list of only polish words w/ special characters
            else:                                       #if current word in the full text does not match the polish word
                i = i + 1                               #go to the next word in the full text

        return indexes

    #main function that runs the program
    def convert(self):              
        txt.convert_words()
        txt.restore_case()
        txt.insert_polish_words()

txt = polish_txt("polish_letter.txt")   #creating the polish_txt object with the sample letter in the directory
txt.convert()                           #converting the text
