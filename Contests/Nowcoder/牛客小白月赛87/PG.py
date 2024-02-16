import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    nums = ints()

    bit = [0] * (n + 1)
    
    def lowbit(x: int) -> int:
        return x & -x
    
    def query(x: int) -> int:
        res = 0
        while x:
            res += bit[x]
            x -= lowbit(x)
        return res

    def add(x: int, val: int):
        while x <= n:
            bit[x] += val
            x += lowbit(x)

    pos = {v:i for i, v in enumerate(nums)}
    dp = [0] * (n + 1)
    
    for d in range(n, 0, -1):
        tmp = []
        for i in range(d, n + 1, d):
            tmp.append(pos[i])
        
        tmp.sort(reverse=True)
        m = len(tmp)
        for i in range(m + 1):
            bit[i] = 0
        for i in tmp:
            dp[d] += query(nums[i] // d)
            add(nums[i] // d + 1, 1)

        for i in range(d * 2, n + 1, d):
            dp[d] -= dp[i]
                
    print(dp[1])
    

solve()
