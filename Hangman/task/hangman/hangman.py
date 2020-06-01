import random


def greeting():
    print('H A N G M A N')


# Outputs random word out of a def list
def random_word():
    word_lis = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(word_lis)


def letter_in_word(word, guess_letters):
    if guess_letters in word:
        return True
    else:
        return False


def main():
    chosen_word = random_word()
    life = 8
    show_word = "-" * (len(chosen_word))

    for rounds in range(life):
        print(show_word)
        letter = (input("Guess the word : "))
        if letter_in_word(chosen_word, letter):
            for index, value in enumerate(chosen_word):
                if value == letter:
                    show_word = list(show_word)
                    show_word[index] = letter
                    show_word = "".join(show_word)
        else:
            print("No such letter in the word")


greeting()
main()

