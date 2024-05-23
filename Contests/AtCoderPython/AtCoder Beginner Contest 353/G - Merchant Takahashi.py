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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

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
    n, c = mint()
    
    st1 = SegmentTree(n + 1, -math.inf, max) # x - ci
    st2 = SegmentTree(n + 1, -math.inf, max) # x + ci

    st1.update(1, - c)
    st2.update(1, c)

    ans = 0
    for _ in range(sint()):
        t, p = mint()
        cur = p + max(st2.getrange(1, t + 1) - t * c, st1.getrange(t, n + 1) + t * c)
        ans = max(ans, cur)
        st1.update(t, cur - c * t)
        st2.update(t, cur + c * t)
        
    print(ans)

solve()
