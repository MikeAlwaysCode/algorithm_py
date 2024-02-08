class Node:
    __slots__ = ("left", "right", "l", "r", "mid", "v")

    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.v = -1

class SegmentTree:
    def __init__(self):
        self.root = Node(1, int(1e9))

    def modify(self, l, r, v, node=None):
        if l > r:
            return
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            node.v = max(node.v, v)
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modify(l, r, v, node.left)
        if r > node.mid:
            self.modify(l, r, v, node.right)
        self.pushup(node)

    def query(self, l, r, node=None):
        if l > r:
            return 0
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            return node.v
        self.pushdown(node)
        v = -1
        if l <= node.mid:
            v = max(v, self.query(l, r, node.left))
        if r > node.mid:
            v = max(v, self.query(l, r, node.right))
        return v

    def pushup(self, node):
        node.v = max(node.left.v, node.right.v)

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.r)


mx = 5 * 10 ** 5

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
    n, d = 4, 2
    nums = [3, 5, 1, 2]
    st = SegmentTree([0] * mx, 0, max)
    ans = 1
    for x in nums:
        res = st.getrange(max(1, x - d), min(mx, x + d) + 1) + 1
        ans = max(ans, res)
        st.update(x, res)
    print(ans)

    
    def min_merge(x, y):
        mnx, cntx = x
        mny, cnty = y
        if mnx < mny:
            return (mnx, cntx)
        if mnx > mny:
            return (mny, cnty)
        return (mnx, cntx + cnty)
