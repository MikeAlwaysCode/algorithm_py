from collections import Counter, defaultdict
from math import gcd

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    # ans = 10 ** 9
    # for i in range(n-1):
    #     ans = min(ans, gcd(arr[i+1], arr[i]))
    #     if ans == 1:
    #         break
    # print(ans*n)
    print(n * gcd(*arr))

t = int(input())
for _ in range(t):
    solve()