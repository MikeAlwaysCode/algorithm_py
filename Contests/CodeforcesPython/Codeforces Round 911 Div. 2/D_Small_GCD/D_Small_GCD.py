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
    nums.sort()
    ans, mx = 0, nums[-1]
    
    dp = [0] * (mx + 1)
    cnt = [0] * (mx + 1)
    last = [-1] * (mx + 1)
    for i, x in enumerate(nums):
        cnt[x] += 1
        last[x] = i
        
    for d in range(mx, 0, -1):
        left = 0
        for i in range(d, mx + 1, d):
            if cnt[i] == 0:
                continue
            dp[d] += left * cnt[i] * (n - 1 - last[i]) + cnt[i] * (cnt[i] - 1) // 2 * (left + n - 1 - last[i]) + cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
            left += cnt[i]
            
        for i in range(d * 2, mx + 1, d):
            dp[d] -= dp[i]
        ans += d * dp[d]

    '''
    # 858 ms
    pos = [[] for _ in range(mx + 1)]
    for i, x in enumerate(nums):
        pos[x].append(i)

    for d in range(mx, 0, -1):
        tmp = []
        for i in range(d, mx + 1, d):
            tmp.extend(pos[i])
        tmp.sort()
        for i, p in enumerate(tmp):
            dp[d] += i * (n - 1 - p)
        for i in range(d * 2, mx + 1, d):
            dp[d] -= dp[i]
        ans += d * dp[d]
    '''
    print(ans)

for _ in range(int(input())):
    solve()
