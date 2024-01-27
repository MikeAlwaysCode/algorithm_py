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
    n = sint()
    s = list(map(int, list(input())))
    ans = 0
    for i in range(n):
        cnt = [0] * 10
        mx = k = 0
        for j in range(i, n):
            cnt[s[j]] += 1
            if cnt[s[j]] > 10:
                break
            if cnt[s[j]] == 1:
                k += 1
            if cnt[s[j]] > mx:
                mx = cnt[s[j]]
            if mx <= k:
                ans += 1

    print(ans)


for _ in range(int(input())):
    solve()
