#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#
# https://leetcode.cn/problems/check-if-it-is-a-straight-line/description/
#
# algorithms
# Easy (45.89%)
# Likes:    126
# Dislikes: 0
# Total Accepted:    44.5K
# Total Submissions: 97K
# Testcase Example:  '[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]'
#
# 给定一个数组 coordinates ，其中 coordinates[i] = [x, y] ， [x, y] 表示横坐标为 x、纵坐标为 y
# 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates 中不含重复的点
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        coordinates.sort()
        x01, y01 = coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]
        for i in range(2, n):
            if (coordinates[i][1] - coordinates[0][1]) * x01 != (coordinates[i][0] - coordinates[0][0]) * y01:
                return False
        return True
# @lc code=end

