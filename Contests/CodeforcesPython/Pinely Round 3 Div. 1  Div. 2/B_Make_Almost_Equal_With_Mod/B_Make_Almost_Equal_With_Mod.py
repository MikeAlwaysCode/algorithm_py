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
    if n == 1:
        print(1)
        return
    for bit in range(58):
        cnt = 0
        for x in nums:
            cnt |= 1 << ((x >> bit) & 1)
        if cnt == 3:
            ans = 1 << (bit + 1)
            break
    print(ans)


for _ in range(int(input())):
    solve()
