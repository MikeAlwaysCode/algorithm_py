import sys
#sys.setrecursionlimit(20000)
#from collections import deque #Counter
#from itertools import accumulate, product
#from functools import reduce
#import math


def rall():
    return [x.strip() for x in sys.stdin.readlines()]
def rl():
    return sys.stdin.readline().strip()
def rl_types(types):
    str_list = [x for x in sys.stdin.readline().strip().split(' ')]
    return [types[i](str_list[i]) for i in range(len(str_list))]

def pr( something='' ):
    sys.stdout.write( str(something) + '\n')
def pra( array ):
    sys.stdout.write( ' '.join([str(x) for x in array]) + '\n')



if __name__ == '__main__':

    NT = int( rl() )
    #a,b = map(int,rl().split(' '))

    for ti in range(NT):
        n,m = map(int, rl().split(' '))
        #array = [0]*m

        if m < n:
            pr('No') # no sequence of positive integers!
        #elif m%2==1:
            #pr('No') # there's going to be an element all by itself of neccesity, thus no
        else:
            # see if we can do this
            if n%2==0 and m%2==0:
                avg = m//n
                array=[avg]*n
                m -= avg*n
                array[0] += m//2
                array[1] += m//2
            elif n%2==1 and m%2==1:
                avg = m//n
                array=[avg]*n
                m -= avg*n
                array[0] += m
            elif n%2==1 and m%2==0:
                array=[m//n]*n
                array[0] = m-array[0]*(n-1)
            #elif m%n == 0:
                #array=[m//n]*n
            else:
                pr('No')
                continue
            pr('Yes')
            pra(array)

