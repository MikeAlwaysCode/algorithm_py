import sys
from collections import Counter

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
    s = odd = even = 0
    for x in nums:
        s += x
        if x & 1:
            odd += 1
        else:
            even += 1
        ans.append(s)
        if odd + even > 1:
            ans[-1] -= odd // 3
            if odd % 3 == 1:
                ans[-1] -= 1
    print(*ans)


for _ in range(int(input())):
    solve()