#
# @lc app=leetcode.cn id=1146 lang=python3
#
# [1146] 快照数组
#
# https://leetcode.cn/problems/snapshot-array/description/
#
# algorithms
# Medium (32.56%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 24K
# Testcase Example:  '["SnapshotArray","set","snap","set","get"]\n[[3],[0,5],[],[0,6],[0,0]]'
#
# 实现支持下列接口的「快照数组」- SnapshotArray：
# 
# 
# SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
# void set(index, val) - 会将指定索引 index 处的元素设置为 val。
# int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
# int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
# 
# 
# 
# 
# 示例：
# 
# 输入：["SnapshotArray","set","snap","set","get"]
# ⁠    [[3],[0,5],[],[0,6],[0,0]]
# 输出：[null,null,0,null,5]
# 解释：
# SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
# snapshotArr.set(0,5);  // 令 array[0] = 5
# snapshotArr.snap();  // 获取快照，返回 snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
# 
# 
# 
# 提示：
# 
# 
# 1 <= length <= 50000
# 题目最多进行50000 次set，snap，和 get的调用 。
# 0 <= index < length
# 0 <= snap_id < 我们调用 snap() 的总次数
# 0 <= val <= 10^9
# 
# 
#
from collections import defaultdict
import bisect
# @lc code=start
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = defaultdict(list)
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index] and self.arr[index][-1][0] == self.snapId:
            self.arr[index].pop()
        self.arr[index].append((self.snapId, val))

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        if not self.arr[index] or self.arr[index][0][0] > snap_id:
            return 0
        j = bisect.bisect(self.arr[index], snap_id, key = lambda x: x[0])

        if j == len(self.arr[index]):
            return self.arr[index][-1][1]
        elif self.arr[index][j][0] == snap_id:
            return self.arr[index][j][1]
        else:
            return self.arr[index][j-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

