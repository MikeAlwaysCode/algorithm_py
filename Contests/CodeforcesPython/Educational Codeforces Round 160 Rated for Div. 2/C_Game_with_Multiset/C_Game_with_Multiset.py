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
    cnt = [0] * 31
    for _ in range(sint()):
        t, x = mint()
        if t == 1:
            cnt[x] += 1
        else:
            check = True
            cur = 0
            for i in range(31):
                cur = cur // 2 + cnt[i]
                if (x >> i) & 1:
                    if cur == 0:
                        check = False
                        break
                    cur -= 1
            print("YES" if check else "NO")

solve()
