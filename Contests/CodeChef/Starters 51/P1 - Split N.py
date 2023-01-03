from collections import Counter, defaultdict
from math import log2

def solve() -> None:
    n = int(input())
    
    ans = 0
    while n:
        ans += 1
        k = int(log2(n))
        n -= 2 ** k

    print(ans - 1)
        

t = int(input())
for _ in range(t):
    solve()