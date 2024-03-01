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
    ans = [-1] * n
    left, right = [], []
    for i in range(n):
        if s[i] == '>':
            right.append(i)
        else:
            left.append(i)
    left.reverse()
    more = 0
    for i in range(n):
        if not left:
            break
        more += (left.pop() - i) * 2
        ans[i] = i + 1 + more
    more = 0
    for i in range(n - 1, -1, -1):
        if not right:
            break
        more += (i - right.pop()) * 2
        ans[i] = n - i + more
    print(*ans)

for _ in range(int(input())):
    solve()
