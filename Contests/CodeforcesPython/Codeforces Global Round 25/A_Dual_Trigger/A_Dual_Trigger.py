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
    cnt = s.count('1')
    if cnt & 1:
        print("NO")
        return
    if cnt > 2:
        print("YES")
        return
    for i in range(1, n):
        if s[i - 1] == '1' and s[i] == '1':
            print("NO")
            return
    print("YES")


for _ in range(int(input())):
    solve()
