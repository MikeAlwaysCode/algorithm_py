from collections import Counter, defaultdict
from math import ceil
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    x, y = map(int, input().split())
    '''
    p = (x + y) // 2
    
    ans = max( abs(p - x), abs(p - y))
    '''
    ans = ceil((max(x, y) - min(x, y))/2)
    print(ans)

    return

t = int(input())
for _ in range(t):
    solve()