import random
print('H A N G M A N')
word = random.choice(('python', 'java', 'kotlin', 'javascript'))
hidden = "-" * (len(word))  # The hidden word on screen
lives = 8

while lives > 0:
    if hidden != word:
        print()
        print(hidden)
        guess = str(input("Input a letter: "))
        if guess not in word:
            print("No such letter in the word")
            lives -= 1
        if guess in hidden:
            print("No improvements")
            lives -= 1
        for index in range(len(word)):
            if guess == word[index]:
                hidden = hidden[:index] + guess + hidden[index+1:]
    else:
        print("You guessed the word!")
        print("You survived!")
        break
if lives == 0 and hidden != word:
    print("You are hanged!")

