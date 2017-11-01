__author__ = 'arana'
from datetime import datetime

class Person(object):

    def __init__(self, startingName):
        self.name = startingName
        self.dateOfBirth = datetime.date(datetime.now())
        self.age = datetime.date(datetime.now()) - self.dateOfBirth
        self.height = 0
        self.weight = 0
        self.eyeColor = None
        self.phrases = []
        self.gender = None

    def __str__(self):
        return "Name: {0} Height:  {1} Weight: {2} Age: {3} Number of past phrases: {4}".format(self.name, self.height, self.weight, self.age, len(self.phrases))

    def speak(self, phraseToSpeak):
        self.phrases.append(phraseToSpeak)
        print(phraseToSpeak)

    def pastPhrases(self, numberOfSteps = 1):
        if numberOfSteps > 0:
            return self.phrases[-numberOfSteps:]
        else:
            raise ValueError

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setDateOfBirth(self, newDate):
        self.dateOfBirth = newDate

    def getDateOfBirth(self):
        return self.dateOfBirth

    def getAge(self):
        return self.age

    def setHeight(self, newHeight):
        self.height = newHeight

    def getHeight(self):
        return self.height

    def setWeight(self, newWeight):
        self.weight = newWeight

    def getWeight(self):
        return self.weight

    def setEyeColor(self, newEyeColor):
        self.eyeColor = newEyeColor

    def getEyeColor(self):
        return self.eyeColor

    def getGender(self):
        return self.gender


class Man(Person):

    def __init__(self, startingName):
        super().__init__(startingName)
        self.gender = "Male"

class Woman(Person):

    def __init__(self, startingName):
        super().__init__(startingName)
        self.gender = "Female"


person1 = Person("Mindy")
person1.setHeight(123)
person1.setWeight(133)
person1.speak("Hello")
person1.speak("Good Bye")
person1.speak("What?")
person1.speak("Nothing!")
person1.speak("Why?")
print(person1)
print("---------")
print(person1.pastPhrases())
print("---------")
print(person1.pastPhrases(4))
print("---------")
try:
    print(person1.pastPhrases(-10))
except ValueError:
    print("Usage error: numberOfSteps must be positive.")
print(person1.getGender())
man1 = Man("George")
man1.setHeight(345)
man1.setWeight(220)
print(man1.getGender())
woman1 = Woman("Martha")
woman1.setHeight(345)
woman1.setWeight(220)
print(woman1.getGender())
