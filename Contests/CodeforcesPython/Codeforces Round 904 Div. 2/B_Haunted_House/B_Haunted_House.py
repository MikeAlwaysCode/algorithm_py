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
    cnt = s.count('1')
    ans = [-1] * n
    j = n
    res = 0
    for i in range(n - cnt):
        if s[n - i - 1] == '1':
            j = min(j - 1, n - i - 2)
            while j >= 0 and s[j] == '1':
                j -= 1
            res += n - i - 1 - j
            s[j] = '1'
        ans[i] = res
    print(*ans)


for _ in range(int(input())):
    solve()