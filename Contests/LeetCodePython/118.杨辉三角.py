#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode.cn/problems/pascals-triangle/description/
#
# algorithms
# Easy (75.40%)
# Likes:    856
# Dislikes: 0
# Total Accepted:    354K
# Total Submissions: 469.6K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 
# 
# 示例 2:
# 
# 
# 输入: numRows = 1
# 输出: [[1]]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j-1] + ans[i-1][j])
        return ans
# @lc code=end

