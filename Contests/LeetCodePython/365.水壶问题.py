#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#
# https://leetcode.cn/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (39.18%)
# Likes:    402
# Dislikes: 0
# Total Accepted:    44.7K
# Total Submissions: 114K
# Testcase Example:  '3\n5\n4'
#
# 有两个水壶，容量分别为 jug1Capacity 和 jug2Capacity 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到
# targetCapacity 升。
# 
# 如果可以得到 targetCapacity 升水，最后请用以上水壶中的一或两个来盛放取得的 targetCapacity 升水。
# 
# 你可以：
# 
# 
# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空
# 
# 
# 
# 
# 示例 1: 
# 
# 
# 输入: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
# 输出: true
# 解释：来自著名的 "Die Hard"
# 
# 示例 2:
# 
# 
# 输入: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
# 输出: false
# 
# 
# 示例 3:
# 
# 
# 输入: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
# 输出: true
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
# 
# 
#
import math
# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
        '''
        stack = [(0, 0)]
        self.seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in self.seen:
                continue
            self.seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False
        '''
# @lc code=end

