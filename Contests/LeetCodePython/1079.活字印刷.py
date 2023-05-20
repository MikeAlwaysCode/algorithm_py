#
# @lc app=leetcode.cn id=1079 lang=python3
#
# [1079] 活字印刷
#
# https://leetcode.cn/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (73.87%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    19.2K
# Total Submissions: 25.6K
# Testcase Example:  '"AAB"'
#
# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
# 
# 注意：本题中，每个活字字模只能使用一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
# 
# 
# 示例 2：
# 
# 
# 输入："AAABBC"
# 输出：188
# 
# 
# 示例 3：
# 
# 
# 输入："V"
# 输出：1
# 
# 
# 
# 提示：
# 
# 
# 1 <= tiles.length <= 7
# tiles 由大写英文字母组成
# 
# 
#
from collections import Counter
from math import comb


# @lc code=start
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        f = [1] + [0] * len(tiles)
        n = 0
        for cnt in Counter(tiles).values():  # 枚举第 i 种字母
            n += cnt  # 常数优化：相比从 len(tiles) 开始要更快
            for j in range(n, 0, -1):  # 枚举序列长度 j
                # 枚举第 i 种字母选了 k 个，注意 k=0 时的方案数已经在 f[j] 中了
                for k in range(1, min(j, cnt) + 1):
                    f[j] += f[j - k] * comb(j, k)  # comb 也可以预处理，见其它语言的实现
        return sum(f[1:])
        '''
        counts = Counter(tiles).values()  # 统计每个字母的出现次数
        n, m = len(tiles), len(counts)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 1  # 构造空序列的方案数
        for i, cnt in enumerate(counts, 1):  # 枚举第 i 种字母
            for j in range(n + 1):  # 枚举序列长度 j
                for k in range(min(j, cnt) + 1):  # 枚举第 i 种字母选了 k 个
                    f[i][j] += f[i - 1][j - k] * comb(j, k)  # comb 也可以预处理，见其它语言
        return sum(f[m][1:])
        '''
# @lc code=end

