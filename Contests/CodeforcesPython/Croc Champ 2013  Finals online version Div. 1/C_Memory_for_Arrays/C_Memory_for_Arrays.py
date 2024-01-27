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
    n, m = mint()
    A = ints()
    B = ints()
    cnt = [0] * 32
    for x in A:
        bit = 0
        while x:
            if x & 1:
                cnt[bit] += 1
            bit += 1
            x >>= 1
    ans = 0
    B.sort()
    for x in B:
        while x < 32 and cnt[x] == 0:
            cnt[x] += 1
            x += 1
        if x > 31:
            break
        cnt[x] -= 1
        ans += 1
    print(ans)


solve()
