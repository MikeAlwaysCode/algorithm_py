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
    def __init__(self, s: str) -> None:
        n = len(s)
        self.n = n
        self.tree = [[0] * 4 for _ in range(4 * n)]
        self.lazy = [0] * (4 * n)
        self.build(s, 1, 1, n)
        
    def build(self, s: str, o: int, l: int, r: int) -> None:
        if l == r:
            c1 = int(s[l - 1]) & 1
            self.tree[o] = [c1 ^ 1, c1, 1, 1]
            return

        m = (l + r) >> 1
        self.build(s, o * 2, l, m)
        self.build(s, o * 2 + 1, m + 1, r)
        self.pushUp(o)

    def do(self, o: int) -> None:
        self.tree[o][0], self.tree[o][1], self.tree[o][2], self.tree[o][3] = self.tree[o][1], self.tree[o][0], self.tree[o][3], self.tree[o][2]
        self.lazy[o] ^= 1

    def pushUp(self, o: int) -> None:
        self.tree[o][0] = self.tree[o * 2][0] + self.tree[o * 2 + 1][0]
        self.tree[o][1] = self.tree[o * 2][1] + self.tree[o * 2 + 1][1]
        self.tree[o][2] = max(self.tree[o * 2][0] + self.tree[o * 2 + 1][2], self.tree[o * 2][2] + self.tree[o * 2 + 1][1])
        self.tree[o][3] = max(self.tree[o * 2][1] + self.tree[o * 2 + 1][3], self.tree[o * 2][3] + self.tree[o * 2 + 1][0])

    def pushDown(self, o: int) -> None:
        self.do(o * 2)
        self.do(o * 2 + 1)
        self.lazy[o] ^= 1

    def update(self, o: int, l: int, r: int, L: int, R: int) -> None:
        if L <= l and r <= R:
            self.do(o)
            return

        if self.lazy[o]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o)

        m = (l + r) >> 1
        if m >= L:  # 左节点在更新区间
            self.update(o * 2, l, m, L, R)
        if m < R:   # 右节点在更新区间
            self.update(o * 2 + 1, m + 1, r, L, R)

        self.pushUp(o)  # 从左右节点更新当前节点值


def solve() -> None:
    n, m = mint()
    s = input()
    st = SegTree(s)

    for _ in range(m):
        qry = input().split()
        if qry[0] == "switch":
            l, r = int(qry[1]), int(qry[2])
            st.update(1, 1, n, l, r)
        else:
            print(st.tree[1][2])

solve()
