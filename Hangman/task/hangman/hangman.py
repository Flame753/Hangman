import random


# Write your code here
def greeting():
    print('H A N G M A N')


def guess():
    world_lis = ['python', 'java', 'kotlin', 'javascript']
    word = input("Guess the word: ")
    if word == random.choice(world_lis):
        print("You survived!")
    else:
        print("You are hanged!")


greeting()
guess()
