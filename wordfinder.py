class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("/Users/student/words.txt") 3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, file):
        self.file = file
        self.word_list = []

    # Method to generate word list
    def get_word_list(self):
        word_file = open(self.file)
        for line in word_file:
            curr_word = line.replace("\n", "")
            self.word_list.append(curr_word)
        print(self.word_list)

    # Method to get length of word list

    # Method to get random word
