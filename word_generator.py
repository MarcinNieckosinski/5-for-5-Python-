import random


class WordGenerator:
    """
    This class generates random 5-letter word.
    """
    def __init__(self):
        self.words = []
        self.word = ""

    def read_words(self):
        """
        This function reads 5-letter words from "words" file.
        """
        words = []
        with open('words') as f:
            word_lines = f.readlines()
            for word_line in word_lines:
                words.append(word_line.replace("\n", ""))
        self.words = words

    def select_random_word(self):
        """
        This function returns random element from a list of 5-letter words.
        """
        self.word = random.choice(self.words)
