import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.BITree = [0] * (n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = 0
        while x:
            ans += self.BITree[x]
            x &= x - 1
        return ans
    
    def range_sum(self, l: int, r: int) -> int:
        return self.query(r) - self.query(l - 1)

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += x & -x

    def getPairOfInversion(nums: list) -> int:
        bit = BIT(max(nums))
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            res += bit.query(nums[i])
            bit.add(nums[i] + 1, 1)
        return res
    
def solve() -> None:
    n, k = mint()
    nums = ints()
    pows = ints()

    # 同一个数的0..k序列内的逆序对
    ans = BIT.getPairOfInversion(pows) * n % MOD

    bit = BIT(n * 2)
    for i, x in enumerate(nums):
        # x < y <= 2x
        l, r = (x + 1) // 2, x - 1
        for i in range(1, k):
            if r <= 0:
                break
            # 0, 0, 0, 1, 2, ..., k - i
            ans = (ans + bit.range_sum(l, r) * (k - i + 1) * (k - i) // 2) % MOD
            l, r = (l + 1) // 2, l - 1
        
        l, r = x + 1, x * 2
        for i in range(k - 1):
            if l >= n * 2:
                break
            ans = (ans + bit.range_sum(l, min(r, n * 2 - 1)) * (k * k - (k - i) * (k - i - 1) // 2)) % MOD
            l, r = r + 1, r * 2

        if l < n * 2:
            ans = (ans + bit.range_sum(l, n * 2 - 1) * k * k) % MOD
        
        bit.add(x, 1)
    
    print(ans)
            


for _ in range(int(input())):
    solve()
