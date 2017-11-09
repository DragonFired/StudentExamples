#! /usr/bin/env python
__author__ = 'Arana Fireheart'

def sortByLen(inputList):
    outputList = inputList[0:1]
    outputList.append('')           # Add a 'null' element to the end, so that
                                    # there is always somthing shorter than any
                                    # input.
    for inputString in inputList[1:]:
        for outputString in outputList:
            if len(outputString) < len(inputString):
                insertPosition = outputList.index(outputString)
                outputList.insert(insertPosition, inputString)
                break
    return outputList[:-1]

def sortByLen2(inputList):
    outputList = inputList[0:1]
    for inputString in inputList[1:]:
        outputListPosition = 0
        while outputListPosition < len(outputList):
            if len(outputList[outputListPosition]) < len(inputString):
                insertPosition = outputList.index(outputList[outputListPosition])
                outputList.insert(insertPosition, inputString)
                break
            if outputListPosition == len(outputList) - 1:
                outputList.append(inputString)
                break
            outputListPosition += 1
    return outputList

def sortByLen3(inputList):
    outputList = inputList[0:1]
    for inputString in inputList[1:]:
        for outputListPosition, outputString in enumerate(outputList):
            if len(outputString) < len(inputString):
                insertPosition = outputList.index(outputString)
                outputList.insert(insertPosition, inputString)
                break
            if outputListPosition == len(outputList) - 1:
                outputList.append(inputString)
                break
    return outputList

print(sortByLen("How does all this wonderful stuff do something".split()))
print(sortByLen2("How does all this wonderful stuff do something".split()))
print(sortByLen3("How does all this wonderful stuff do something".split()))
print(sortByLen(['python', 'java', 'c', 'swift', 'ruby', 'php']))
print(sortByLen2(['python', 'java', 'c', 'swift', 'ruby', 'php']))
print(sortByLen3(['python', 'java', 'c', 'swift', 'ruby', 'php']))
