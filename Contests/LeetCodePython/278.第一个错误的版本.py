#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#
# https://leetcode.cn/problems/first-bad-version/description/
#
# algorithms
# Easy (45.62%)
# Likes:    783
# Dislikes: 0
# Total Accepted:    384.6K
# Total Submissions: 842.8K
# Testcase Example:  '5\n4'
#
# 
# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
# 
# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
# 
# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version
# 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
# 
# 
# 示例 1：
# 
# 
# 输入：n = 5, bad = 4
# 输出：4
# 解释：
# 调用 isBadVersion(3) -> false 
# 调用 isBadVersion(5) -> true 
# 调用 isBadVersion(4) -> true
# 所以，4 是第一个错误的版本。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1, bad = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#
def isBadVersion(version: int) -> bool:
    return True
# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 对首个单元出现故障的情况进行判断，目的是方便下面的代码编写
        if isBadVersion(1):
            return 1

        # 初始上下界以及中间值mid赋值
        left = 1
        right = n
        mid = int((left + right)/2)

        # while循环，根据mid单元是否出现故障确定每次循环后的上下界，right - left == 2时循环结束
        while right - left > 2:
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
            mid = int((left + right)/2)

        # 循环结束后对结果进行分析，这里left、mid、right是否出现故障对应的布尔值只可能出现011和001两种情况
        if isBadVersion(mid):
            return mid
        else:
            return right
# @lc code=end

