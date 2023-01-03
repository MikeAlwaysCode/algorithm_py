#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode.cn/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (38.50%)
# Likes:    454
# Dislikes: 0
# Total Accepted:    72.6K
# Total Submissions: 188.4K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# points[i].length == 2
# -10^4 i, yi 
# points 中的所有点 互不相同
# 
# 
#
import math
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        ans = 0
        for i in range(n):
            if ans >= n - i or ans > n // 2:
                break
            
            d = defaultdict(int)
            for j in range(i+1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]

                if x == 0:
                    y = 1
                elif y == 0:
                    x = 1
                else:
                    if y < 0:
                        x, y = -x, -y
                    g = math.gcd(abs(x), abs(y))
                    x //= g
                    y //= g
                key = x + y * 20001
                d[key] += 1
                ans = max(ans, d[key] + 1)
        
        return ans
# @lc code=end

