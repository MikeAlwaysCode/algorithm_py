from collections import Counter, defaultdict
from math import sqrt

def solve() -> None:
    x, y = map(int, input().split())

    a = x // 2
    b = x - a
    '''
    t = int(sqrt(y))

    c, d = 1, y
    for i in range(t+1, 1, -1):
        if y % i == 0:
            c = min(i, y // i)
            d = max(i, y // i)
            break
    
    if c > b or a > d:
        print(a, b)
        print(c, d)
    else:
        print(-1)
    '''
    i = 1
    while i * i <= y:
        if y % i == 0:
            j = y // i
            
            if min(i, j) > b or max(i, j) < a:
                print(a, b)
                print(min(i, j), max(i, j))
                return
        i += 1

    print(-1)

t = int(input())
for _ in range(t):
    solve()