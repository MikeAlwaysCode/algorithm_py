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
    nums = ints()
    ans = []
    s = set()
    l = 0
    for r, x in enumerate(nums):
        if x in s:
            ans.append([l + 1, r + 1])
            l = r + 1
            s.clear()
        else:
            s.add(x)
    if s and not ans:
        print(-1)
        return
    if s:
        ans[-1][1] = n
    print(len(ans))
    for l, r in ans:
        print(l, r)


solve()
