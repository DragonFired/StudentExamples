#!/usr/bin/env python
__author__ = "Arana Fireheart"

from os import path

outputFilename = "outputFile.txt"   # set a default output filename.
defaultInputFilename = "testfile2.txt"

inputData = []

def getFilename(defaultFileName):
    newFilename = input("Enter input filename ({0}): ".format(defaultFileName))
    if newFilename != '':
        return newFilename
    else:
        return defaultFileName

inputFilename = getFilename(defaultInputFilename)

while not path.exists(inputFilename):
    inputFilename = getFilename(defaultInputFilename)

with open(inputFilename, 'r') as inputFile:
    headerLine = inputFile.readline().strip().split(',')
    for line in inputFile.readlines():
        if line.strip() != '':
            inputData.append(line.strip().split(','))

outputList = []
outputDict = {}
lastNameList = []
for recordNumber, line in enumerate(inputData):
    idField = line[0]
    lastName = line[1]
    userID = line[2]
    country = line[3]
    keywordList = line[4:-2]
    fullName = line[-2]
    firstName = fullName.split()[0]
    email = line[-1]
    outputList.append([firstName, lastName, email, country, keywordList])
    outputDict[lastName + str(recordNumber)] = [firstName, lastName, email, country, keywordList]
    lastNameList.append(lastName + str(recordNumber))

lastNameList.sort()

while path.exists(outputFilename):
    print("ERROR: file named {0} exists.".format(outputFilename))
    outputFilename = input("Please enter a new filename (enter q to stop). ")
    if outputFilename.lower() == 'q':
        break

if outputFilename.lower() != 'q':
    with open(outputFilename, 'w') as outputFile:
        for sortedLastName in lastNameList:
            firstName, lastName, email, country, keywordList = outputDict[sortedLastName]
            outputFile.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(firstName, lastName, email, country, keywordList))

pass