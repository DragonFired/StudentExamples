#! /usr/bin/env python
__author__ = 'Arana Fireheart'

def sortByLen(inputList):
    outputList = inputList[0:1]
    for inputString in inputList[1:]:
        for outputString in outputList:
            if len(outputString) < len(inputString):
                insertPosition = outputList.index(outputString)
                outputList.insert(insertPosition, inputString)
                break
    return outputList

print(sortByLen("How does all this wonderful stuff do something".split()))
print(sortByLen(['python', 'java', 'c', 'swift', 'ruby', 'php']))