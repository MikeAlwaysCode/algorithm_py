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
    A = ints()
    B = ints()
    
    A.sort()
    B.sort()
    idx = [-1] * n
    cnt = j = 0
    for i, a in enumerate(A):
        while j < n and a >= B[j]:
            j += 1
        if j == n and cnt == 0:
            cnt = n - i - 1
        if j < n:
            idx[j] = i
            j += 1
    ans = m * (cnt + 1)
    for i in range(n - 1, -1, -1):
        if idx[i] == -1:
            ans = min((B[i] - 1), m) * cnt + max(0, m - B[i] + 1) * (cnt + 1)
            break
    
    print(ans)

for _ in range(int(input())):
    solve()