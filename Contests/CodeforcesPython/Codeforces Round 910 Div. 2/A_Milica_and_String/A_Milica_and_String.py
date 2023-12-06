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
    n, k = mint()
    s = input()
    cnt = s.count('B')
    if cnt == k:
        print(0)
    elif cnt < k:
        for i in range(n):
            if s[i] == 'A':
                cnt += 1
                if cnt == k:
                    print(1)
                    print(i + 1, 'B')
    else:
        for i in range(n):
            if s[i] == 'B':
                cnt -= 1
                if cnt == k:
                    print(1)
                    print(i + 1, 'A')

for _ in range(int(input())):
    solve()