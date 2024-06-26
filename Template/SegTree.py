from typing import List


class SegTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (4 * n)

    def do(self, o: int, val: int) -> None:
        self.tree[o] = max(self.tree[o], val)

    def op(self, a: int, b: int) -> int:
        return max(a, b)

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
        res = 0
        if m >= L:  # 左节点在查询区间
            res = max(res, self.query(o * 2, l, m, L, R))
        if m < R:   # 右节点在查询区间
            res = max(res, self.query(o * 2 + 1, m + 1, r, L, R))

        return res
    

class SegTree:
    def __init__(self, nums: list) -> None:
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 1, 1, self.n)
        
    def build(self, nums: list, o: int, l: int, r: int) -> None:
        if l == r:
            self.tree[o] = nums[l - 1]
            return

        m = (l + r) >> 1
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
    
    def do(self, o: int, val: int) -> None:
        self.tree[o] += val
    
    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:
            self.do(o, val)
            return
        
        m = (l + r) >> 1
        if m >= L:
            self.update(o * 2, l, m, L, R, val)
        if m < R:
            self.update(o * 2 + 1, m + 1, r, L, R, val)
    
    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if R < l or L > r:
            return 0
        
        if L <= l and r <= R:
            return self.tree[o]
        
        m = (l + r) >> 1
        # res = 0
        res = self.tree[o]
        if m >= L:
            res += self.query(o * 2, l, m, L, R)
        if m < R:
            res += self.query(o * 2 + 1, m + 1, r, L, R)
        
        return res