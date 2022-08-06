def boomingEcho(inWord,sizeofEcho):

    for aLetter in inWord:

        print(aLetter*sizeofEcho)



myString = input('Please enter a message >> ')

noofTimes = int(input('Please enter number of times'))

boomingEcho(myString,noofTimes)


def boomingEcho1(inWord):

    for aLetter in inWord:

        print(aLetter * len(inWord))



myString = input('Please enter a message >> ')

# noofTimes = int(input('Please enter number of times: '))

boomingEcho1(myString)