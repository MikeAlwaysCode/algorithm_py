from collections import defaultdict
from itertools import count


def solve() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    def check(ans: int) -> bool:
        cnt = defaultdict(int)
        for x in a:
            # 前i位的组合 +1 
            cnt[x & ans] += 1
        for x in b:
            # 前i位的组合 -1
            cnt[~x & ans] -= 1
        
        return not [v for v in cnt.values() if v != 0]
        
    ans = 0
    for i in range(30, -1, -1):
        if check(ans | (1 << i)):
            ans |= 1 << i
    print(ans)

t = int(input())
for _ in range(t):
    solve()