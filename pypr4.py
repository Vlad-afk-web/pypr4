class Eyes:
    def __init__(self, eclr):
        self.ecolor = eclr

    def sees(self):
        print('Очі закриті')

    def getcolor(self):
        print(self.ecolor)
    
    def addLens(self):
        print('Лінзи додано')

class Hair:
    def __init__(self, hclr):
        self.hcolor = hclr
    
    def gethcolor(self):
        print(self.hcolor)

class Beard:
    def getlength():
        return 'has a beard and its 13cm long'

    def getcolor():
        return 'grey'

class Ear:
    def hear(self):
        return 'nothing'
    
    def addEarring():
        print('Додано сережку')

class Mouth:
    def eat():
        return 'Hasnt eaten in a couple hours'
    
    def speak(self):
        return 'currently not speaking'
    
class Nose:
    def smell(self):
        return 'Smelling fresh air'
    
    def inhale():
        print('User inhailed')

    def exhale():
        print('User exhailed')

class Head(Nose, Eyes, Hair, Beard, Ear, Mouth):
    def getSize(self):
        print('Head is 60cm')

    def getEyes(self):
        print('The eyes are', self.ecolor)
    
    def getNose(self):
        print('The nose is ', self.smell())

    def getMouth(self):
        print('The mouth is', self.speak())

    def getEars(self):
        print('The ears are currently hearing', self.hear())

    def isBald():
        return False

e = Head('green')
e.getSize()

