#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#
# https://leetcode.cn/problems/interval-list-intersections/description/
#
# algorithms
# Medium (68.49%)
# Likes:    336
# Dislikes: 0
# Total Accepted:    54.8K
# Total Submissions: 80.1K
# Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而
# secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。
# 
# 返回这 两个区间列表的交集 。
# 
# 形式上，闭区间 [a, b]（其中 a ）表示实数 x 的集合，而 a  。
# 
# 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =
# [[1,5],[8,12],[15,24],[25,26]]
# 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# 
# 
# 示例 2：
# 
# 
# 输入：firstList = [[1,3],[5,9]], secondList = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：firstList = [], secondList = [[4,8],[10,12]]
# 输出：[]
# 
# 
# 示例 4：
# 
# 
# 输入：firstList = [[1,7]], secondList = [[3,10]]
# 输出：[[3,7]]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# firstList.length + secondList.length >= 1
# 0 i < endi 
# endi < starti+1
# 0 j < endj 
# endj < startj+1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        n, m = len(firstList), len(secondList)
        ans = []
        i = j = 0
        while i < n and j < m:
            l = max(firstList[i][0], secondList[j][0])
            r = min(firstList[i][1], secondList[j][1])
            if l <= r:
                ans.append([l, r])
            if firstList[i][1] > secondList[j][1]:
                j += 1
            elif firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                i += 1
                j += 1
        return ans
# @lc code=end

