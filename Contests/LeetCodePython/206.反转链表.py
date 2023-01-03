#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode.cn/problems/reverse-linked-list/description/
#
# algorithms
# Easy (73.24%)
# Likes:    2686
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,2]
# 输出：[2,1]
# 
# 
# 示例 3：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目范围是 [0, 5000]
# -5000 
# 
# 
# 
# 
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
# 
# 
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
# @lc code=end

