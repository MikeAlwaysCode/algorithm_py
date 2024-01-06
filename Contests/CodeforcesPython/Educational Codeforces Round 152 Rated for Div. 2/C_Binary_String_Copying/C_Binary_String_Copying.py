import sys
from bisect import bisect

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
    s = input()
    ans = set()
    left, right = [-1] * n, [n] * n
    last = -1
    for i in range(n):
        if s[i] == "0":
            last = i
        left[i] = last
    last = n
    for i in range(n - 1, -1, -1):
        if s[i] == "1":
            last = i
        right[i] = last
    for _ in range(m):
        l, r = mint()
        l = right[l - 1]
        r = left[r - 1]
        if r < l: ans.add((n, n))
        else: ans.add((l, r))

    '''
    one = [n] * n
    zero = []
    last = n
    for i in range(n - 1, -1, -1):
        if s[i] == "1":
            last = i
        else:
            zero.append(i)
        one[i] = last
    zero.reverse()
    for _ in range(m):
        l, r = mint()
        l -= 1
        r -= 1
        if not zero or len(zero) == n:
            ans.add((n, n))
            continue
        l = one[l]
        if r <= l:
            ans.add((n, n))
            continue
        i = bisect(zero, l)
        j = bisect(zero, r)
        if i == j: ans.add((n, n))
        else: ans.add((l, j))
    '''
    print(len(ans))


for _ in range(int(input())):
    solve()
