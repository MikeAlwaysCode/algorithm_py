from collections import Counter, defaultdict

def solve() -> None:
    n, m = map(int, input().split())
    s = input()
    c1 = s.count("1")
    c0 = n - c1
    
    if c0 == n: # 全是0
        ans = n * m
    elif c1 == n: # 全是1
        ans = 0 if n*m&1 else 1
    elif c1&1 and m&1: # 奇数个1，m是奇数
        ans = 0
    elif not m&1: # 偶数个1或奇数个1，m是偶数
        k = s.index("1")
        l = n - s.rindex("1") - 1
        ans = k + l + 1
    else: # 偶数个1且m是奇数
        k = c1 // 2
        l = 0
        for x in s:
            if x == '1':
                if k > 0:
                    k -= 1
                else:
                    break
            else:
                if k == 0:
                    l += 1
        ans = l + 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()