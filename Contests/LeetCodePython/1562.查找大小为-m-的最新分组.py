#
# @lc app=leetcode.cn id=1562 lang=python3
#
# [1562] 查找大小为 M 的最新分组
#
# https://leetcode.cn/problems/find-latest-group-of-size-m/description/
#
# algorithms
# Medium (35.42%)
# Likes:    70
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 17.7K
# Testcase Example:  '[3,5,1,2,4]\n1'
#
# 给你一个数组 arr ，该数组表示一个从 1 到 n 的数字排列。有一个长度为 n 的二进制字符串，该字符串上的所有位最初都设置为 0 。
# 
# 在从 1 到 n 的每个步骤 i 中（假设二进制字符串和 arr 都是从 1 开始索引的情况下），二进制字符串上位于位置 arr[i] 的位将会设为 1
# 。
# 
# 给你一个整数 m ，请你找出二进制字符串上存在长度为 m 的一组 1 的最后步骤。一组 1 是一个连续的、由 1 组成的子串，且左右两边不再有可以延伸的
# 1 。
# 
# 返回存在长度 恰好 为 m 的 一组 1  的最后步骤。如果不存在这样的步骤，请返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [3,5,1,2,4], m = 1
# 输出：4
# 解释：
# 步骤 1："00100"，由 1 构成的组：["1"]
# 步骤 2："00101"，由 1 构成的组：["1", "1"]
# 步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
# 步骤 4："11101"，由 1 构成的组：["111", "1"]
# 步骤 5："11111"，由 1 构成的组：["11111"]
# 存在长度为 1 的一组 1 的最后步骤是步骤 4 。
# 
# 示例 2：
# 
# 输入：arr = [3,1,5,4,2], m = 2
# 输出：-1
# 解释：
# 步骤 1："00100"，由 1 构成的组：["1"]
# 步骤 2："10100"，由 1 构成的组：["1", "1"]
# 步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
# 步骤 4："10111"，由 1 构成的组：["1", "111"]
# 步骤 5："11111"，由 1 构成的组：["11111"]
# 不管是哪一步骤都无法形成长度为 2 的一组 1 。
# 
# 
# 示例 3：
# 
# 输入：arr = [1], m = 1
# 输出：1
# 
# 
# 示例 4：
# 
# 输入：arr = [2,1], m = 2
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# n == arr.length
# 1 <= n <= 10^5
# 1 <= arr[i] <= n
# arr 中的所有整数 互不相同
# 1 <= m <= arr.length
# 
# 
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        fa = list(range(n + 1))
        s = [0] * (n + 1)

        def find(x: int):
            cur = x
            while x != fa[x]:
                x = fa[x]
            if cur != x:
                fa[cur] = x
            return x

        def union(fr: int, to: int):
            fa[find(fr)] = find(to)
        
        mcnt = 0
        ans = -1
        for i in range(n):
            curr = arr[i]
            fr = curr
            s[fr] = 1
            if curr > 0:
                to = find(curr - 1)
                if s[to]:
                    if s[to] == m:
                        mcnt -= 1
                    s[to] += s[fr]
                    union(fr, to)
                    fr = to
            if curr < n:
                to = find(curr + 1)
                if s[to]:
                    if s[to] == m:
                        mcnt -= 1
                    s[to] += s[fr]
                    union(fr, to)
                    fr = to
            if s[fr] == m:
                mcnt += 1
            if mcnt:
                ans = i + 1
        return ans
        ''' 模拟
        link = [0] * (len(arr)+2) # arr从1开始索引 同时头尾相当于哨兵节点 使link在跳转后能够恰当终止
        cnt, res= 0, -1
        
        # 情况2可以视为情况3的特例
        for i in range(len(arr)):
            x = arr[i]
            # 找到储存的左右端点的信息
            l = link[x-1] if link[x-1] else x
            r = link[x+1] if link[x+1] else x
            # 合并段
            if x-l == m: cnt -=1
            if r-x == m: cnt -=1
            if r-l+1 == m: cnt +=1
            # 只要cnt>0就不断更新 那么最终返回的就是 **存在长度恰好为m的一组1的最后步骤**
            if cnt >0: res = i+1
            # 更新端点信息 将l/r替换为link列表中的位置就是题解中的更新式子
            link[l] = r 
            link[r] = l

        return res
        '''
# @lc code=end

