#
# @lc app=leetcode.cn id=1240 lang=python3
#
# [1240] 铺瓷砖
#
# https://leetcode.cn/problems/tiling-a-rectangle-with-the-fewest-squares/description/
#
# algorithms
# Hard (52.25%)
# Likes:    122
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 9.3K
# Testcase Example:  '2\n3'
#
# 你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。
# 
# 房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。
# 
# 假设正方形瓷砖的规格不限，边长都是整数。
# 
# 请你帮设计师计算一下，最少需要用到多少块方形瓷砖？
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：n = 2, m = 3
# 输出：3
# 解释：3 块地砖就可以铺满卧室。
# ⁠    2 块 1x1 地砖
# ⁠    1 块 2x2 地砖
# 
# 示例 2：
# 
# 
# 
# 输入：n = 5, m = 8
# 输出：5
# 
# 
# 示例 3：
# 
# 
# 
# 输入：n = 11, m = 13
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 13
# 1 <= m <= 13
# 
# 
#

# @lc code=start
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
# @lc code=end

