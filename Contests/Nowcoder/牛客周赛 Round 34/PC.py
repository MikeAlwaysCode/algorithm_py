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
    ans = []
    n = len(s)
    i = 0
    while i < n:
        if int(s[i]) & 1:
            j = i + 1
            while j < n and int(s[j]) & 1:
                j += 1
            ans.append(s[i:j + 1])
            i = j + 1
        else:
            ans.append(s[i])
            i += 1
    ans.sort(key = lambda x: (len(x), x))
    for x in ans:
        print(x)


solve()
