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
    nums = input().split()
    ans = 0
    cnt = [[[0] * 50 for _ in range(6)] for _ in range(6)]
    for x in nums:
        m = len(x)
        left, right = sum(map(int, x)), 0
        cnt[m][0][left] += 1
        for i in range(m - 1, -1, -1):
            left -= int(x[i])
            right += int(x[i])
            cnt[i][m - i][left - right] += 1
    for x in nums:
        m = len(x)
        for l in range(m + 5, m, -1):
            if l & 1: continue
            d = l // 2
            left = min(d, l - m)
            right = max(0, d - m)
            if d >= m:
                t = sum(map(int, x))
            else:
                t = -sum(map(int, x[:m - d])) + sum(map(int, x[m - d:]))
            ans += cnt[left][right][t]
    
    print(ans)



solve()