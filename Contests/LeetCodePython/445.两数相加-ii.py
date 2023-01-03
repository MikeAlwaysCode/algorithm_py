#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode.cn/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (60.14%)
# Likes:    570
# Dislikes: 0
# Total Accepted:    115.3K
# Total Submissions: 191.7K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 
# 
# 示例1：
# 
# 
# 
# 
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
# 
# 
# 示例2：
# 
# 
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
# 
# 
# 示例3：
# 
# 
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表的长度范围为 [1, 100]
# 0 <= node.val <= 9
# 输入数据保证链表代表的数字无前导 0
# 
# 
# 
# 
# 进阶：如果输入链表不能翻转该如何解决？
# 
#
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans
# @lc code=end

