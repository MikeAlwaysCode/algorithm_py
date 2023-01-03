#
# @lc app=leetcode.cn id=855 lang=python3
#
# [855] 考场就座
#
# https://leetcode.cn/problems/exam-room/description/
#
# algorithms
# Medium (41.31%)
# Likes:    133
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 20.6K
# Testcase Example:  '["ExamRoom","seat","seat","seat","seat","leave","seat"]\n[[10],[],[],[],[],[4],[]]'
#
# 在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。
# 
# 
# 当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在
# 0 号座位上。)
# 
# 返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int
# （整型数据），代表学生坐的位置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。每次调用
# ExamRoom.leave(p) 时都保证有学生坐在座位 p 上。
# 
# 
# 
# 示例：
# 
# 输入：["ExamRoom","seat","seat","seat","seat","leave","seat"],
# [[10],[],[],[],[],[4],[]]
# 输出：[null,0,9,4,2,null,5]
# 解释：
# ExamRoom(10) -> null
# seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
# seat() -> 9，学生最后坐在 9 号座位上。
# seat() -> 4，学生最后坐在 4 号座位上。
# seat() -> 2，学生最后坐在 2 号座位上。
# leave(4) -> null
# seat() -> 5，学生最后坐在 5 号座位上。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^9
# 在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
# 保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。
# 
# 
#
import bisect
from heapq import heappop, heappush

# @lc code=start
from sortedcontainers import SortedSet


class ExamRoom(object):
    def __init__(self, N):
        self.n = N
        self.students = SortedSet()
        self.h = []

    def seat(self):
        if not self.students:
            self.students.add(0)
            return 0
        
        left = self.students[0]
        right = self.n - 1 - self.students[-1]
        while len(self.students) >= 2:
            (d, l, r) = self.h[0]
            if l in self.students and r in self.students and self.students[bisect.bisect(self.students, l)] == r:
                d = -d
                if d < right or d <= left:
                    break
                heappop(self.h)
                heappush(self.h, (- (d // 2), l, l + d))
                heappush(self.h, (- ((r - l - d) // 2), l + d, r))

                self.students.add(l + d)
                return l + d

            heappop(self.h)
        if right > left:
            heappush(self.h, (- (right // 2), self.students[-1], self.n - 1))
            self.students.add(self.n - 1)
            return self.n - 1
        else:
            heappush(self.h, (- (left // 2), 0, self.students[0]))
            self.students.add(0)
            return 0
        
    def leave(self, p):
        if p != self.students[0] and p != self.students[-1]:
            j = bisect.bisect_left(self.students, p)
            pr = self.students[j + 1]
            pl = self.students[j - 1]
            heappush(self.h, (- ((pr - pl) // 2), pl, pr))
        self.students.remove(p)

    '''
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)
    '''
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
# @lc code=end

def main():
    sol = ExamRoom(10)

    print(sol.seat())
    print(sol.seat())
    print(sol.seat())
    print(sol.seat())
    sol.leave(4)
    print(sol.seat())

if __name__ == '__main__':
    main()

