import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

class SegTree:
    def __init__(self, nums: list) -> None:
        n = len(nums[0])
        self.n = n
        self.tree = [[0] * 3 for _ in range(4 * n)]
        self.lazy = [[0] * 2 for _ in range(4 * n)]
        self.build(nums, 1, 1, n)
        
    def build(self, nums: list, o: int, l: int, r: int) -> None:
        if l == r:
            self.tree[o][0] = nums[0][l - 1]
            self.tree[o][1] = nums[1][l - 1]
            self.tree[o][2] = self.tree[o][0] * self.tree[o][1] % MOD
            return
        m = (l + r) >> 1
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
        self.pushUp(o)

    def do(self, o: int, l: int, r: int, t: int, val: int) -> None:
        self.tree[o][t] = (self.tree[o][t] + val * (r - l + 1)) % MOD
        self.tree[o][2] = (self.tree[o][2] + self.tree[o][t ^ 1] * val) % MOD
        self.lazy[o][t] += val

    def pushUp(self, o: int) -> None:
        self.tree[o][0] = (self.tree[o * 2][0] + self.tree[o * 2 + 1][0]) % MOD
        self.tree[o][1] = (self.tree[o * 2][1] + self.tree[o * 2 + 1][1]) % MOD
        self.tree[o][2] = (self.tree[o * 2][2] + self.tree[o * 2 + 1][2]) % MOD

    def pushDown(self, o: int, l: int, r: int) -> None:
        m = (l + r) >> 1
        if self.lazy[o][0]:
            self.do(o * 2, l, m, 0, self.lazy[o][0])
            self.do(o * 2 + 1, m + 1, r, 0, self.lazy[o][0])
            self.lazy[o][0] = 0
        
        if self.lazy[o][1]:
            self.do(o * 2, l, m, 1, self.lazy[o][1])
            self.do(o * 2 + 1, m + 1, r, 1, self.lazy[o][1])
            self.lazy[o][1] = 0

    def update(self, o: int, l: int, r: int, L: int, R: int, t: int, val: int) -> None:
        if L <= l and r <= R:   # 当前区间已完全包含在更新区间，不需要继续往下更新，存在lazy
            self.do(o, l, r, t, val)
            return
        if self.lazy[o][0] or self.lazy[o][1]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o, l, r)
        m = (l + r) >> 1
        if m >= L:  # 左节点在更新区间
            self.update(o * 2, l, m, L, R, t, val)
        if m < R:   # 右节点在更新区间
            self.update(o * 2 + 1, m + 1, r, L, R, t, val)
        self.pushUp(o)  # 从左右节点更新当前节点值

    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if R < l or L > r:
            return 0
        if L <= l and r <= R:
            return self.tree[o][2]
        if self.lazy[o][0] or self.lazy[o][1]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o, l, r)
        m = (l + r) >> 1
        res = 0
        if m >= L:  # 左节点在查询区间
            res = (res + self.query(o * 2, l, m, L, R)) % MOD
        if m < R:   # 右节点在查询区间
            res = (res + self.query(o * 2 + 1, m + 1, r, L, R)) % MOD
        return res

def solve() -> None:
    n, q = mint()
    nums = list(ints() for _ in range(2))
    st = SegTree(nums)
    for _ in range(q):
        qry = ints()
        if qry[0] == 3:
            print(st.query(1, 1, n, qry[1], qry[2]))
        else:
            st.update(1, 1, n, qry[1], qry[2], qry[0] - 1, qry[3])


solve()
