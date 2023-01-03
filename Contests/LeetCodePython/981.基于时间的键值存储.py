#
# @lc app=leetcode.cn id=981 lang=python3
#
# [981] 基于时间的键值存储
#
# https://leetcode.cn/problems/time-based-key-value-store/description/
#
# algorithms
# Medium (53.13%)
# Likes:    189
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 53.4K
# Testcase Example:  '["TimeMap","set","get","get","set","get","get"]\n' +
  '[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]'
#
# 设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。
# 
# 实现 TimeMap 类：
# 
# 
# TimeMap() 初始化数据结构对象
# void set(String key, String value, int timestamp) 存储键 key、值 value，以及给定的时间戳
# timestamp。
# String get(String key, int timestamp)
# 
# 返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev  。
# 如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
# 如果没有值，则返回空字符串（""）。
# 
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo",
# 4], ["foo", 5]]
# 输出：
# [null, null, "bar", "bar", null, "bar2", "bar2"]
# 
# 解释：
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1   
# timeMap.get("foo", 1);         // 返回 "bar"
# timeMap.get("foo", 3);         // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo"
# 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
# timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4  
# timeMap.get("foo", 4);         // 返回 "bar2"
# timeMap.get("foo", 5);         // 返回 "bar2"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# key 和 value 由小写英文字母和数字组成
# 1 
# set 操作中的时间戳 timestamp 都是严格递增的
# 最多调用 set 和 get 操作 2 * 10^5 次
# 
# 
#
import bisect
from collections import defaultdict


# @lc code=start
class TimeMap:

    def __init__(self):
      self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
      self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
      if not self.map[key]:
        return ""
      j = bisect.bisect(self.map[key], [timestamp + 1])
      if j > 0:
        return self.map[key][j - 1][1]
      else:
        return ""
      # j = bisect.bisect(self.map[key], [timestamp])
      # if j == len(self.map[key]) or (j > 0 and self.map[key][j][0] > timestamp):
      #   return self.map[key][j - 1][1]
      # elif self.map[key][j][0] == timestamp:
      #   return self.map[key][j][1]
      # else:
      #   return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

