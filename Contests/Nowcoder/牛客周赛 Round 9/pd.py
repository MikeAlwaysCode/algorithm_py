from itertools import accumulate

n = int(input())
a = [int(c) for c in input().split()]

a.sort()
sum_ = sum(a)
if sum_ % n == 0:
    res = 0
    avg = sum_ // n
    for i in a:
        res += abs(avg - i)
    res //= 2
    print(res)
else:
    nums1 = a[1:]
    nums2 = a[:-1]

    def cal(nums):
        sum_ = sum(nums)
        avg = sum_ // len(nums) + (0 if sum_ % len(nums) == 0 else 1)
        x,y = 0, 0
        for num in nums:
            if num >= avg: x+= num -avg
            else: y+= avg - num
        return max(x,y)

    print(min(cal(nums1), cal(nums2)))