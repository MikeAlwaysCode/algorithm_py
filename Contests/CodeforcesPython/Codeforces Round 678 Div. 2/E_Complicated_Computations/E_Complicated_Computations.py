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

'''
class SegTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [-1] * (4 * n)

    def do(self, o: int, val: int) -> None:
        self.tree[o] = max(self.tree[o], val)

    def op(self, a: int, b: int) -> int:
        return min(a, b)

    def pushUp(self, o: int) -> None:
        self.tree[o] = self.op(self.tree[o * 2], self.tree[o * 2 + 1])

    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:
            self.do(o, val)
            return

        m = (l + r) >> 1
        if m >= L:  # 左节点在更新区间
            self.update(o * 2, l, m, L, R, val)
        if m < R:   # 右节点在更新区间
            self.update(o * 2 + 1, m + 1, r, L, R, val)

        self.pushUp(o)  # 从左右节点更新当前节点值

    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if R < l or L > r:
            return 0

        if L <= l and r <= R:
            return self.tree[o]

        m = (l + r) >> 1
        res = self.n
        if m >= L:  # 左节点在查询区间
            res = min(res, self.query(o * 2, l, m, L, R))
        if m < R:   # 右节点在查询区间
            res = min(res, self.query(o * 2 + 1, m + 1, r, L, R))

        return res
'''

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
        # self.X[i] = self.f(self.X[i], x)
        self.X[i] = x
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

    vis = [False] * (n + 2)
    
    # Segment Tree: 779 ms, 202 ms
    last = [-1] * (n + 2)
    # sg = SegTree(n)
    sg = SegmentTree([-1] * (n + 1), n, min)
    for i, x in enumerate(nums):
        if x == 1:
            vis[2] = True
        else:
            vis[1] = True
            # left = sg.query(1, 1, n, 1, x - 1)
            if not vis[x] and sg.getrange(1, x) > last[x]:
                vis[x] = True
        last[x] = i
        # sg.update(1, 1, n, x, x, i)
        sg.update(x, i)
    
    for x in range(2, n + 2):
        # left = sg.query(1, 1, n, 1, x - 1)
        if not vis[x] and sg.getrange(1, x) > last[x]:
            vis[x] = True
            
    '''
    # 值域分块 686 ms
    size = int(n ** 0.5)
    # size = int(1.4 * n // (int(n ** 0.5) + 1)) + 1
    cnt = (n + size - 1) // size
    pos = [[] for _ in range(n + 2)]
    block_pos = [0] * (n + 1)
    s, e = [0] * (cnt + 1), [0] * (cnt + 1)
    exist_id = [0] * (n + 1)
    exist_num = [0] * (n + 1)
    check = [0] * (n + 1)

    for i, x in enumerate(nums, 1):
        pos[x].append(i)
        block_pos[i] = (i - 1) // size + 1

    # 块内起止位置
    for i in range(1, cnt + 1):
        s[i], e[i] = (i - 1) * size + 1, i * size
    e[cnt] = n

    # 查询离线
    qry = []
    for x in range(1, n + 2):
        l = 1
        for r in pos[x]:
            if l == r:
                l = r + 1
                continue
            if r - l >= x - 1:
                qry.append((l, r - 1))
            l = r + 1
        if l < n and n - l + 1 >= x - 1:
            qry.append((l, n))
    # qry.sort()
    # qry.sort(key = lambda x: (block_pos[x[0]], x[1]))
    qry.sort(key = lambda x: (block_pos[x[0]], x[1] if block_pos[x[0]] & 1 else -x[1]))
    
    def add(i: int):
        x = nums[i - 1]
        if check[x] == 0:
            id = block_pos[x]      # 值域段编号
            exist_id[id] += 1      # 值域段数量+1
            exist_num[x] += 1      # 值数量+1
        check[x] += 1
    
    def delete(i: int):
        x = nums[i - 1]
        check[x] -= 1
        if check[x] == 0:
            id = block_pos[x]
            exist_id[id] -= 1
            exist_num[x] -= 1
    
    def query_mex() -> int:
        id = 1
        while id <= cnt and exist_id[id] == e[id] - s[id] + 1:
            id += 1
        if id > cnt:
            return n + 1
        x = s[id]
        while x <= e[id] and exist_num[x]:
            x += 1
        return x

    l, r = 1, 0
    for nl, nr in qry:
        while l < nl:
            delete(l)
            l += 1
        while nl < l:
            l -= 1
            add(l)
        while r < nr:
            r += 1
            add(r)
        while nr < r:
            delete(r)
            r -= 1
        vis[query_mex()] = True
    '''
    ans = 1
    while ans < n + 2 and vis[ans]:
        ans += 1
    print(ans)

solve()
