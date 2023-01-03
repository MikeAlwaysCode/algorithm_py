# from functools import reduce
# from math import lcm, gcd
# from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    n = int(input())
    s = str(input())
    
    p = 0
    for i in range(2*n):
        if s[i] == ')':
            p += 1
        elif i > 0 and s[i-1] == ')':
            p -= 1

    print(p)

t = int(input())
for _ in range(t):
    solve()