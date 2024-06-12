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
    mex = 0
    s = set()
    for x in nums:
        if x > 0:
            ans.append(mex)
        else:
            ans.append(mex - x)
        s.add(ans[-1])
        while mex in s:
            mex += 1
    print(*ans)

for _ in range(int(input())):
    solve()