#
# @lc app=leetcode.cn id=2709 lang=python3
#
# [2709] 最大公约数遍历
#
# https://leetcode.cn/problems/greatest-common-divisor-traversal/description/
#
# algorithms
# Hard (23.54%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    2.4K
# Total Submissions: 10K
# Testcase Example:  '[2,3,6]'
#
# 给你一个下标从 0 开始的整数数组 nums ，你可以在一些下标之间遍历。对于两个下标 i 和 j（i != j），当且仅当 gcd(nums[i],
# nums[j]) > 1 时，我们可以在两个下标之间通行，其中 gcd 是两个数的 最大公约数 。
# 
# 你需要判断 nums 数组中 任意 两个满足 i < j 的下标 i 和 j ，是否存在若干次通行可以从 i 遍历到 j 。
# 
# 如果任意满足条件的下标对都可以遍历，那么返回 true ，否则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,3,6]
# 输出：true
# 解释：这个例子中，总共有 3 个下标对：(0, 1) ，(0, 2) 和 (1, 2) 。
# 从下标 0 到下标 1 ，我们可以遍历 0 -> 2 -> 1 ，我们可以从下标 0 到 2 是因为 gcd(nums[0], nums[2]) =
# gcd(2, 6) = 2 > 1 ，从下标 2 到 1 是因为 gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1 。
# 从下标 0 到下标 2 ，我们可以直接遍历，因为 gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1
# 。同理，我们也可以从下标 1 到 2 因为 gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,9,5]
# 输出：false
# 解释：我们没法从下标 0 到 2 ，所以返回 false 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [4,3,12,8]
# 输出：true
# 解释：总共有 6 个下标对：(0, 1) ，(0, 2) ，(0, 3) ，(1, 2) ，(1, 3) 和 (2, 3)
# 。所有下标对之间都存在可行的遍历，所以返回 true 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 
# 
#
from typing import List


# @lc code=start
C = 10 ** 5
isprime = [True] * (C + 1)
primes = list()
for i in range(2, C + 1):
    if isprime[i]:
        primes.append(i)
    for prime in primes:
        if i * prime > C:
            break
        isprime[i * prime] = False
        if i % prime == 0:
            break
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set(nums)
        if 1 in s and n > 1: return False
        nums = list(s)
        n = len(nums)
        if n == 1: return True
        fa = list(range(n))
        setCount = n
        def find(x: int):
            cur = x
            while x != fa[x]:
                x = fa[x]
            while fa[cur] != x:
                tmp = fa[cur]
                fa[cur] = x
                cur = tmp
            return x
        pd = dict()
        def union(d: int, i: int):
            if d not in pd:
                pd[d] = i
            else:
                fd = find(pd[d])
                fi = find(i)
                if fd != fi:
                    fa[fi] = fd
                    nonlocal setCount
                    setCount -= 1

        for i, x in enumerate(nums):
            for p in primes:
                if p * p > x: break
                if x % p == 0:
                    union(p, i)
                    while x % p == 0:
                        x //= p
            if x > 1: union(x, i)

        return setCount == 1
# @lc code=end

