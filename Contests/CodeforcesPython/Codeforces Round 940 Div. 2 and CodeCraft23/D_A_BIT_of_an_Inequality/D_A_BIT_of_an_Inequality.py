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
    ans = mask = 0
    cnt0 = [[1] * 31, [0] * 31]
    cnt1 = [[0] * 31 for _ in range(2)]
    for x in nums:
        mask ^= x
        for bit in range(30, -1, -1):
            if (x >> bit) & 1:
                cnt1[0][bit] += cnt0[0][bit]
                cnt1[1][bit] += cnt0[1][bit]
                break
        for bit in range(30, -1, -1):
            cnt0[(mask >> bit) & 1][bit] += 1
            ans += cnt1[(mask >> bit) & 1][bit]
    print(ans)


for _ in range(int(input())):
    solve()
