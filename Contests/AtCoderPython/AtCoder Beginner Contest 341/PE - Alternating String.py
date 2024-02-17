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
    n, q = mint()
    s = list(map(int, list(input())))
    op = BIT(n)
    bit = BIT(n)
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            bit.update(i, 1)
    
    for _ in range(q):
        t, l, r = mint()
        if t == 1:
            op.add(l, 1)
            if r + 1 <= n:
                op.add(r + 1, -1)
            if l - 1 >= 1:
                c1 = s[l - 2] ^ (op.query(l - 1) & 1)
                c2 = s[l - 1] ^ (op.query(l) & 1)
                bit.update(l - 2, int(c1 != c2))
            if r < n:
                c1 = s[r - 1] ^ (op.query(r) & 1)
                c2 = s[r] ^ (op.query(r + 1) & 1)
                bit.update(r - 1, int(c1 != c2))
        else:
            if l == r:
                print("Yes")
                continue
            cnt = bit.query(r - 1)
            if l > 1:
                cnt -= bit.query(l - 1)
            print("Yes" if cnt == r - l else "No")


solve()
