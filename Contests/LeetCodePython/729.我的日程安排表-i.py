#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#
# https://leetcode.cn/problems/my-calendar-i/description/
#
# algorithms
# Medium (58.50%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    48.5K
# Total Submissions: 82.8K
# Testcase Example:  '["MyCalendar","book","book","book"]\n[[],[10,20],[15,25],[20,30]]'
#
# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。
# 
# 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。
# 
# 日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x <
# end 。
# 
# 实现 MyCalendar 类：
# 
# 
# MyCalendar() 初始化日历对象。
# boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回
# false 并且不要将该日程安排添加到日历中。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# 输出：
# [null, true, false, true]
# 
# 解释：
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False ，这个日程安排不能添加到日历中，因为时间 15
# 已经被另一个日程安排预订了。
# myCalendar.book(20, 30); // return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于
# 20 ，且不包含时间 20 。
# 
# 
# 
# 提示：
# 
# 
# 0 <= start < end <= 10^9
# 每个测试用例，调用 book 方法的次数最多不超过 1000 次。
# 
# 
#

# @lc code=start
class MyCalendar:
    def __init__(self):
        self.tree = set()
        self.lazy = set()

    def query(self, start: int, end: int, l: int, r: int, idx: int) -> bool:
        if r < start or end < l:
            return False
        if idx in self.lazy:  # 如果该区间已被预订，则直接返回
            return True
        if start <= l and r <= end:
            return idx in self.tree
        mid = (l + r) // 2
        return self.query(start, end, l, mid, 2 * idx) or \
               self.query(start, end, mid + 1, r, 2 * idx + 1)

    def update(self, start: int, end: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree.add(idx)
            self.lazy.add(idx)
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, 2 * idx)
            self.update(start, end, mid + 1, r, 2 * idx + 1)
            self.tree.add(idx)
            if 2 * idx in self.lazy and 2 * idx + 1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start: int, end: int) -> bool:
        if self.query(start, end - 1, 0, 10 ** 9, 1):
            return False
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return True
'''
from sortedcontainers import SortedDict


class MyCalendar:

    def __init__(self):
        self.booked = SortedDict()

    def book(self, start: int, end: int) -> bool:
        i = self.booked.bisect_left(end)
        if i == 0 or self.booked.items()[i - 1][1] <= start:
            self.booked[start] = end
            return True
        return False
'''

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

