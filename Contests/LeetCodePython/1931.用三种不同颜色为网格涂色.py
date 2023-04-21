#
# @lc app=leetcode.cn id=1931 lang=python3
#
# [1931] 用三种不同颜色为网格涂色
#
# https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/description/
#
# algorithms
# Hard (58.91%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 5.2K
# Testcase Example:  '1\n1'
#
# 给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝
# 三种颜色为每个单元格涂色。所有单元格都需要被涂色。
# 
# 涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 10^9 + 7 取余 的结果。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：m = 1, n = 1
# 输出：3
# 解释：如上图所示，存在三种可能的涂色方案。
# 
# 
# 示例 2：
# 
# 
# 输入：m = 1, n = 2
# 输出：6
# 解释：如上图所示，存在六种可能的涂色方案。
# 
# 
# 示例 3：
# 
# 
# 输入：m = 5, n = 5
# 输出：580986
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        # 哈希映射 valid 存储所有满足要求的对一行进行涂色的方案
        # 键表示 mask，值表示 mask 的三进制串（以列表的形式存储）
        valid = dict()
        
        # 在 [0, 3^m) 范围内枚举满足要求的 mask
        for mask in range(3**m):
            color = list()
            mm = mask
            for i in range(m):
                color.append(mm % 3)
                mm //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color
        
        # 预处理所有的 (mask1, mask2) 二元组，满足 mask1 和 mask2 作为相邻行时，同一列上两个格子的颜色不同
        adjacent = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adjacent[mask1].append(mask2)
        
        f = [int(mask in valid) for mask in range(3**m)]
        for i in range(1, n):
            g = [0] * (3**m)
            for mask2 in valid.keys():
                for mask1 in adjacent[mask2]:
                    g[mask2] += f[mask1]
                    if g[mask2] >= mod:
                        g[mask2] -= mod
            f = g
            
        return sum(f) % mod
# @lc code=end

