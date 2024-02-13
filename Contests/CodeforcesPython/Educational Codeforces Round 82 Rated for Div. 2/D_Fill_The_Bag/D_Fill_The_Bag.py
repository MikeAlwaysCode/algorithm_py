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
    nums = ints()
    cnt = [0] * 62
    for x in nums:
        cnt[x.bit_length() - 1] += 1
    ans = 0
    for bit in range(61):
        if (n >> bit) & 1:
            j = bit
            while j < 62 and cnt[j] == 0:
                j += 1
            if j > 61:
                print(-1)
                return
            ans += j - bit
            for i in range(bit, j):
                cnt[i] += 1
            cnt[j] -= 1
        cnt[bit + 1] += cnt[bit] // 2
    print(ans)


for _ in range(int(input())):
    solve()
