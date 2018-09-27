
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

#
# stopping here for today
#


def urlifyinplace(urlstring, strlen):
    index = 0
    while index < len(urlstring):
        if urlstring[index] == " ":
            urlstring[index] = '%'
            for letter in range(index, len(urlstring)):
                urlstring[letter+2] = urlstring[letter]
            index += 1
            urlstring[index] = '2'
            index += 1
            urlstring[index] = '0'

        index += 1

    return urlstring




