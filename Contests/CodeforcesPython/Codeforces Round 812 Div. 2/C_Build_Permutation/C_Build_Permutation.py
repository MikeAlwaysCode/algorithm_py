from math import sqrt

N = int(1e5 + 5)
ans = [0] * N

def solve(r: int) -> None:
    if r < 0:
        return
    s = int(sqrt(2*r))
    s *= s
    l = s - r
    solve(l - 1)
    while l <= r:
        ans[l] = r
        ans[r] = l
        l += 1
        r -= 1

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n - 1)
    print(*ans[:n])
    
'''
from math import sqrt

def solve() -> None:
    n = int(input())

    res = [-1] * n
    def go(i):
        a = int(sqrt((i-1)*2))
        m = a * a
        # print(i, a)
        idx = i - 1
        while m - idx < i:
            res[idx] = m - idx
            idx -= 1
        if idx >= 0:
            go(idx+1)

    go(n)
    print(*res)

t = int(input())
for _ in range(t):
    solve()
'''