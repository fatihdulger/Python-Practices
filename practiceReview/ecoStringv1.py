def boomingEcho(inWord):
    for aLetter in inWord:
        print(aLetter * 8)

myString = input('Please enter a message >> ')

boomingEcho(myString)

def boomingEcho1(xWord):
    for a in xWord:
        print(a * 4)

myString = input('Please enter a message >> ')

boomingEcho1(myString)


def acrostic(xWord):
    for a in xWord:
        print(a * 1)

myString = input('Please enter a message >> ')

acrostic(myString)