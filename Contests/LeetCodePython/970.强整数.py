#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] 强整数
#
# https://leetcode.cn/problems/powerful-integers/description/
#
# algorithms
# Medium (41.19%)
# Likes:    70
# Dislikes: 0
# Total Accepted:    16.7K
# Total Submissions: 38.8K
# Testcase Example:  '2\n3\n10'
#
# 给定三个整数 x 、 y 和 bound ，返回 值小于或等于 bound 的所有 强整数 组成的列表 。
# 
# 如果某一整数可以表示为 x^i + y^j ，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个 强整数 。
# 
# 你可以按 任何顺序 返回答案。在你的回答中，每个值 最多 出现一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 2, y = 3, bound = 10
# 输出：[2,3,4,5,7,9,10]
# 解释： 
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
# 
# 示例 2：
# 
# 
# 输入：x = 3, y = 5, bound = 15
# 输出：[2,4,6,8,10,14]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= x, y <= 100
# 0 <= bound <= 10^6
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        a = 1
        while a <= bound:
            b = 1
            while a + b <= bound:
                ans.add(a + b)
                b *= y
                if y == 1:
                    break
            if x == 1:
                break
            a *= x
        return list(ans)
# @lc code=end

