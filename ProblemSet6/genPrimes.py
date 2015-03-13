__author__ = 'Vamsi'

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last


def genOddNumbers():

    i = 0
    while True:
        i += 1
        if i % 2 != 0:
            yield i


a = genOddNumbers()
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
