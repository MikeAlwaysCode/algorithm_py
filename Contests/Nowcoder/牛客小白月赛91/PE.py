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

t1 = "ACCEPT"
t2 = "WA"

def solve() -> None:
    n, k = mint()
    s = input()
    ans = 0
    last1 = [-1] * 6
    last2 = [-1] * 2
    for i, c in enumerate(s):
        for j in range(5, -1, -1):
            if c != t1[j]:
                continue
            if j == 0:
                last1[0] = i
            else:
                last1[j] = last1[j - 1]
        j = t2.find(c)
        if j != -1:
            if j == 0:
                last2[0] = i
            else:
                last2[j] = last2[j - 1]
        if last1[-1] != -1 and last1[-1] > last2[-1]:
            ans += max(0, min(last1[-1], i - k + 1) - last2[-1])
    print(ans)


solve()
