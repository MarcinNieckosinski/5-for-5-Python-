from time import sleep
from word_generator import WordGenerator


def draw_word(used_words):
    """
    This function draws a word for the game. It also checks if the word was not used before.
    :param used_words:
    A list with words already used in a single game.
    :return:
    Returns a word for the game and changed list with already used words.
    """
    word_generator = WordGenerator()

    word_generator.read_words()
    word_generator.select_random_word()
    while word_generator.word in used_words:
        word_generator.select_random_word()
    used_words.append(word_generator.word)

    return word_generator.word, used_words


def game():
    """
    Main game function that gets user input and verifies it against drawn word.
    """
    game_used_words = []
    try_number = 0
    score = 0

    drawn_word, game_used_words = draw_word(game_used_words)

    print("Send \"menu\" to get back to main menu!")
    print("Game has begun! GL && HF!")

    while try_number < 5:
        help_string = "#####"
        not_guessed_letters = []

        try_number += 1

        print("Try number: " + str(try_number))
        user_input = input("Your guess: ")

        if user_input == "menu":
            break

        if len(user_input) != 5 or any(character.isdigit() for character in user_input):
            print("ERROR! Only 5 letter words allowed. Also do not use numbers!")
            continue

        if user_input == drawn_word:
            score += 1
            drawn_word, game_used_words = draw_word(game_used_words)
            try_number = 0
            continue

        for i in range(len(drawn_word)):
            if user_input[i] == drawn_word[i]:
                help_string = help_string[:i] + "@" + help_string[i + 1:]

        for i in range(len(drawn_word)):
            if help_string[i] == "#":
                not_guessed_letters.append(drawn_word[i])

        for i in range(len(user_input)):
            if help_string[i] == "#":
                if user_input[i] in not_guessed_letters:
                    help_string = help_string[:i] + "*" + help_string[i + 1:]

        print(help_string)

    if try_number >= 5:
        print("You've lost the game. Your score: " + str(score))
        print("The game will get back to menu soon.")
        sleep(5)
