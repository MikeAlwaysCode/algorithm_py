#
# @lc app=leetcode.cn id=2612 lang=python3
#
# [2612] 最少翻转操作数
#
# https://leetcode.cn/problems/minimum-reverse-operations/description/
#
# algorithms
# Hard (20.20%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 11.2K
# Testcase Example:  '4\n0\n[1,2]\n4'
#
# 给你一个整数 n 和一个在范围 [0, n - 1] 以内的整数 p ，它们表示一个长度为 n 且下标从 0 开始的数组 arr ，数组中除了下标为 p
# 处是 1 以外，其他所有数都是 0 。
# 
# 同时给你一个整数数组 banned ，它包含数组中的一些位置。banned 中第 i 个位置表示 arr[banned[i]] = 0 ，题目保证
# banned[i] != p 。
# 
# 你可以对 arr 进行 若干次 操作。一次操作中，你选择大小为 k 的一个 子数组 ，并将它 翻转 。在任何一次翻转操作后，你都需要确保 arr 中唯一的
# 1 不会到达任何 banned 中的位置。换句话说，arr[banned[i]] 始终 保持 0 。
# 
# 请你返回一个数组 ans ，对于 [0, n - 1] 之间的任意下标 i ，ans[i] 是将 1 放到位置 i 处的 最少
# 翻转操作次数，如果无法放到位置 i 处，此数为 -1 。
# 
# 
# 子数组 指的是一个数组里一段连续 非空 的元素序列。
# 对于所有的 i ，ans[i] 相互之间独立计算。
# 将一个数组中的元素 翻转 指的是将数组中的值变成 相反顺序 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4, p = 0, banned = [1,2], k = 4
# 输出：[0,-1,-1,1]
# 解释：k = 4，所以只有一种可行的翻转操作，就是将整个数组翻转。一开始 1 在位置 0 处，所以将它翻转到位置 0 处需要的操作数为 0 。
# 我们不能将 1 翻转到 banned 中的位置，所以位置 1 和 2 处的答案都是 -1 。
# 通过一次翻转操作，可以将 1 放到位置 3 处，所以位置 3 的答案是 1 。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 5, p = 0, banned = [2,4], k = 3
# 输出：[0,-1,-1,-1,-1]
# 解释：这个例子中 1 一开始在位置 0 处，所以此下标的答案为 0 。
# 翻转的子数组长度为 k = 3 ，1 此时在位置 0 处，所以我们可以翻转子数组 [0, 2]，但翻转后的下标 2 在 banned
# 中，所以不能执行此操作。
# 由于 1 没法离开位置 0 ，所以其他位置的答案都是 -1 。
# 
# 
# 示例 3：
# 
# 
# 输入：n = 4, p = 2, banned = [0,1,3], k = 1
# 输出：[-1,-1,0,-1]
# 解释：这个例子中，我们只能对长度为 1 的子数组执行翻转操作，所以 1 无法离开初始位置。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^5
# 0 <= p <= n - 1
# 0 <= banned.length <= n - 1
# 0 <= banned[i] <= n - 1
# 1 <= k <= n 
# banned[i] != p
# banned 中的值 互不相同 。
# 
# 
#
from bisect import bisect_left
from typing import List


# @lc code=start
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        s = set(banned) | {p}
        not_banned = [[], []]
        for i in range(n):
            if i not in s:
                not_banned[i % 2].append(i)
        not_banned[0].append(n)
        not_banned[1].append(n)  # 哨兵

        fa = [list(range(len(not_banned[0]))), list(range(len(not_banned[1])))]

        def find(i: int, x: int) -> int:
            f = fa[i]
            if f[x] != x:
                f[x] = find(i, f[x])
            return f[x]

        def merge(i: int, from_: int, to: int) -> None:
            x, y = find(i, from_), find(i, to)
            fa[i][x] = y

        ans = [-1] * n
        q = [p]
        step = 0
        while q:
            tmp = q
            q = []
            for i in tmp:
                ans[i] = step
                # 从 mn 到 mx 的所有位置都可以翻转到
                mn = max(i - k + 1, k - i - 1)
                mx = min(i + k - 1, n * 2 - k - i - 1)
                a = not_banned[mn % 2]
                j = find(mn % 2, bisect_left(a, mn))
                while a[j] <= mx:
                    q.append(a[j])
                    merge(mn % 2, j, j + 1)  # 删除 j
                    j = find(mn % 2, j + 1)
            step += 1
        return ans
# @lc code=end

