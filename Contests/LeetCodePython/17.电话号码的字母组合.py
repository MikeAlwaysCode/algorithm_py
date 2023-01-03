#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (57.83%)
# Likes:    2183
# Dislikes: 0
# Total Accepted:    596.6K
# Total Submissions: 1M
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# 示例 2：
# 
# 
# 输入：digits = ""
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：digits = "2"
# 输出：["a","b","c"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtracking(i: int) -> None:
            if i == len(digits):
                combinations.append("".join(combination))
            else:
                for x in phoneMap[digits[i]]:
                    combination.append(x)
                    backtracking(i+1)
                    combination.pop()
        
        combination = list()
        combinations = list()
        backtracking(0)
        return combinations
# @lc code=end

