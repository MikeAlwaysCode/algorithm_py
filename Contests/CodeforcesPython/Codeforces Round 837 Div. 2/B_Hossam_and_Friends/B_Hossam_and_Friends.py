import sys

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
    n, m = mint()
    mn = [n] * (n + 1)
    for i in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        mn[u] = min(mn[u], v - 1)

    for i in range(n - 1, 0, -1):
        mn[i] = min(mn[i], mn[i + 1])
        
    ans = n
    # Let's process people from right to left and calculate the rightmost positions there subsegment can end. 
    # Initially, R=n−1. Then we go to ai just do R=min(R,ri) and add R−i+1 to answer.
    for i in range(1, n):
        ans += mn[i] - i

    print(ans)

for _ in range(int(input())):
    solve()
