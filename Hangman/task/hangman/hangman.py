import random


def greeting():
    print('H A N G M A N')


# Outputs random word out of a define list
def random_word():
    word_lis = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(word_lis)


def letter_in_word(word, guess_letters):
    if guess_letters in word:
        return True
    else:
        return False


def main():
    chosen_word = random_word()  # The word your guessing
    life = 8
    show_word = "-" * (len(chosen_word))  # The hidden word on screen
    guessed_letters = set()
    guess = ""  # user guess

    while life > 0:  # if life runs out then death
        print()
        print(show_word)
        if guess == chosen_word or show_word == chosen_word:  # if guessed word or all letter (win)
            print("you guessed the word!")
            print("You survived!")
            break

        guess = (input("Input a letter: "))
        if guess in guessed_letters:  # if letter was repeated
            print("No improvements")

        elif letter_in_word(chosen_word, guess):  # if letter in word
            for index, value in enumerate(chosen_word):
                if value == guess:
                    show_word = list(show_word)
                    show_word[index] = guess
                    show_word = "".join(show_word)
            life -= 1

        else:  # if letter not in word
            print("No such letter in the word")
            life -= 1

        guessed_letters.add(guess)
    else:  # death
        print("You are hanged!")


greeting()
main()
