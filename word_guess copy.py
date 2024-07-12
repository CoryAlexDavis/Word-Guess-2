"""
file: word_guess.py
"""
import random
import sys

def main():

    #select a random word from a file that contains a list of words
    word_list = read_in()
    #select random word
    word = select_word(word_list)
    #print a row of dashes for each letter in mystery word
    word_dict = turn_word_to_dict(word)
    # make a function that fills in letters that are guessed in the word using a conditional statment
    print_function(word_dict)

    #make a way to keep track of correctly guessed letters
    correct = 0
    number_of_turns = 8
    #create a break from the function if user has guessed the word or made 8 incorrect guesses
    while number_of_turns > 0:
        if word == ''.join(word_dict):
            print('congratulations the word is ' + str(word))
            break
        user_guess = input('Type a single letter here, then press enter: ').upper()
        if number_of_turns <= 0:
            break
        # if number of guesses is equal to the length of the word then break
        if word == ''.join(word_dict):
        #if correct == len(word) - 1:
            print('congratulations the word is ' + str(word))
            break
        elif user_guess in word:
            for i in range(len(word_dict)):
                if word[i] == user_guess:
                    word_dict[i] = user_guess
            correct += 1
            number_of_turns -= 1
            print('That guess is correct')
            print('You have ' + str(number_of_turns) + ' turns left')
            print_function(word_dict)
        elif user_guess not in word:
            number_of_turns -= 1
            print('There are no ' + user_guess + "'s in the word")
            print('You have ' + str(number_of_turns ) + ' turns left')
    

def read_in():
    cohesion = []
    with open('TestLexicon.txt') as file:
        for line in file:
            line = line.split()
            cohesion += line
    return cohesion

def select_word(word_list):
    return random.choice(word_list)

def turn_word_to_dict(word):
    word_dict = []
    print(word)
    for letter in range(len(word)):
        word_dict += '-'
    return word_dict

def print_function(word_dict):
    connector = ''
    for i in range(len(word_dict)):
        connector += word_dict[i]
    print('The word now looks like this: ' + str(connector))


if __name__=='__main__':
    main()
