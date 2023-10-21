import sys
import math
import os
from io import BytesIO, IOBase

# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

class SegTree:
    def __init__(self, nums: list) -> None:
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(nums, 1, 1, self.n)
        
    def build(self, nums: list, o: int, l: int, r: int) -> None:
        if l == r:
            self.tree[o] = nums[l - 1]
            return

        m = (l + r) >> 1
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
        self.pushUp(o)

    def do(self, o: int, val: int) -> None:
        self.tree[o] += val
        self.lazy[o] += val
    
    def maintain(self, o: int, l: int, r: int) -> None:
        self.tree[o] = min(self.tree[l], self.tree[r])

    def pushUp(self, o: int) -> None:
        self.tree[o] = min(self.tree[o * 2], self.tree[o * 2 + 1])

    def pushDown(self, o: int) -> None:
        self.do(o * 2, self.lazy[o])           # 调用相应的更新操作方法
        self.do(o * 2 + 1, self.lazy[o])
        self.lazy[o] = 0

    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:   # 当前区间已完全包含在更新区间，不需要继续往下更新，存在lazy
            self.do(o, val)
            return

        if self.lazy[o]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o)

        m = (l + r) >> 1
        if m >= L:  # 左节点在更新区间
            self.update(o * 2, l, m, L, R, val)
        if m < R:   # 右节点在更新区间
            self.update(o * 2 + 1, m + 1, r, L, R, val)

        self.pushUp(o)  # 从左右节点更新当前节点值

    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if R < l or L > r:
            return math.inf

        if L <= l and r <= R:
            return self.tree[o]

        if self.lazy[o]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o)

        m = (l + r) >> 1
        res = math.inf
        if m >= L:  # 左节点在查询区间
            res = min(res, self.query(o * 2, l, m, L, R))
        if m < R:   # 右节点在查询区间
            res = min(res, self.query(o * 2 + 1, m + 1, r, L, R))

        return res
    
def solve() -> None:
    n = sint()
    nums = ints()
    st = SegTree(nums)
    for _ in range(sint()):
        qry = tuple(mint())
        if len(qry) == 3:
            l, r, v = qry
            if v == 0: continue
            if l <= r:
                st.update(1, 1, n, l + 1, r + 1, v)
            else:
                st.update(1, 1, n, l + 1, n, v)
                st.update(1, 1, n, 1, r + 1, v)
        else:
            l, r = qry
            if l <= r:
                print(st.query(1, 1, n, l + 1, r + 1))
            else:
                print(min(st.query(1, 1, n, l + 1, n), st.query(1, 1, n, 1, r + 1)))
    
solve()