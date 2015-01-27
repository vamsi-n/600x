__author__ = 'vnellore'


def printMove(fr, to):

    print fr + ' to ' + to

def Towers(n, fr, to, sp):

    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, sp, to)
        Towers(1, fr,to, sp)
        Towers(n-1, sp,to,fr)

Towers(5,'f','t','s')
