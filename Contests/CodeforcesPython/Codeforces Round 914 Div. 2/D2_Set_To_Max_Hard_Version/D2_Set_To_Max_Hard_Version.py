import sys
from collections import deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    nums1 = ints()
    nums2 = ints()

    stk = deque()
    for i in range(n):
        if nums1[i] > nums2[i]:
            print("NO")
            return
        while stk and stk[-1] <= nums1[i]:
            stk.pop()
        while stk and stk[0] > nums2[i]:
            stk.popleft()
        stk.append(nums1[i])
        if stk[0] == nums2[i]:
            nums1[i] = nums2[i]
    stk.clear()
    for i in range(n - 1, -1, -1):
        while stk and stk[-1] <= nums1[i]:
            stk.pop()
        while stk and stk[0] > nums2[i]:
            stk.popleft()
        stk.append(nums1[i])
        if stk[0] == nums2[i]:
            nums1[i] = nums2[i]
    print("YES" if nums1 == nums2 else "NO")


for _ in range(int(input())):
    solve()
