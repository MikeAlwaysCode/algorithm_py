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
    s = input()
    ans = []
    p = []
    for c in s:
        while ans and ans[-1] > c:
            p.append(str(min(int(ans.pop()) + 1, 9)))
        ans.append(c)
    
    print("".join(sorted(ans + p)))

    '''
    n = len(s)
    pred = int(s[-1])
    for i in range(n - 2, -1, -1):
        d = int(s[i])
        if d <= pred:
            ans.append(str(pred))
            pred = d
        else:
            ans.append(str(min(d + 1, 9)))
    ans.append(str(pred))
    ans.sort()
    print("".join(ans))
    '''

for _ in range(int(input())):
    solve()
