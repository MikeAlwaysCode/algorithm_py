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
    n, l, k = mint()
    s = sorted(input())
    if k == 1:
        for i in range(n):
            print("".join(s[i * l:(i + 1) * l]))
        return
    i, j = 0, n * l - 1
    ans = [[] for _ in range(k)]
    b = 0
    for m in range(l):
        for p in range(b, k):
            ans[p].append(s[i])
            i += 1
        p = k - 2
        while p >= b and ans[p][-1] == ans[-1][-1]:
            p -= 1
        nb = p + 1
        for p in range(nb - 1, b - 1, -1):
            ans[p].extend(s[j - l + m + 2:j + 1])
            j -= l - m - 1
        if nb == k - 1:
            ans[-1].extend(s[i:i + l - m - 1])
            i += l - m - 1
            break
        b = nb
    for p in range(k):
        print("".join(ans[p]))
    for _ in range(n - k):
        print("".join(s[i:i + l]))
        i += l

solve()
