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

class SparseTable:
    def __init__(self, nums: list, op) -> None:
        self.pow2 = [1]
        for _ in range(20):
            self.pow2.append(2 * self.pow2[-1])
        self.op = op
        self.st = []
        s, l = nums, 1
        self.st.append(s)
        while l * 2 <= len(nums):
            ns = []
            for i in range(len(s) - l):
                ns.append(self.op(s[i], s[i + l]))
            s = ns
            self.st.append(s)
            l *= 2

    def query(self, l: int, r: int):
        s = len(bin(r - l + 1)) - 3
        res = self.op(self.st[s][l], self.st[s][r - self.pow2[s] + 1])
        return res

class SegmentTree():
    def __init__(self, init, unitX, f):
        self.f = f  # (X, X) -> X
        self.unitX = unitX
        self.f = f
        if type(init) == int:
            self.n = init
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
        else:
            self.n = len(init)
            self.n = 1 << (self.n - 1).bit_length()
            # len(init)が2の累乗ではない時UnitXで埋める
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            # 配列のindex1まで埋める
            for i in range(self.n - 1, 0, -1):
                self.X[i] = self.f(self.X[i * 2], self.X[i * 2 | 1])

    def update(self, i, x):
        """0-indexedのi番目の値をxで置換"""
        # 最下段に移動
        i += self.n
        self.X[i] = self.f(self.X[i], x)
        # 上向に更新
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i * 2], self.X[i * 2 | 1])
            i >>= 1

    def getvalue(self, i):
        """元の配列のindexの値を見る"""
        return self.X[i + self.n]

    def getrange(self, l, r):
        """区間[l, r)でのfを行った値"""
        l += self.n
        r += self.n
        al = self.unitX
        ar = self.unitX
        while l < r:
            # 左端が右子ノードであれば
            if l & 1:
                al = self.f(al, self.X[l])
                l += 1
            # 右端が右子ノードであれば
            if r & 1:
                r -= 1
                ar = self.f(self.X[r], ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)
    
def solve() -> None:
    n = sint()
    nums = ints()
    st = SparseTable(nums, math.gcd)

    def min_merge(x, y):
        mnx, cntx = x
        mny, cnty = y
        if mnx < mny:
            return (mnx, cntx)
        if mnx > mny:
            return (mny, cnty)
        return (mnx, cntx + cnty)
    
    # 842 ms
    seg = SegmentTree(n, (math.inf, 0), min_merge)
    for i, x in enumerate(nums):
        seg.update(i, (x, 1))
        
    # 998 ms
    # seg = SegmentTree(list((x, 1) for x in nums), (math.inf, 0), min_merge)

    for _ in range(sint()):
        l, r = mint()
        g = st.query(l - 1, r - 1)
        mn, cnt = seg.getrange(l - 1, r)
        if g == mn:
            print(r - l + 1 - cnt)
        else:
            print(r - l + 1)


solve()
