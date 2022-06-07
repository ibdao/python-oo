from random import choice
FILE_PATH = '/home/kestrel/Documents/Rithm/r-26/Class notes/week3/June7/python-oo-practice-lab/python-oo/words.txt'

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        """opens word file and sets word list"""
        self.file = open(file_path)
        self.list = self.get_list_of_words()
    
    def random(self):
        """returns a random word from list of words"""
        return choice(self.list)
        
    def get_list_of_words(self):
        """Returns a list of words from word file"""
        """check .strip method for newlines"""
        lst = []
        for line in self.file:
            lst.append(line.strip())
        self.file.close()
        return lst


class SpecialWordFinder(WordFinder):
    """Special Word Finder: removes comment strings from word file and blank lines"""
    
    def get_list_of_words(self):
        """Returns a list of words from word file omitting #comments and blank lines"""
        lst = []
        for line in self.file:
            if not line.startswith('#') and not line.isspace():
                lst.append(line.strip())
        self.file.close()
        return lst