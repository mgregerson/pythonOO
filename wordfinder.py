import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file):
        """Defines file and word_list arguments in our Class"""
        self.file = file
        self.word_list = self.get_word_list()
        print(f"{len(self.word_list)} words read")

    def __repr__(self):
        return f"{len(self.word_list)} words read"

    # Add comprehension to line 21
    def get_word_list(self):
        """Generates a list of words in the file"""
        word_file = open(self.file)
        word_list = [line.replace("\n", "") for line in word_file]
        # for line in word_file:
        #     curr_word = line.replace("\n", "")
        #     word_list.append(curr_word)
        return word_list

    def len_word_list(self):
        """Returns length of word list in file"""
        return len(self.word_list)

    def get_random_word(self):
        """Returns random word from file"""
        return random.choice(self.word_list)

class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: Finds words without comments or blank space"""

    def get_word_list(self):
        """Returns a word list without blank lines or comment lines"""
        word_list = super().get_word_list()
        new_word_list = []
        for line in word_list:
            if line.strip() == '':
                pass
            elif line[0] != '#':
                curr_word = line.replace("\n", "")
                new_word_list.append(curr_word)

        self.word_list = new_word_list
        return self.word_list










