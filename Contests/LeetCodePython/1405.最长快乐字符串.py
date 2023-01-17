#
# @lc app=leetcode.cn id=1405 lang=python3
#
# [1405] 最长快乐字符串
#
# https://leetcode.cn/problems/longest-happy-string/description/
#
# algorithms
# Medium (63.54%)
# Likes:    211
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 45.7K
# Testcase Example:  '1\n1\n7'
#
# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
# 
# 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
# 
# 
# s 是一个尽可能长的快乐字符串。
# s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
# s 中只含有 'a'、'b' 、'c' 三种字母。
# 
# 
# 如果不存在这样的字符串 s ，请返回一个空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。
# 
# 
# 示例 2：
# 
# 输入：a = 2, b = 2, c = 1
# 输出："aabbc"
# 
# 
# 示例 3：
# 
# 输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。
# 
# 
# 
# 提示：
# 
# 
# 0 <= a, b, c <= 100
# a + b + c > 0
# 
# 
#
from heapq import heapify, heappop, heappush, heapreplace


# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapify(h)  # 建堆
        ans = []
        while h:
            d1, c1 = heappop(h)

            # 如果前两个字符都和当前堆顶相同，则尝试换一个字符
            if len(ans) > 1 and c1 == ans[-1][0] and c1 == ans[-2][0]:
                if not h: break # 堆中没有可以替换的字符，直接退出
                d1, c1 = heapreplace(h, (d1, c1))

            if d1 == 0:
                break
                
            ans.append(c1)
            d1 += 1
            if d1 != 0:
                heappush(h, (d1, c1))
            
        return "".join(ans)
# @lc code=end

