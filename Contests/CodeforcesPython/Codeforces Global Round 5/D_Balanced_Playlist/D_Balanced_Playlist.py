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
    nums = ints()
    nums = nums + nums + nums
    ans = [-1] * n
    q = deque()
    j = 0
    for i in range(n):
        while j < n * 3 and (not q or nums[j] * 2 >= nums[q[0]]):
            while q and nums[j] >= nums[q[-1]]:
                q.pop()
            q.append(j)
            j += 1
        if j < n * 3:
            ans[i] = j - i
        if q[0] == i:
            q.popleft()
    print(*ans)


solve()
