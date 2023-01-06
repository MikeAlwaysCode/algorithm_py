#
# @lc app=leetcode.cn id=2180 lang=python3
#
# [2180] 统计各位数字之和为偶数的整数个数
#
# https://leetcode.cn/problems/count-integers-with-even-digit-sum/description/
#
# algorithms
# Easy (64.62%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    14K
# Total Submissions: 20.9K
# Testcase Example:  '4'
#
# 给你一个正整数 num ，请你统计并返回 小于或等于 num 且各位数字之和为 偶数 的正整数的数目。
# 
# 正整数的 各位数字之和 是其所有位上的对应数字相加的结果。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = 4
# 输出：2
# 解释：
# 只有 2 和 4 满足小于等于 4 且各位数字之和为偶数。    
# 
# 
# 示例 2：
# 
# 
# 输入：num = 30
# 输出：14
# 解释：
# 只有 14 个整数满足小于等于 30 且各位数字之和为偶数，分别是： 
# 2、4、6、8、11、13、15、17、19、20、22、24、26 和 28 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        y, x = divmod(num, 10)
        ans = y * 5
        sm = 0
        while y:
            sm += y % 10
            y //= 10
        ans += (x + 1) // 2 - 1 if sm & 1 else x // 2
        '''
        ans = 0
        for x in range(1, num + 1):
            sm = 0
            while x:
                sm += x % 10
                x //= 10
            ans += sm & 1 ^ 1
        '''
        return ans
# @lc code=end

