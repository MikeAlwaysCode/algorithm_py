from typing import List


# 4倍空间
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

    def xor(self, o: int, l: int, r: int) -> None:
        self.tree[o] = r - l + 1 - self.tree[o] # 异或反转
        self.lazy[o] ^= 1

    def do(self, o: int, l: int, r: int, val: int) -> None:
        self.tree[o] = r - l + 1 - self.tree[o] # 异或反转
        self.lazy[o] ^= 1

    def op(self, a: int, b: int) -> int:
        # + - * / max min
        return a + b
    
    def maintain(self, o: int, l: int, r: int) -> None:
        self.tree[o] = self.op(self.tree[l], self.tree[r])
        self.lazy[o] ^= 1

    def pushUp(self, o: int) -> None:
        self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]

    def pushDown(self, o: int, l: int, r: int) -> None:
        m = (l + r) >> 1
        self.do(o * 2, l, m, self.lazy[o])           # 调用相应的更新操作方法
        self.do(o * 2 + 1, m + 1, r, self.lazy[o])
        self.lazy[o] = 0

    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:   # 当前区间已完全包含在更新区间，不需要继续往下更新，存在lazy
            self.xor(o, l, r)
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
            res += self.query(o * 2, l, m, L, R)
        if m < R:   # 右节点在查询区间
            res += self.query(o * 2 + 1, m + 1, r, L, R)

        return res
        
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        s = sum(nums2)
        st = SegTree(nums1)
        
        ans = []
        for op, l, r in queries:
            if op == 1:
                st.update(1, 1, n, l+1, r+1, 1)
            elif op == 2:
                s += l * st.query(1, 1, n, 1, n)
            else:
                ans.append(s)
        return ans
    
# 动态开点
class Node:
    def __init__(self, l, r) -> None:
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.v = 0
        self.todo = 0

class DynSegTree:
    def __init__(self):
        self.root = Node(1, int(1e9))

    def update(self, l, r, v, node=None):
        if l > r:
            return
        
        if node is None:
            node = self.root

        if node.l >= l and node.r <= r:
            node.v = v
            node.todo = v
            return
        
        self.pushdown(node)

        mid = l + r >> 1

        if l <= mid:
            self.update(l, r, v, node.left)
        if r > mid:
            self.update(l, r, v, node.right)

        self.pushup(node)

    def query(self, l, r, node=None):
        if l > r:
            return 0
        
        if node is None:
            node = self.root

        if node.l >= l and node.r <= r:
            return node.v
        
        self.pushdown(node)

        mid = l + r >> 1

        v = 0
        if l <= mid:
            v = max(v, self.query(l, r, node.left))
        if r > mid:
            v = max(v, self.query(l, r, node.right))

        return v

    def pushup(self, node):
        node.v = max(node.left.v, node.right.v)

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)

        if node.right is None:
            node.right = Node(node.mid + 1, node.r)

        if node.todo:
            node.left.v = node.todo
            node.right.v = node.todo
            node.left.todo = node.todo
            node.right.todo = node.todo
            node.todo = 0