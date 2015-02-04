__author__ = 'vnellore'

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''

    result = ()
    for i in range(0,len(aTup), 2):
        result += (aTup[i],)

    return result

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))