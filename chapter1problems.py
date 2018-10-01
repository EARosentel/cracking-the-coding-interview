import BitVector
# Problem 1.1
# Is Unique: Implement and algorithm to determine if a string has all unique characters.
# What if you couldn't use additional data structures


def isunique(uniquestring):
    lettermap = {}

    for letter in uniquestring:
        if lettermap.__contains__(letter):
            return False
        else:
            lettermap[letter] = 1

    return True


def isuniqueinplace(uniquestring):
    uniquestringsorted = sorted(uniquestring)

    for index in range(len(uniquestringsorted)-1):
        if uniquestringsorted[index] == uniquestringsorted[index+1]:
            return False

    return True

# Problem 1.2
# Check Permutation: given two strings, write a method to decide if one is
# a permutation of the other


def ispermutation(string1, string2):
    if sorted(string1.lower()) == sorted(string2.lower()):
        return True
    else:
        return False

# Problem 1.3
# URLify: write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient
# space at the end to hold the additional characters, and that you are given the "true" length of the string.


def urlify(urlstring, strlen):
    finalstring = ""
    for index in range(strlen):
        if urlstring[index] == " ":
            finalstring += '%20'
        else:
            finalstring += urlstring[index]
        print(index)
    return finalstring


def urlifyinplace(urlstring, trulen):
    spacecount = 0

    for i in range(trulen):
        if urlstring[i] == ' ':
            spacecount += 1

    index = trulen + spacecount*2

    for letter in range(trulen-1, -1, -1):
        if urlstring[letter] == ' ':
            urlstring[index-1] = '0'
            urlstring[index-2] = '2'
            urlstring[index-3] = '%'
            index -= 3
        else:
            urlstring[index-1]=urlstring[letter]
            index -= 1

    return urlstring


# Problem 1.4
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.

def permpalindrome(inputstr):
    lettermap = {}

    for letter in inputstr:
        if letter == ' ':  #this one only takes into account space. it should account for any non letter character
            continue

        if letter in lettermap.keys():
            lettermap.pop(letter)
        else:
            lettermap[letter] = 0

    remainingletters = lettermap.keys()

    if len(remainingletters) > 1:
        return False

    return True


# Palindrome Permutation - with bit vectors


def lettertoint(letter):
    lettermap = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }

    if letter in lettermap.keys():
        return lettermap[letter]
    else:
        return 0


def toggle(bitvector, index):
    if index == 0:
        return bitvector
    mask = BitVector.BitVector(size=26, intVal=1)
    mask = mask << index
    if int(bitvector & mask) == 0:
        bitvector |= mask
    else:
        bitvector &= ~mask

    return bitvector


def createbitvector(phrase):
    bitvector = BitVector.BitVector(size=26)
    for letter in phrase:
        x = lettertoint(letter)
        bitvector = toggle(bitvector, x)
    return bitvector


def checkbitvector(bitvector):
    return int(bitvector & BitVector.BitVector(size=26, intVal=int(bitvector)-1)) == 0


def ispalindromepermutation(phrase):
    bitvector = createbitvector(phrase)
    return int(bitvector) == 0 or checkbitvector(bitvector)


# Problem 1.5
# One Away - There are three types of edits that can be performed on strings: insert a character, remove a character,
# or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def oneaway(string1, string2):
    if len(string1) == len(string2):
        flag = False
        for index in range(len(string1)):
            if string1[index: index+1] != string2[index: index+1]:
                if flag:
                    return False
                else:
                    flag = True
        return True

    else:
        if len(string1) > len(string2):
            return extracharoneaway(string1, string2)
        else:
            return extracharoneaway(string2, string1)


def extracharoneaway(lstring, sstring):
    specindex = 0
    for index in range(len(sstring)):
        if lstring[index+specindex: index+1+specindex] != sstring[index: index+1]:
            if specindex == 1:
                return False
            else:
                specindex = 1
                if lstring[index + specindex: index + 1 + specindex] != sstring[index: index + 1]:
                    return False
    return True


# Problem 1.6
# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# If the compressed string would not be smaller than the original string, return the original string.


def compresstring(inputstring):
    index = 0
    counter = 1
    resultstring = ""
    while index < len(inputstring):
        if inputstring[index:index+1] == inputstring[index+1: index+2]:
            counter += 1
        else:
            resultstring += inputstring[index:index+1] + str(counter)
            counter = 1
        index += 1

    if len(resultstring) > len(inputstring):
        return inputstring
    else:
        return resultstring

