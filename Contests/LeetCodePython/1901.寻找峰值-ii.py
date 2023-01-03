#
# @lc app=leetcode.cn id=1901 lang=python3
#
# [1901] 寻找峰值 II
#
# https://leetcode.cn/problems/find-a-peak-element-ii/description/
#
# algorithms
# Medium (58.94%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    6.2K
# Total Submissions: 10.5K
# Testcase Example:  '[[1,4],[3,2]]'
#
# 一个 2D 网格中的 峰值 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。
# 
# 给你一个 从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。找出 任意一个 峰值 mat[i][j] 并 返回其位置
# [i,j] 。
# 
# 你可以假设整个矩阵周边环绕着一圈值为 -1 的格子。
# 
# 要求必须写出时间复杂度为 O(m log(n)) 或 O(n log(m)) 的算法
# 
# 
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: mat = [[1,4],[3,2]]
# 输出: [0,1]
# 解释: 3 和 4 都是峰值，所以[1,0]和[0,1]都是可接受的答案。
# 
# 
# 示例 2:
# 
# 
# 
# 
# 输入: mat = [[10,20,15],[21,30,14],[7,16,32]]
# 输出: [1,1]
# 解释: 30 和 32 都是峰值，所以[1,1]和[2,2]都是可接受的答案。
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 500
# 1 <= mat[i][j] <= 10^5
# 任意两个相邻元素均不相等.
# 
# 
#

# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])

        # 找到单列中最大值和其索引
        def getColMax(i: int) -> tuple[int, int]:
            value, index = mat[0][i], 0
            for row in range(1, m):
                if mat[row][i] > value:
                    value, index = mat[row][i], row
            return value, index

        # 二分法切片
        left, right = 0, n - 1
        while left < right:
            mid = left + right >> 1
            max_val, max_idx = getColMax(mid)
            if mid == 0: # left = 0, right = 1
                if max_val > mat[max_idx][1]:
                    return [max_idx, 0]
                else:
                    left = 1
            else:
                if mat[max_idx][mid-1] < max_val and mat[max_idx][mid+1] < max_val:
                    return [max_idx, mid]
                elif mat[max_idx][mid-1] < max_val < mat[max_idx][mid+1]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # 对于最后剩下的一列，其最大值一定是极大值
        _, idx = getColMax(left)
        return [idx, left]
# @lc code=end

