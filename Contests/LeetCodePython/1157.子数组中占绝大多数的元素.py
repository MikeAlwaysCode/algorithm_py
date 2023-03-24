#
# @lc app=leetcode.cn id=1157 lang=python3
#
# [1157] 子数组中占绝大多数的元素
#
# https://leetcode.cn/problems/online-majority-element-in-subarray/description/
#
# algorithms
# Hard (36.01%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    4.6K
# Total Submissions: 12.8K
# Testcase Example:  '["MajorityChecker","query","query","query"]\n[[[1,1,2,2,1,1]],[0,5,4],[0,3,3],[2,3,2]]'
#
# 设计一个数据结构，有效地找到给定子数组的 多数元素 。
# 
# 子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。
# 
# 实现 MajorityChecker 类:
# 
# 
# MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。
# int query(int left, int right, int threshold) 返回子数组中的元素  arr[left...right]
# 至少出现 threshold 次数，如果不存在这样的元素则返回 -1。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入:
# ["MajorityChecker", "query", "query", "query"]
# [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
# 输出：
# [null, 1, -1, 2]
# 
# 解释：
# MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // 返回 1
# majorityChecker.query(0,3,3); // 返回 -1
# majorityChecker.query(2,3,2); // 返回 2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 2 * 10^4
# 1 <= arr[i] <= 2 * 10^4
# 0 <= left <= right < arr.length
# threshold <= right - left + 1
# 2 * threshold > right - left + 1
# 调用 query 的次数最多为 10^4 
# 
# 
#

# @lc code=start
class MajorityChecker:

    def __init__(self, arr: List[int]):
        class Node:
            def __init__(self, i, j):
                self.l = i
                self.r = j
                if i + 1 == j:
                    self.k = arr[i]
                    self.c = 1
                    return
                mid = (i + j) // 2
                self.left = Node(i, mid)
                self.right = Node(mid, j)
                self.build()
                
            def build(self):#摩尔投票
                if self.left.k == self.right.k:
                    self.k = self.left.k
                    self.c = self.left.c + self.right.c
                else:
                    if self.left.c > self.right.c:
                        self.k = self.left.k
                        self.c = self.left.c - self.right.c
                    else:
                        self.k = self.right.k
                        self.c = self.right.c - self.left.c
                        
            def find(self, i, j):
                if self.l == i and self.r == j:
                    return self.k, self.c
                mid = (self.l + self.r) // 2
                if mid >= j:
                    return self.left.find(i, j)
                elif mid <= i:
                    return self.right.find(i, j)
                else:
                    left = self.left.find(i, mid)
                    right = self.right.find(mid, j)
                    if left[0] == right[0]:
                        return left[0], left[1] + right[1]
                    else:
                        if left[1] > right[1]:
                            return left[0], left[1] - right[1]
                        else:
                            return right[0], right[1] - left[1]
                        
        self.node = Node(0, len(arr))
        self.d = {}
        for i, n in enumerate(arr):
            if n not in self.d:#将数值映射为索引列表
                self.d[n] = []
            self.d[n].append(i)
                


    def query(self, left: int, right: int, threshold: int) -> int:
        n, c = self.node.find(left, right + 1)
        c = bisect.bisect_right(self.d[n], right) - bisect.bisect_left(self.d[n], left)#通过二分找到区间内的数量
        return n if c >= threshold else -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end

