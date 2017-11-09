#!/usr/bin/env python
__author__ = "Arana Fireheart"

class Person(object):
    def __init__(self, birthDateTime):
        self.birthday = birthDateTime
        self.name = None
        self.height = None
        self.weight = None      # Float for weight in pounds
        self.gender = None
        self.location = None
        self.parents = []
        self.siblings = []

    def __str__(self):
        return "{0} is {1} years old, {2}\" tall and weighs {3} pounds".format(self.getName(), self.getAge(), self.getHeight(), self.getWeight())

    def setBirthday(self, newDateTime):
        self.birthday = newDateTime

    def getBirthday(self):
        return self.birthday

    def getAge(self):
        pass
        # return self.now() - self.birthday

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setHeight(self, newHeight):
        self.height = newHeight

    def getHeight(self):
        return self.height

    def setWeight(self, newWeight):
        self.weight = newWeight

    def getWeight(self):
        return self.weight

    def setGender(self, newGender):
        self.gender = newGender

    def getGender(self):
        return self.gender

    def setLocation(self, newLocation):
        self.location = newLocation

    def getLocation(self):
        return self.location

    def addParent(self, newParent):
        self.parents.append(newParent)

    def getParents(self):
        return self.parents

    def addSibling(self, newSibling):
        self.siblings.append(newSibling)

    def getSiblings(self):
        return self.siblings