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
    n = sint()
    s = list(input())
    stk = []
    for i, c in enumerate(s):
        while stk and s[stk[-1]] < c:
            stk.pop()
        stk.append(i)
    
    ans = len(stk) - 1
    i, j = 0, len(stk) - 1
    while i < j:
        s[stk[i]], s[stk[j]] = s[stk[j]], s[stk[i]]
        i += 1
        j -= 1

    for i in range(1, n):
        if s[i] < s[i - 1]:
            print(-1)
            return
    
    for i in range(n - 2, -1, -1):
        if s[i] == s[i + 1]:
            ans -= 1
        else:
            break
        
    print(ans)


for _ in range(int(input())):
    solve()
