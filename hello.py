print 'hello, world!'


def vowel_count(x):

    x = x.lower()
    totalCount = x.count('a') + x.count('e') + x.count('i') + x.count('o') + x.count('u')

    return totalCount

def string_count(x):

    total = 0
    total += x.count('bob')
    return total

x = 'azcbobobobobgghakl'
print 'Number of times bob occurs is ' +  str(string_count(x))


vowel_count('elephant')