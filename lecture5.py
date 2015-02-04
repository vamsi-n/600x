__author__ = 'vnellore'

def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''

    if aStr == '':
        return 0

    if aStr[:-1] == '':
        return 1
    else:
        return 1 + lenRecur(aStr[1:])




def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    if aStr == '':
        return False

    middle_char_idx = len(aStr) / 2
    middle_char = aStr[middle_char_idx]



    if middle_char == char:
        return True
    elif middle_char > char:
        return isIn(char, aStr[0:middle_char_idx])
    elif middle_char < char:
        return isIn(char, aStr[middle_char_idx + 1:])

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''

    if len(str1) != len(str2):
        return False

    if str1 == '' and str2 == '':
        return True

    return str1[0] == str2[-1] and semordnilap(str1[1:], str2[0:-1])

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)


print str(semordnilapWrapper('desserts','stresseds'))