#
# @lc app=leetcode.cn id=1054 lang=python3
#
# [1054] 距离相等的条形码
#
# https://leetcode.cn/problems/distant-barcodes/description/
#
# algorithms
# Medium (39.91%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    13.8K
# Total Submissions: 33.4K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
# 
# 请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：barcodes = [1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
# 
# 
# 示例 2：
# 
# 
# 输入：barcodes = [1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1]
# 
# 
# 
# 提示：
# 
# 
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
# 
# 
#
from typing import Counter, List


# @lc code=start
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        n, i, j = len(barcodes), 0, 1
        ans = [0] * n
        for k, v in cnt.items():
            while v and v <= n // 2 and j < n:
                ans[j] = k
                v -= 1
                j += 2
            while v:
                ans[i] = k
                v -= 1
                i += 2
        return ans
# @lc code=end

