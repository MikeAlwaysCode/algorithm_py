import math
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
    n, x, y, s = mint()
    
    # 计算通过若干段(0, 1, 2, ... ) 构成和k的最小数组长度
    dp = [math.inf] * (s + 1)
    # p = [0] * (s + 1)
    dp[0] = 0
    for k in range(1, s + 1):
        l, m = 2, 1
        while m <= k:
            dp[k] = min(dp[k], dp[k - m] + l)
            # if dp[k - m] + l < dp[k]:
            #     dp[k] = dp[k - m] + l
            #     p[k] = l
            l += 1
            m = l * (l - 1) // 2
    
    # 枚举前面的(x, x + y, x + 2y, ... ) 看是否存在答案
    for k in range(n):
        pres = x * (k + 1) + k * (k + 1) // 2 * y
        if pres > s:
            break

        need_sum = s - pres - (n - k - 1) * (x % y)
        if need_sum < 0 or need_sum % y:
            continue
        
        cnt = need_sum // y
        if dp[cnt] > n - k - 1:
            continue

        ans = list(range(x, x + k * y + 1, y)) + [x % y] * (n - k - 1 - dp[cnt])
        # 通过dp回溯构造
        # while cnt:
        #     l = p[cnt]
        #     cnt -= l * (l - 1) // 2
        #     ans.extend(range(x%y, x%y + (l - 1) * y + 1, y))
        while cnt:
            l, m = 2, 1
            while m <= cnt:
                if dp[cnt] == dp[cnt - m] + l:
                    ans.extend(range(x%y, x%y + (l - 1) * y + 1, y))
                    cnt -= m
                    break
                l += 1
                m = l * (l - 1) // 2

        print("YES")
        print(*ans)
        return

    print("NO")


for _ in range(int(input())):
    solve()
