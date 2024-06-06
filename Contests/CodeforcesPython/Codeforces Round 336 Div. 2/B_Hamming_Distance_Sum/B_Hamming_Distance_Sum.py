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
    s = input()
    t = input()
    n, m = len(s), len(t)
    cnt = [0] * 2
    ans = 0
    i = j = 0
    for k, c in enumerate(t):
        if j < n and j <= k:
            cnt[int(s[j])] += 1
            j += 1
        if i < n - m + k:
            cnt[int(s[i])] -= 1
            i += 1
        ans += cnt[int(t[k]) ^ 1]
    print(ans)


solve()
