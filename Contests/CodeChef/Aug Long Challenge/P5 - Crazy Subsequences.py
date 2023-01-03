from collections import Counter, defaultdict

def solve() -> None:
    s = str(input())

    ans = ""
    n = len(s)
    m = k = 0
    preZero = occurrence = 0
    for i, x in enumerate(s):
        if x == '0':
            m += 1
        else:
            m = 1 if m&1 else 2 if m > 0 else 0
            preZero += m
            if m > 0:
                occurrence += 1
            m = 0

            if preZero&1 or occurrence < 2:
                k = preZero if occurrence < 2 else preZero & 1
            else:
                k = 0
            # print(preZero, occurrence, k)
            
            if k >= n - i - 1:
                k -= n - i - 1
                # print(k)
                if k > 0:
                    ans += "0" * k
                ans += "1"
                break
            ans += "1"
            
    if m > 0:
        if preZero&1 or occurrence < 2:
            k = preZero if occurrence < 2 else preZero & 1
        else:
            k = 0
        ans += "0" * (m - k)
    print(ans)

t = int(input())
for _ in range(t):
    solve()