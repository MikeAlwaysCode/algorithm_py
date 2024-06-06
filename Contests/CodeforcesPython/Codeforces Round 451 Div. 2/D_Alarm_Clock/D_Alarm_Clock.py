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
    n, m, k = mint()
    nums = ints()
    nums.sort()
    ans = 0
    l = cnt = 0
    for r, x in enumerate(nums):
        cnt += 1
        while x - nums[l] + 1 > m:
            cnt -= int(nums[l] > 0)
            l += 1
        if cnt == k:
            nums[r] = 0
            cnt -= 1
            ans += 1
    '''
    q = deque()
    for x in nums:
        q.append(x)
        while x - q[0] + 1 > m:
            q.popleft()
        while len(q) >= k:
            ans += 1
            q.pop()
    '''
    print(ans)

solve()
