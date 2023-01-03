from collections import Counter, defaultdict

def solve() -> None:
    s = str(input())
    n = len(s)
    k = s.count("0")
    if k == n or k == 0:
        print(0)
        return
    ans = cnt1 = s[:k].count("1")
    for i, o in zip(s[k:], s):
        cnt1 += (i == '1') - (o == '1')
        ans = min(ans, cnt1)
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()