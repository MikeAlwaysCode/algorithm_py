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

class SegTree:
    def __init__(self, nums: list) -> None:
        n = len(nums)
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.build(nums, 1, 1, n)
        
    def build(self, nums: list, o: int, l: int, r: int) -> None:
        if l == r:
            self.tree[o] = nums[l - 1]
            return

        m = (l + r) >> 1
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
        self.pushUp(o)

    def do(self, o: int, l: int, r: int, val: int) -> None:
        self.tree[o] = val
        self.lazy[o] = val

    def pushUp(self, o: int) -> None:
        self.tree[o] = self.tree[o * 2] | self.tree[o * 2 + 1]

    def pushDown(self, o: int, l: int, r: int) -> None:
        m = (l + r) >> 1
        self.do(o * 2, l, m, self.lazy[o])           # 调用相应的更新操作方法
        self.do(o * 2 + 1, m + 1, r, self.lazy[o])
        self.lazy[o] = 0

    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:   # 当前区间已完全包含在更新区间，不需要继续往下更新，存在lazy
            self.do(o, l, r, val)
            return

        if self.lazy[o]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o, l, r)

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

        if self.lazy[o]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o, l, r)

        m = (l + r) >> 1
        res = 0
        if m >= L:  # 左节点在查询区间
            res |= self.query(o * 2, l, m, L, R)
        if m < R:   # 右节点在查询区间
            res |= self.query(o * 2 + 1, m + 1, r, L, R)

        return res

def popcount(x):
    x = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x & 0x0f0f0f0f0f0f0f0f) + ((x >> 4) & 0x0f0f0f0f0f0f0f0f)
    x = (x & 0x00ff00ff00ff00ff) + ((x >> 8) & 0x00ff00ff00ff00ff)
    x = (x & 0x0000ffff0000ffff) + ((x >> 16) & 0x0000ffff0000ffff)
    x = (x & 0x00000000ffffffff) + ((x >> 32) & 0x00000000ffffffff)
    return x

def solve() -> None:
    n, m = mint()
    c = ints()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    tin = [-1] * n
    tout = [-1] * n
    q = [0]
    t = 0
    while q:
        u = q[-1]
        if tin[u] == -1:
            t += 1
            tin[u] = t
            for v in g[u]:
                if tin[v] >= 0:continue
                q.append(v)
        else:
            q.pop()
            tout[u] = t

    pw2 = [1] * 62
    for i in range(1, len(pw2)):
        pw2[i] = pw2[i - 1] << 1
    
    nums = [-1] * n
    for i in range(n):
        # nums[tin[i] - 1] = 1 << (c[i] - 1)
        nums[tin[i] - 1] = pw2[c[i]]
    
    st = SegTree(nums)

    l1 = pow(2, (n + 1).bit_length())
    l2 = 2 * l1
    tree, lazy = [0] * l2, [0] * l2
    def f(i):
        if not lazy[i]:
            return
        tree[i] = lazy[i]
        if i < l1:
            lazy[i << 1] = lazy[i]
            lazy[i << 1 ^ 1] = lazy[i]
        lazy[i] = 0
        return
    
    def update(l, r, s):
        q, ll, rr, i = [1], [0], [l1 - 1], 0
        while len(q) ^ i:
            j = q[i]
            l0, r0 = ll[i], rr[i]
            if l <= l0 and r0 <= r:
                if s:
                    lazy[j] = s
                f(j)
                i += 1
                continue
            f(j)
            m0 = (l0 + r0) >> 1
            if l <= m0 and l0 <= r:
                q.append(j << 1)
                ll.append(l0)
                rr.append(m0)
            if l <= r0 and m0 + 1 <= r:
                q.append(j << 1 ^ 1)
                ll.append(m0 + 1)
                rr.append(r0)
            i += 1
        for i in q[::-1]:
            if i < l1:
                j, k = i << 1, i << 1 ^ 1
                f(j)
                f(k)
                tree[i] = tree[j] | tree[k]
        return
    
    def get_ans(s, t):
        update(s, t, 0)
        s += l1
        t += l1
        ans = 0
        while s <= t:
            if s % 2:
                ans |= tree[s]
                s += 1
            s >>= 1
            if not t % 2:
                ans |= tree[t]
                t -= 1
            t >>= 1
        return ans

    for _ in range(m):
        qry = ints()
        if qry[0] == 1:
            u, c = qry[1] - 1, qry[2]
            # st.update(1, 1, n, tin[u], tout[u], 1 << (c - 1))
            st.update(1, 1, n, tin[u], tout[u], pw2[c])
        else:
            u = qry[1] - 1
            res = st.query(1, 1, n, tin[u], tout[u])
            # print(bin(res)[2:].count('1'))
            print(popcount(res))


solve()
