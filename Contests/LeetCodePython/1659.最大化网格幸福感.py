#
# @lc app=leetcode.cn id=1659 lang=python3
#
# [1659] 最大化网格幸福感
#
# https://leetcode.cn/problems/maximize-grid-happiness/description/
#
# algorithms
# Hard (44.23%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 4.8K
# Testcase Example:  '2\n3\n1\n2'
#
# 给你四个整数 m、n、introvertsCount 和 extrovertsCount 。有一个 m x n
# 网格，和两种类型的人：内向的人和外向的人。总共有 introvertsCount 个内向的人和 extrovertsCount 个外向的人。
# 
# 请你决定网格中应当居住多少人，并为每个人分配一个网格单元。 注意，不必 让所有人都生活在网格中。
# 
# 每个人的 幸福感 计算如下：
# 
# 
# 内向的人 开始 时有 120 个幸福感，但每存在一个邻居（内向的或外向的）他都会 失去  30 个幸福感。
# 外向的人 开始 时有 40 个幸福感，每存在一个邻居（内向的或外向的）他都会 得到  20 个幸福感。
# 
# 
# 邻居是指居住在一个人所在单元的上、下、左、右四个直接相邻的单元中的其他人。
# 
# 网格幸福感 是每个人幸福感的 总和 。 返回 最大可能的网格幸福感 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
# 输出：240
# 解释：假设网格坐标 (row, column) 从 1 开始编号。
# 将内向的人放置在单元 (1,1) ，将外向的人放置在单元 (1,3) 和 (2,3) 。
# - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (0 * 30)（0 位邻居）= 120
# - 位于 (1,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
# - 位于 (2,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
# 网格幸福感为：120 + 60 + 60 = 240
# 上图展示该示例对应网格中每个人的幸福感。内向的人在浅绿色单元中，而外向的人在浅紫色单元中。
# 
# 
# 示例 2：
# 
# 
# 输入：m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
# 输出：260
# 解释：将内向的人放置在单元 (1,1) 和 (3,1) ，将外向的人放置在单元 (2,1) 。
# - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
# - 位于 (2,1) 的外向的人的幸福感：40（初始幸福感）+ (2 * 20)（2 位邻居）= 80
# - 位于 (3,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
# 网格幸福感为 90 + 80 + 90 = 260
# 
# 
# 示例 3：
# 
# 
# 输入：m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
# 输出：240
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#
from functools import cache


# @lc code=start
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, nx: int, wx: int) -> int:
        # 如果 x 和 y 相邻，需要加上的分数
        def calc(x: int, y: int) -> int:
            if x == 0 or y == 0:
                return 0
            # 例如两个内向的人，每个人要 -30，一共 -60，下同
            if x == 1 and y == 1:
                return -60
            if x == 2 and y == 2:
                return 40
            return -10
        
        n3 = 3**n
        # 预处理：每一个 mask 的三进制表示
        mask_span = dict()
        # 预处理：每一个 mask 去除最高位、乘 3、加上新的最低位的结果
        truncate = dict()

        # 预处理
        highest = n3 // 3
        for mask in range(n3):
            mask_tmp = mask
            bits = list()
            for i in range(n):
                bits.append(mask_tmp % 3)
                mask_tmp //= 3
            # 与方法一不同的是，这里需要反过来存储，这样 [0] 对应最高位，[n-1] 对应最低位
            mask_span[mask] = bits[::-1]
            truncate[mask] = [
                mask % highest * 3,
                mask % highest * 3 + 1,
                mask % highest * 3 + 2,
            ]
        
        # dfs(位置，轮廓线上的 mask，剩余的内向人数，剩余的外向人数)
        @cache
        def dfs(pos: int, borderline: int, nx: int, wx: int):
            # 边界条件：如果已经处理完，或者没有人了
            if pos == m * n or nx + wx == 0:
                return 0
            
            x, y = divmod(pos, n)
            
            # 什么都不做
            best = dfs(pos + 1, truncate[borderline][0], nx, wx)
            # 放一个内向的人
            if nx > 0:
                best = max(best, 120 + calc(1, mask_span[borderline][0]) \
                                     + (0 if y == 0 else calc(1, mask_span[borderline][n - 1])) \
                                     + dfs(pos + 1, truncate[borderline][1], nx - 1, wx))
            # 放一个外向的人
            if wx > 0:
                best = max(best, 40 + calc(2, mask_span[borderline][0]) \
                                    + (0 if y == 0 else calc(2, mask_span[borderline][n - 1])) \
                                    + dfs(pos + 1, truncate[borderline][2], nx, wx - 1))

            return best
        
        return dfs(0, 0, nx, wx)
# @lc code=end

