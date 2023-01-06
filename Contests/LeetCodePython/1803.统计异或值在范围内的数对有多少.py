#
# @lc app=leetcode.cn id=1803 lang=python3
#
# [1803] 统计异或值在范围内的数对有多少
#
# https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/description/
#
# algorithms
# Hard (42.99%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    8.1K
# Total Submissions: 16K
# Testcase Example:  '[1,4,2,7]\n2\n6'
#
# 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。
# 
# 漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR
# nums[j]) <= high 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,4,2,7], low = 2, high = 6
# 输出：6
# 解释：所有漂亮数对 (i, j) 列出如下：
# ⁠   - (0, 1): nums[0] XOR nums[1] = 5 
# ⁠   - (0, 2): nums[0] XOR nums[2] = 3
# ⁠   - (0, 3): nums[0] XOR nums[3] = 6
# ⁠   - (1, 2): nums[1] XOR nums[2] = 6
# ⁠   - (1, 3): nums[1] XOR nums[3] = 3
# ⁠   - (2, 3): nums[2] XOR nums[3] = 5
# 
# 
# 示例 2：
# 
# 输入：nums = [9,8,4,2,1], low = 5, high = 14
# 输出：8
# 解释：所有漂亮数对 (i, j) 列出如下：
# ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
# - (0, 3): nums[0] XOR nums[3] = 11
# - (0, 4): nums[0] XOR nums[4] = 8
# - (1, 2): nums[1] XOR nums[2] = 12
# - (1, 3): nums[1] XOR nums[3] = 10
# - (1, 4): nums[1] XOR nums[4] = 9
# - (2, 3): nums[2] XOR nums[3] = 6
# - (2, 4): nums[2] XOR nums[4] = 5
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 2 * 10^4
# 1 <= low <= high <= 2 * 10^4
# 
# 
#
from collections import Counter
from typing import List

# @lc code=start
HIGH_BIT = 14

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.sum = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num: int) -> None:
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if not cur.children[bit]:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
            cur.sum += 1

    def get(self, num: int, x: int) -> int:
        res = 0
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if (x >> k) & 1:
                if cur.children[bit]:
                    res += cur.children[bit].sum
                if not cur.children[bit ^ 1]:
                    return res
                cur = cur.children[bit ^ 1]
            else:
                if not cur.children[bit]:
                    return res
                cur = cur.children[bit]
        res += cur.sum
        return res

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        '''
        def f(nums: List[int], x: int) -> int:
            res = 0
            trie = Trie()
            for i in range(1, len(nums)):
                trie.add(nums[i - 1])
                res += trie.get(nums[i], x)
            return res
        return f(nums, high) - f(nums, low - 1)
        '''
        ans, cnt = 0, Counter(nums)
        high += 1
        while high:
            nxt = Counter()
            for x, c in cnt.items():
                # high%2*cnt[(high-1)^x] 相当于 cnt[(high-1)^x] if high%2 else 0
                ans += c * (high % 2 * cnt[(high - 1) ^ x] - low % 2 * cnt[(low - 1) ^ x])
                nxt[x >> 1] += c
            cnt = nxt
            low >>= 1
            high >>= 1
        return ans // 2
# @lc code=end

