import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    s = input()
    cnt = [0] * 26
    mx = 0
    ans = ""
    for i, c in enumerate(s):
        d = ord(c) - 97
        cnt[d] += 1
        if cnt[d] > mx:
            mx, ans = cnt[d], c
        elif cnt[d] == mx and c < ans:
            ans = c
    print(ans)


solve()
