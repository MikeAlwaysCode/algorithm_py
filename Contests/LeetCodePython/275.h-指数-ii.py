#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#
# https://leetcode.cn/problems/h-index-ii/description/
#
# algorithms
# Medium (45.33%)
# Likes:    218
# Dislikes: 0
# Total Accepted:    65K
# Total Submissions: 143.4K
# Testcase Example:  '[0,1,3,5,6]'
#
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照 升序排列
# 。计算并返回该研究者的 h 指数。
# 
# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）总共有 h
# 篇论文分别被引用了至少 h 次。且其余的 n - h 篇论文每篇被引用次数 不超过 h 次。
# 
# 提示：如果 h 有多种可能的值，h 指数 是其中最大的那个。
# 
# 请你设计并实现对数时间复杂度的算法解决此问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：citations = [0,1,3,5,6]
# 输出：3 
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
# 由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3 。
# 
# 示例 2：
# 
# 
# 输入：citations = [1,2,100]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# n == citations.length
# 1 
# 0 
# citations 按 升序排列
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = l + r >> 1
            if n - mid > citations[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return n - l
# @lc code=end

