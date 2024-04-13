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
    k = max(nums)
    d = [0] * (k + 1)
    idx = sorted(range(n), key = lambda x: -nums[x])
    seen = [False] * n
    i = s = 0
    for j in range(k, 0, -1):
        while i < n and nums[idx[i]] >= j:
            s += 1
            x = idx[i]
            seen[x] = True
            if x and seen[x - 1] and x < n - 1 and seen[x + 1]:
                s -= 2
            elif (x and seen[x - 1]) or (x < n - 1 and seen[x + 1]):
                s -= 1
            i += 1
        d[j] = s
    # print(d)
    ans = [0] * k
    for i in range(1, k + 1):
        for j in range(0, k, i):
            ans[i - 1] += d[j + 1]
    print(*ans)

solve()
