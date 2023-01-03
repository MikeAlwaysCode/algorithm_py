from collections import Counter, defaultdict
from math import sqrt

def solve() -> None:
    n = int(input())

    if n < 5:
        print("No")
        return
    
    n += 4
    for i in range(3, int(sqrt(n))+1):
        if n % i == 0 and n // i >= 3:
            print("Yes")
            return
    print("No")


t = int(input())
for _ in range(t):
    solve()