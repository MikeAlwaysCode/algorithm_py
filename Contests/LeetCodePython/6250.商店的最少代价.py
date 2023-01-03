#
# @lc app=leetcode.cn id=6250 lang=python3
#
# [6250] 商店的最少代价
#
# https://leetcode.cn/problems/minimum-penalty-for-a-shop/description/
#
# algorithms
# Medium (62.45%)
# Likes:    2
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 4.4K
# Testcase Example:  '"YYNY"'
#
# 给你一个顾客访问商店的日志，用一个下标从 0 开始且只包含字符 'N' 和 'Y' 的字符串 customers 表示：
# 
# 
# 如果第 i 个字符是 'Y' ，它表示第 i 小时有顾客到达。
# 如果第 i 个字符是 'N' ，它表示第 i 小时没有顾客到达。
# 
# 
# 如果商店在第 j 小时关门（0 <= j <= n），代价按如下方式计算：
# 
# 
# 在开门期间，如果某一个小时没有顾客到达，代价增加 1 。
# 在关门期间，如果某一个小时有顾客到达，代价增加 1 。
# 
# 
# 请你返回在确保代价 最小 的前提下，商店的 最早 关门时间。
# 
# 注意，商店在第 j 小时关门表示在第 j 小时以及之后商店处于关门状态。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：customers = "YYNY"
# 输出：2
# 解释：
# - 第 0 小时关门，总共 1+1+0+1 = 3 代价。
# - 第 1 小时关门，总共 0+1+0+1 = 2 代价。
# - 第 2 小时关门，总共 0+0+0+1 = 1 代价。
# - 第 3 小时关门，总共 0+0+1+1 = 2 代价。
# - 第 4 小时关门，总共 0+0+1+0 = 1 代价。
# 在第 2 或第 4 小时关门代价都最小。由于第 2 小时更早，所以最优关门时间是 2 。
# 
# 
# 示例 2：
# 
# 
# 输入：customers = "NNNNN"
# 输出：0
# 解释：最优关门时间是 0 ，因为自始至终没有顾客到达。
# 
# 示例 3：
# 
# 
# 输入：customers = "YYYY"
# 输出：4
# 解释：最优关门时间是 4 ，因为每一小时均有顾客到达。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= customers.length <= 10^5
# customers 只包含字符 'Y' 和 'N' 。
# 
# 
#

# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = 0
        mn = cost = customers.count('Y')
        for i, c in enumerate(customers, 1):
            if c == 'Y':
                cost -= 1
                if cost < mn:
                    mn = cost
                    ans = i
            else:
                cost += 1
        return ans
# @lc code=end

