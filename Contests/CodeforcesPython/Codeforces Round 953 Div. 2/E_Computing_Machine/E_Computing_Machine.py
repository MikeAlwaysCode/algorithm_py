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
    s = input()
    t = input()
    
    pres = [0] * (n + 1)
    
    left, right = list(range(n)), list(range(n))
    for i in range(n):
        pres[i + 1] = pres[i]
        if s[i] == '1':
            pres[i + 1] += 1
        else:
            l = r = -1
            if i > 0 and t[i - 1] == '1':
                l = i - 1
            elif i > 1 and s[i - 2] == '0':
                l = i - 2
            if i < n - 1 and t[i + 1] == '1':
                r = i + 1
            elif i < n - 2 and s[i + 2] == '0':
                r = i + 2
            if l != -1 and r != -1:
                left[i], right[i] = l, r
                pres[i + 1] += 1
    
    for i in range(sint()):
        l, r = mint()
        ans = pres[r] - pres[l - 1]
        # print("---", ans)
        for i in range(l - 1, min(l + 1, r)):
            if left[i] < l - 1 or right[i] >= r:
                ans -= 1
        for i in range(max(l + 1, r - 2), r):
            if left[i] < l - 1 or right[i] >= r:
                ans -= 1
        print(ans)


for _ in range(int(input())):
    solve()
