from typing import Counter

def solve() -> None:
    n = int(input())
    s = [[] for _ in range(3)]
    ans = [0] * 3
    cnt = Counter()
    for i in range(3):
        s[i] = list(map(str, input().split()))
        cnt.update(s[i])
    
    for i in range(3):
        for x in s[i]:
            if cnt[x] == 1:
                ans[i] += 3
            elif cnt[x] == 2:
                ans[i] += 1
    
    print(*ans)

t = int(input())
for _ in range(t):
    solve()