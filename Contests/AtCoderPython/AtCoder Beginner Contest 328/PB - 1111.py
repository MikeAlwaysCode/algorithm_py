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
    n = sint()
    nums = ints()
    ans = 0
    for i, x in enumerate(nums):
        m = i + 1
        s = set(list(str(m)))
        if len(s) > 1: continue
        d = int(s.pop())
        cur = d
        while cur <= x:
            ans += 1
            cur = cur * 10 + d
    print(ans)

solve()