#
# @lc app=leetcode.cn id=1649 lang=python3
#
# [1649] 通过指令创建有序数组
#
# https://leetcode.cn/problems/create-sorted-array-through-instructions/description/
#
# algorithms
# Hard (48.96%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 8.3K
# Testcase Example:  '[1,5,6,2]'
#
# 给你一个整数数组 instructions ，你需要根据 instructions 中的元素创建一个有序数组。一开始你有一个空的数组 nums ，你需要
# 从左到右 遍历 instructions 中的元素，将它们依次插入 nums 数组中。每一次插入操作的 代价 是以下两者的 较小值 ：
# 
# 
# nums 中 严格小于  instructions[i] 的数字数目。
# nums 中 严格大于  instructions[i] 的数字数目。
# 
# 
# 比方说，如果要将 3 插入到 nums = [1,2,3,5] ，那么插入操作的 代价 为 min(2, 1) (元素 1 和  2 小于 3 ，元素 5
# 大于 3 ），插入后 nums 变成 [1,2,3,3,5] 。
# 
# 请你返回将 instructions 中所有元素依次插入 nums 后的 总最小代价 。由于答案会很大，请将它对 10^9 + 7 取余 后返回。
# 
# 
# 
# 示例 1：
# 
# 输入：instructions = [1,5,6,2]
# 输出：1
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 5 ，代价为 min(1, 0) = 0 ，现在 nums = [1,5] 。
# 插入 6 ，代价为 min(2, 0) = 0 ，现在 nums = [1,5,6] 。
# 插入 2 ，代价为 min(1, 2) = 1 ，现在 nums = [1,2,5,6] 。
# 总代价为 0 + 0 + 0 + 1 = 1 。
# 
# 示例 2:
# 
# 输入：instructions = [1,2,3,6,5,4]
# 输出：3
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 2 ，代价为 min(1, 0) = 0 ，现在 nums = [1,2] 。
# 插入 3 ，代价为 min(2, 0) = 0 ，现在 nums = [1,2,3] 。
# 插入 6 ，代价为 min(3, 0) = 0 ，现在 nums = [1,2,3,6] 。
# 插入 5 ，代价为 min(3, 1) = 1 ，现在 nums = [1,2,3,5,6] 。
# 插入 4 ，代价为 min(3, 2) = 2 ，现在 nums = [1,2,3,4,5,6] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 2 = 3 。
# 
# 
# 示例 3：
# 
# 输入：instructions = [1,3,3,3,2,4,2,1,2]
# 输出：4
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3,3] 。
# 插入 2 ，代价为 min(1, 3) = 1 ，现在 nums = [1,2,3,3,3] 。
# 插入 4 ，代价为 min(5, 0) = 0 ，现在 nums = [1,2,3,3,3,4] 。
# ​​​​​插入 2 ，代价为 min(1, 4) = 1 ，现在 nums = [1,2,2,3,3,3,4] 。
# 插入 1 ，代价为 min(0, 6) = 0 ，现在 nums = [1,1,2,2,3,3,3,4] 。
# 插入 2 ，代价为 min(2, 4) = 2 ，现在 nums = [1,1,2,2,2,3,3,3,4] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= instructions.length <= 10^5
# 1 <= instructions[i] <= 10^5
# 
# 
#

# @lc code=start
class BitTree:
    def __init__(self, n: int):
        self.nums = [0 for _ in range(n + 1)]
        self.n = n
    
    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, i: int, diff: int) -> None:
        i += 1
        while i <= self.n:
            self.nums[i] += diff
            i += self.lowbit(i)

    def query(self, i: int) -> int:
        i += 1
        presum = 0
        while i:
            presum += self.nums[i]
            i -= self.lowbit(i)
        return presum

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = max(instructions)

        BT = BitTree(n + 1)

        res = 0
        for i, x in enumerate(instructions):
            lessesr = BT.query(x - 1)
            greater = i - BT.query(x)
            res += min(lessesr, greater)
            res %= MOD
            BT.update(x, 1)
        return res
'''
class SegmentTree:
    def __init__(self, n: int):
        self.treesum = [0 for _ in range(4 * n)]
        self.n = n

    def update(self, i: int, diff: int) -> None:
        return self._update(0, 0, self.n - 1, i, diff)
    
    def query(self, ql: int, qr: int) -> int:
        return self._query(0, 0, self.n - 1, ql, qr)

    def _update(self, root: int, l: int, r: int, ID: int, diff: int) -> int:
        if l == r == ID:
            self.treesum[root] += diff
            return 
        left = 2 * root + 1
        right = 2 * root + 2
        mid = (l + r) // 2
        if ID <= mid:
            self._update(left, l, mid, ID, diff)
        else:
            self._update(right, mid + 1, r, ID, diff)
        self.treesum[root] = self.treesum[left] + self.treesum[right]
    
    def _query(self, root: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql == l and r == qr:
            return self.treesum[root]
        left = 2 * root + 1
        right = 2 * root + 2
        mid = (l + r) // 2
        if qr <= mid:
            return self._query(left, l, mid, ql, qr)
        elif mid + 1 <= ql:
            return self._query(right, mid + 1, r, ql, qr)
        else:
            return self._query(left, l, mid, ql, mid) + self._query(right, mid + 1, r, mid + 1, qr)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = max(instructions)
        ST = SegmentTree(n + 1)
        res = 0
        for x in instructions:
            lesser = ST.query(1, x - 1) if 1 <= x-1 else 0
            greater = ST.query(x + 1, n) if x+1 <= n else 0
            res += min(lesser, greater)
            res %= MOD
            ST.update(x, 1)
        return res
'''
'''
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        class Node:#线段树
            def __init__(self, i, j):
                self.l = i
                self.r = j
                self.c = 0
                if i + 1 == j:
                    return
                mid = (i + j) // 2
                self.left = Node(i, mid)
                self.right = Node(mid, j)
                
            def insert(self, i):
                if self.l + 1 == self.r:#区间大小为1，区间数值数量 + 1，且严格大于和严格小于都为0
                    self.c += 1
                    return [0, 0]
                mid = (self.l + self.r) // 2
                if mid <= i:#右节点插入
                    res = self.right.insert(i) #右节点的结果
                    res[0] += self.left.c#加上左节点的全部严格小于数量
                else:#左节点插入
                    res = self.left.insert(i)#左节点的结果
                    res[1] += self.right.c#加上右节点的全部严格大于数量
                self.c += 1#更新线段树区间值
                return res
            
        s = sorted(set(instructions))
        l = len(s)
        d = {}
        for i in range(l - 1, -1, -1):
            d[s[i]] = i
        node = Node(0, l)
        res = 0
        for n in instructions:
            res += min(node.insert(d[n]))
        return res % (10 ** 9 + 7)
'''
# @lc code=end

