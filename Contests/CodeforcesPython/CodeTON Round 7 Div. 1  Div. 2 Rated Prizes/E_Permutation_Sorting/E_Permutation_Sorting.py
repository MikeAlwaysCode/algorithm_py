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

class BIT:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)
        self.n = n
        self.BITree = [0] * (self.n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = 0
        while x:
            ans += self.BITree[x]
            x -= self.lowbit(x)
        return ans

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += self.lowbit(x)

    def update(self, x: int, val: int) -> None:
        self.add(x + 1, val - self.nums[x])
        self.nums[x] = val

def solve() -> None:
    n = sint()
    nums = ints()
    g = []
    bit = BIT(n * 2)
    for i, x in enumerate(nums, 1):
        if i <= x:
            g.append((i, x))
            g.append((i + n, x + n))
        else:
            g.append((i, x + n))
    ans = [0] * n
    g.sort(reverse=True)
    for s, t in g:
        if s <= n:
            ans[nums[s - 1] - 1] = t - s - bit.query(t) + bit.query(s - 1)
        bit.add(t, 1)
    print(*ans)


for _ in range(int(input())):
    solve()
