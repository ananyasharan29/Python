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

w1 = Word()

w1.add_char('A')
w1.add_char('N')
w1.add_char('A')
w1.add_char('N')
w1.add_char('Y')
w1.add_char('A')

w2 = Word()

w2.add_char('S')
w2.add_char('H')
w2.add_char('A')
w2.add_char('R')
w2.add_char('A')
w2.add_char('N')


w3 = Word()

w3.add_char('P')
w3.add_char('Y')
w3.add_char('T')
w3.add_char('H')
w3.add_char('O')
w3.add_char('N')

w4 = Word()

w4.add_char('I')
w4.add_char('S')


w5 = Word()

w5.add_char('G')
w5.add_char('R')
w5.add_char('E')
w5.add_char('A')
w5.add_char('T')


w6 = Word()

w6.add_char('P')
w6.add_char('A')
w6.add_char('R')
w6.add_char('U')
w6.add_char('L')

p1 = Paragraph()
p2 = Paragraph()
p3 = Paragraph()
p4 = Paragraph()
p5 = Paragraph()

p1.add_word(w1)
p1.add_word(w2)

p2.add_word(w1)
p3.add_word(w3)

p3.add_word(w2)
p3.add_word(w4)
p3.add_word(w6)

p4.add_word(w2)
p4.add_word(w3)
p4.add_word(w4)

p5.add_word(w6)
p5.add_word(w2)

print(w1)
print(p1)

f1= File()
f2= File()
f3= File()
f4= File()

f1.add_para(p1)
f1.add_para(p2)

f2.add_para(p2)
f2.add_para(p5)

f3.add_para(p1)
f3.add_para(p3)
f3.add_para(p4)

f4.add_para(p1)
f4.add_para(p4)
f4.add_para(p5)

print(f1)

u = User()
u.folders[0].add_file(f1)
u.folders[0].add_file(f2)

u.folders[1].add_file(f1)
u.folders[1].add_file(f3)
u.folders[1].add_file(f4)

print(u)






















