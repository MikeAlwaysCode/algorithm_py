#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
# https://leetcode.cn/problems/open-the-lock/description/
#
# algorithms
# Medium (52.76%)
# Likes:    570
# Dislikes: 0
# Total Accepted:    108.8K
# Total Submissions: 206.1K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
# 
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
# 
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
# 
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
# 
# 
# 示例 2:
# 
# 
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
# 
# 
# 示例 3:
# 
# 
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：无法旋转到目标数字且不被锁定。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target 不在 deadends 之中
# target 和 deadends[i] 仅由若干位数字组成
# 
# 
#
from collections import deque
from string import digits
from turtle import update
from typing import List
# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        if target == start:
            return 0
        deadends = set(deadends)
        if start in deadends:
            return -1
            
        def bfs() -> int:
            q1 = deque([start])    # From 0000
            q2 = deque([target])    # From target
            d1 = {start:0}
            d2 = {target:0}

            while q1 and q2:
                res = -1
                if len(q1) <= len(q2):
                    res = update(q1, d1, d2)
                else:
                    res = update(q2, d2, d1)
                if res != -1:
                    return res
            return -1
        
        def update(q: deque[str], d1: dict, d2: dict) -> int:
            # 将q完整扩展一次
            m = len(q)
            while m > 0:
                m -= 1
                curr = q.popleft()
                step = d1[curr]
                for i, c in enumerate(curr):
                    for d in [str((int(c) + 1)%10), str((int(c) - 1)%10)]:
                        nxt = curr[:i] + d + curr[i + 1:]
                        if nxt in deadends or nxt in d1:
                            continue
                        if nxt in d2:
                            return step + 1 + d2[nxt]
                        d1[nxt] = step + 1
                        q.append(nxt)
            return -1
            
        return bfs()
        
        '''
        q = deque([("0000", 0)])
        while q:
            curr, step = q.popleft()
            for i, c in enumerate(curr):
                # for d in digits:
                for d in [str((int(c) + 1)%10), str((int(c) - 1)%10)]:
                    nxt = curr[:i] + d + curr[i + 1:]
                    if nxt in deadends:
                        continue
                    if nxt == target:
                        return step + 1
                    deadends.add(nxt)
                    q.append((nxt, step + 1))
        return -1
        '''
# @lc code=end

