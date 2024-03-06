import sys
from collections import deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    s = input()
    L, R = [0] * n, [0] * n
    for i in range(n):
        L[i], R[i] = mint()
    
    ans = n
    q = deque([(0, 0)])
    while q:
        u, t = q.popleft()
        if L[u] == R[u] == 0:
            ans = min(ans, t)
            continue
        if L[u]:
            q.append((L[u] - 1, t + (s[u] != 'L')))
        if R[u]:
            q.append((R[u] - 1, t + (s[u] != 'R')))
    print(ans)


for _ in range(int(input())):
    solve()
