from images import IMAGES
def hangman(secret_word):
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""

    total_lives = remaining_lives = 8
    user_difficulty_choice = raw_input("Choose your difficulty level!\na)\tEasy\nb)\tMedium\nc)\tHard\n")
    images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]

    if user_difficulty_choice not in ["a", "b", "c", "easy", "Easy", "Medium", "medium", "Hard", "hard"]:
        print "Your choice is invalid.\nThe Game is starting in Easy mode"

    else:
        if user_difficulty_choice == "b" or user_difficulty_choice == "medium" or user_difficulty_choice == "Medium":
            total_lives = remaining_lives = 6
            images_selection_list_indices = [0, 2, 3, 5, 6, 7]

        elif user_difficulty_choice == "c" or user_difficulty_choice == "hard" or user_difficulty_choice == "Hard":
            total_lives = remaining_lives = 4
            images_selection_list_indices = [1, 3, 5, 7]

    letters_guessed = []
    print "You have only " + str(remaining_lives) + " chances."

    while (remaining_lives > 0):
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + available_letters

        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()

        if guess == "hint":
            letter = get_hint(secret_word, letters_guessed)

        if len(letter) != 1:
            print "Oops! Please enter a single letter alphabet."
            return False

        if not letter.isalpha():
            print "Oops! Please enter only alphabet letter"
            return False

        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break

        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            print ""
            print IMAGES[images_selection_list_indices[total_lives-remaining_lives]]
            remaining_lives -= 1
            print "Remaining Lives: " + str(remaining_lives)

    else:
        print "Sorry, you ran out of guesses.\nThe word was " + str(secret_word) + "."

def get_available_letters(letters_guessed):
    import string
    all_letters = string.ascii_lowercase
    letters_left = ""

    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter

    return letters_left

def is_word_guessed(secret_word, letters_guessed):
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True
    return False

def get_hint(secret_word, letters_guessed):

    import random
    letters_not_guessed = []

    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index += 1
    return random.choice(letters_not_guessed)

def get_guessed_word(secret_word, letters_guessed):

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1

    return guessed_word

def load_words():
    import random
    import string
    WORDLIST_FILENAME = "words.txt"
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME)
    line = inFile.readline()
    word_list = string.split(line)
    print "  ", len(word_list), "words loaded.\n"

    return word_list

def choose_word():
    import random
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word



hangman(choose_word())
