print 'hello, world!'


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''

    if exp == 0:
        return 1
    elif exp == 1:
        return base
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp/2)
    elif exp % 2 == 1:
        return base * recurPowerNew(base, exp - 1)

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if a > b:
        gcd = b
    else:
        gcd = a

    while True:
        if (a % gcd == 0 and b % gcd == 0) or (gcd == 1):
            return gcd
        else:
            gcd -= 1

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)


print gcdRecur(15,9)