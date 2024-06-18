import sys
from collections import defaultdict
from random import getrandbits

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
    h = getrandbits(30)
    pos = defaultdict(list)
    for i, x in enumerate(nums, 1):
        pos[x ^ h].append(i)
    ans, l, r, mx = nums[0], 1, 1, 1
    for x, arr in pos.items():
        i = 0
        for j in range(len(arr)):
            if j * 2 - i * 2 + 1 - arr[j] + arr[i] < 1:
                i = j
            if j * 2 - i * 2 + 1 - arr[j] + arr[i] > mx:
                ans, l, r, mx = x ^ h, arr[i], arr[j], j * 2 - i * 2 + 1 - arr[j] + arr[i]
    print(ans, l, r)


for _ in range(int(input())):
    solve()
