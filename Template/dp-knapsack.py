'''
https://leetcode.cn/problems/last-stone-weight-ii/solution/yi-pian-wen-zhang-chi-tou-bei-bao-wen-ti-5lfv/
https://leetcode.cn/circle/discuss/GWpXCM/
https://en.wikipedia.org/wiki/Knapsack_problem

01背包
    每个元素最多选取一次, 外循环nums, 内循环target, target倒序且target>=nums[i];

完全背包
    每个元素可以重复选择, 外循环nums, 内循环target, target正序且target>=nums[i];

多重背包
    在 0-1 背包问题的基础上，在容量允许的情况下，增加了每件物品可以选择多次的特点（但又不是无限次，是有限制的多次）。;

分组背包
    不止一个背包，需要遍历每个背包, 外循环背包bags, 内部两层循环根据题目的要求转化为1,2,3三种背包类型的模板;

树上背包
    有依赖的背包问题 ：有 N 个物品和一个容量是 V 的背包。物品之间具有依赖关系，且依赖关系组成一棵树的形状。如果选择一个物品，则必须选择它的父节点。
'''
from typing import List


# 01背包
class Solution:
    # LC416 https://leetcode.cn/problems/partition-equal-subset-sum/
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target & 1:
            return False
        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True
        for x in nums:
            for j in range(target, x - 1, -1):
                dp[j] |= dp[j - x]
        return dp[target]
    
    # LC474 https://leetcode.cn/problems/ones-and-zeroes/
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            cnt0 = s.count("0")
            cnt1 = len(s) - cnt0
            for i in range(m, cnt0-1, -1):
                for j in range(n, cnt1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-cnt0][j-cnt1] + 1)
        return dp[m][n]