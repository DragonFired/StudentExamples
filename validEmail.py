#! /usr/bin/env python
__author__ = 'Arana Fireheart'

def validEmail(address, domains=(".com", ".net", "org", ".uk" ".biz", ".gov", ".edu", ".mil")):

    if address.find(' ') >= 0:
        return False
    elif address.find('@') < 1:
        return False
    elif address.count('.') < 1:
        return False
    else:
        atPosition = address.index('@')
        periodPosition = address.index('.')
        if periodPosition - atPosition <= 1:
            return False
        else:
            lastPeriodPosition = address.rfind('.')
            if lastPeriodPosition == len(address):
                return False
            elif address[lastPeriodPosition:] not in domains:
                return False
    return True


print(validEmail("me@hotmail.com"))    # Returns True
print(validEmail("@abc.com"))          # Returns False
print(validEmail("me@abc.fat"))        # Returns False
print(validEmail("me@abc."))           # Returns False
print(validEmail("me@abc.def.com"))    # Returns True