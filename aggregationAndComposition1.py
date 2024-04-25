class Character:
    def __init__(self, char):
        self.char = char
    def __str__(self):
        return self.char

class Word:
    def __init__(self):
        self.characters = []
    def add_char(self, char):
        self.characters.append(Character(char))#this is composition

    def __str__(self):
        return ''.join(str(char) for char in self.characters)

class Paragraph:
    def __init__(self):
        self.words = []
    def add_word(self, word):
        self.words.append(word)
    def __str__(self):
        return ' '.join(str(word) for word in self.words)

class File:
    def __init__(self):
        self.paragraphs = []
    def add_para(self, para):
        self.paragraphs.append(para)
    def __str__(self):
        return '\n'.join(str(para) for para in self.paragraphs)

class Folder:
    def __init__(self):
        self.files = []
    def add_file(self, file):
        self.files.append(file)
    def __str__(self):
        return '\n\n'.join(str(file) for file in self.files)


class User:
    def __init__(self):
        self.folders = [Folder(), Folder()] #composition
    def __str__(self):
        return '\n\n------\n\n'.join(str(folder) for folder in self.folders)

user.add_folders()
user.add_files()
user.add
