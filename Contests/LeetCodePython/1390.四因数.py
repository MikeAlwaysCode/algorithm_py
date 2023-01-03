#
# @lc app=leetcode.cn id=1390 lang=python3
#
# [1390] 四因数
#
# https://leetcode.cn/problems/four-divisors/description/
#
# algorithms
# Medium (37.63%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 21.7K
# Testcase Example:  '[21,4,7]'
#
# 给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。如果数组中不存在满足题意的整数，则返回 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [21,4,7]
# 输出：32
# 解释：
# 21 有 4 个因数：1, 3, 7, 21
# 4 有 3 个因数：1, 2, 4
# 7 有 2 个因数：1, 7
# 答案仅为 21 的所有因数的和。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [21,21]
# 输出: 64
# 
# 
# 示例 3:
# 
# 
# 输入: nums = [1,2,3,4,5]
# 输出: 0
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^5
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # C 是数组 nums 元素的上限，C3 是 C 的立方根
        C, C3 = 100000, 46

        isprime = [True] * (C + 1)
        primes = list()

        # 埃拉托斯特尼筛法
        for i in range(2, C + 1):
            if isprime[i]:
                primes.append(i)
            for j in range(i + i, C + 1, i):
                isprime[j] = False
        
        # 欧拉筛法
        """
        for i in range(2, C + 1):
            if isprime[i]:
                primes.append(i)
            for prime in primes:
                if i * prime > C:
                    break
                isprime[i * prime] = False
                if i % prime == 0:
                    break
        """
        
        # 通过质数表构造出所有的四因数
        factor4 = dict()
        for prime in primes:
            if prime <= C3:
                factor4[prime**3] = 1 + prime + prime**2 + prime**3
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                if primes[i] * primes[j] <= C:
                    factor4[primes[i] * primes[j]] = 1 + primes[i] + primes[j] + primes[i] * primes[j]
                else:
                    break
        
        ans = 0
        for num in nums:
            if num in factor4:
                ans += factor4[num]
        return ans
# @lc code=end

