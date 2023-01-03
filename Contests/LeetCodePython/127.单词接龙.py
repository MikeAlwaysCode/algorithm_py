#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode.cn/problems/word-ladder/description/
#
# algorithms
# Hard (48.08%)
# Likes:    1169
# Dislikes: 0
# Total Accepted:    172.3K
# Total Submissions: 358.3K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 ->
# s2 -> ... -> sk：
# 
# 
# 每一对相邻的单词只差一个字母。
# 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
# 
# 
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列
# 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
# 
# 
# 示例 1：
# 
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
# 
# 
# 示例 2：
# 
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。
# 
# 
# 
# 提示：
# 
# 
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同
# 
# 
#
from collections import deque
from string import ascii_lowercase
from typing import List
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
            
        def bfs() -> int:
            q1 = deque([beginWord])
            q2 = deque([endWord])
            d1 = {beginWord:1}
            d2 = {endWord:0}

            while q1 and q2:
                res = -1
                if len(q1) <= len(q2):
                    res = update(q1, d1, d2)
                else:
                    res = update(q2, d2, d1)
                if res != -1:
                    return res
            return 0
        
        def update(q: deque[str], d1: dict, d2: dict) -> int:
            # 将q完整扩展一次
            m = len(q)
            while m > 0:
                m -= 1
                curr = q.popleft()
                step = d1[curr]
                for i, c in enumerate(curr):
                    for tc in ascii_lowercase:
                        if tc == c:
                            continue
                        nxt = curr[:i] + tc + curr[i + 1:]
                        if nxt not in wordList or nxt in d1:
                            continue
                        if nxt in d2:
                            return step + 1 + d2[nxt]
                        d1[nxt] = step + 1
                        q.append(nxt)
            return -1
            
        return bfs()
# @lc code=end

