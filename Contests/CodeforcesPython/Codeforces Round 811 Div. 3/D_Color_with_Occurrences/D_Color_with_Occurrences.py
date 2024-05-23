import math
import sys

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
    t = input()
    a = []
    for _ in range(sint()):
        a.append(input())
    
    n = len(t)
    dp = [0] * (n + 1)
    fr = [None for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i] = math.inf
        for j, s in enumerate(a):
            m = len(s)
            for k in range(max(i-m, 0), min(i, n - m + 1)):
                if t[k:k+m] == s and dp[k] + 1 < dp[i]:
                    dp[i] = dp[k] + 1
                    fr[i] = (j + 1, k)
    
    if dp[n] == math.inf:
        print(-1)
        return
    print(dp[n])
    i = n
    while fr[i][1]:
        print(fr[i][0], fr[i][1] + 1)
        i = fr[i][1]
    print(fr[i][0], fr[i][1] + 1)

    '''
    ans = []
    tLen = len(t)
    s = e = 0
    while e < tLen:
        id = pos = -1
        tmpEnd = e
        for i in range(s, e+1):
            for j in range(n):
                sLen = len(a[j])
                if i + sLen > tLen or i + sLen <= e:
                    # 大于t长度 or 不及前面到达的终点e
                    continue
                if t[i: i + sLen] == a[j]:
                    if i + sLen > tmpEnd:
                        tmpEnd = i + sLen
                        id = j
                        pos = i

        if id == -1:
            # 当前位置范围完全没有匹配的，返回-1
            print(-1)
            return
        ans.append((id+1, pos+1))
        if tmpEnd < tLen:
            s = e + 1
            e = tmpEnd
        else:
            break

    print(len(ans))
    for i, j in ans:
        print(i, j)
    '''

for _ in range(int(input())):
    solve()
