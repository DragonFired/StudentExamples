#! /usr/bin/env python
from math import pi

# This is an example of a function with an optional parameter
# The optional parameter was added as an upgrade to handle
# griviances about the lack of a "report and crash" mode
# of operation.

__author__ = 'Arana Fireheart'

def avSphere(radius, raiseError = True, errorMessage = ""):
    surfaceArea = 4 * pi * radius ** 2
    volume = 4 / 3 * pi * radius ** 3
    if radius >= 0:
        return (surfaceArea, volume)
    else:
        if raiseError == True:
            raise ValueError
        else:
            print(errorMessage)
            return (abs(surfaceArea), abs(volume))


print(avSphere(3))
print(avSphere(43.5))
print(avSphere(0))
try:
    print(avSphere(-323))
except ValueError:
    print("Oops!")
print(20 * '-')

try:
    print(avSphere(-323, False))
except ValueError:
    print("Oops!")
print(20 * '-')

try:
    print(avSphere(-323, False, "Died due to negative radius, RIP"))
except ValueError:
    print("Oops!")
print(20 * '-')

mySurfaceArea, myVolume = avSphere(43.5)
print("Surface Area: {0} Volume: {1}".format(mySurfaceArea, myVolume))