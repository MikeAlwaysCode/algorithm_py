#
# @lc app=leetcode.cn id=2561 lang=python3
#
# [2561] 重排水果
#
# https://leetcode.cn/problems/rearranging-fruits/description/
#
# algorithms
# Hard (36.52%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 7.3K
# Testcase Example:  '[4,2,2,2]\n[1,4,1,2]'
#
# 你有两个果篮，每个果篮中有 n 个水果。给你两个下标从 0 开始的整数数组 basket1 和 basket2 ，用以表示两个果篮中每个水果的成本。
# 
# 你希望两个果篮相等。为此，可以根据需要多次执行下述操作：
# 
# 
# 选中两个下标 i 和 j ，并交换 basket1 中的第 i 个水果和 basket2 中的第 j 个水果。
# 交换的成本是 min(basket1i,basket2j) 。
# 
# 
# 根据果篮中水果的成本进行排序，如果排序后结果完全相同，则认为两个果篮相等。
# 
# 返回使两个果篮相等的最小交换成本，如果无法使两个果篮相等，则返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：basket1 = [4,2,2,2], basket2 = [1,4,1,2]
# 输出：1
# 解释：交换 basket1 中下标为 1 的水果和 basket2 中下标为 0 的水果，交换的成本为 1 。此时，basket1 = [4,1,2,2]
# 且 basket2 = [2,4,1,2] 。重排两个数组，发现二者相等。
# 
# 
# 示例 2：
# 
# 
# 输入：basket1 = [2,3,4,1], basket2 = [3,2,5,1]
# 输出：-1
# 解释：可以证明无法使两个果篮相等。
# 
# 
# 
# 
# 提示：
# 
# 
# basket1.length == bakste2.length
# 1 <= basket1.length <= 10^5
# 1 <= basket1i,basket2i <= 10^9
# 
# 
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter()
        for x, y in zip(basket1, basket2):
            cnt[x] += 1
            cnt[y] -= 1
        mn = min(cnt)
        a = []
        for x, c in cnt.items():
            if c % 2: return -1
            a.extend([x] * (abs(c) // 2))
        a.sort()  # 也可以用快速选择
        return sum(min(x, mn * 2) for x in a[:len(a) // 2])
        '''
        basket1.sort()
        basket2.sort()
        n = len(basket1)
        ans = i = j = 0
        mn = min(basket1[0], basket2[0])
        cost = []
        while i < n and j < n:
            if basket1[i] < basket2[j]:
                if i < n - 1 and basket1[i] == basket1[i + 1]:
                    cost.append(basket1[i])
                    i += 2
                else:
                    return -1
            elif basket1[i] > basket2[j]:
                if j < n - 1 and basket2[j] == basket2[j + 1]:
                    cost.append(basket2[j])
                    j += 2
                else:
                    return -1
            else:
                i += 1
                j += 1
        while i < n:
            if i < n - 1 and basket1[i] == basket1[i + 1]:
                cost.append(basket1[i])
                i += 2
            else:
                return -1
        while j < n:
            if j < n - 1 and basket2[j] == basket2[j + 1]:
                cost.append(basket2[j])
                j += 2
            else:
                return -1
        # print(cost)
        m = len(cost)
        for i in range(m//2):
            ans += min(mn * 2, cost[i])
        return ans
        '''
# @lc code=end

