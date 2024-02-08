import sys
from collections import defaultdict
from string import ascii_lowercase

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
    d = defaultdict(list)
    ans = []
    i = 0
    for x in nums:
        if x == 0:
            ans.append(ascii_lowercase[i])
            d[0].append(ascii_lowercase[i])
            i += 1
        else:
            c = d[x - 1].pop()
            ans.append(c)
            d[x].append(c)
    print("".join(ans))


for _ in range(int(input())):
    solve()
