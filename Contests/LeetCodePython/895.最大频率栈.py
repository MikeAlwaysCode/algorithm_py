#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#
# https://leetcode.cn/problems/maximum-frequency-stack/description/
#
# algorithms
# Hard (59.35%)
# Likes:    281
# Dislikes: 0
# Total Accepted:    16.8K
# Total Submissions: 27.3K
# Testcase Example:  '["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n' +
  '[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]'
#
# 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。
# 
# 实现 FreqStack 类:
# 
# 
# FreqStack() 构造一个空的堆栈。
# void push(int val) 将一个整数 val 压入栈顶。
# int pop() 删除并返回堆栈中出现频率最高的元素。
# 
# 如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# 
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# 输出：[null,null,null,null,null,null,null,5,7,5,4]
# 解释：
# FreqStack = new FreqStack();
# freqStack.push (5);//堆栈为 [5]
# freqStack.push (7);//堆栈是 [5,7]
# freqStack.push (5);//堆栈是 [5,7,5]
# freqStack.push (7);//堆栈是 [5,7,5,7]
# freqStack.push (4);//堆栈是 [5,7,5,7,4]
# freqStack.push (5);//堆栈是 [5,7,5,7,4,5]
# freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
# freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
# freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
# freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
# 
# 
# 
# 提示：
# 
# 
# 0 <= val <= 10^9
# push 和 pop 的操作数不大于 2 * 10^4。
# 输入保证在调用 pop 之前堆栈中至少有一个元素。
# 
# 
#
from heapq import heappop, heappush
from typing import Counter
# @lc code=start
class FreqStack:
  
    def __init__(self):
      self.d = []
      self.cnt = Counter()
      self.nums = 0

    def push(self, val: int) -> None:
      self.cnt[val] += 1
      self.nums += 1
      heappush(self.d, (-self.cnt[val], -self.nums, val))

    def pop(self) -> int:
      res = heappop(self.d)[2]
      self.cnt[res] -= 1
      return res

    '''
    def __init__(self):
      self.d = defaultdict(list)
      self.cnt = defaultdict(int)
      self.mx = 0

    def push(self, val: int) -> None:
      self.cnt[val] += 1
      self.d[self.cnt[val]].append(val)
      
      self.mx = max(self.mx, self.cnt[val])

    def pop(self) -> int:
      res = self.d[self.mx].pop()
      self.cnt[res] -= 1
      if not self.d[self.mx]:
        self.mx -= 1
      return res
    '''
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

