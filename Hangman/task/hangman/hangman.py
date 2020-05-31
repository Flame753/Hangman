import random


def greeting():
    print('H A N G M A N')


# Outputs random word out of a def list
def random_word():
    word_lis = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(word_lis)


# Takes the first 3 char form the given string and outputs a
# string with the first 3 char with the rest char as "-".
def hint(word):
    return word[:3] + "-"*(len(word)-3)


def guess():
    chosen_word = random_word()
    word = input(f"Guess the word {hint(chosen_word)}: ")
    if word == chosen_word:
        print("You survived!")
    else:
        print("You are hanged!")


greeting()
guess()

