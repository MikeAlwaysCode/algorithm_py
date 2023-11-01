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
    z0 = s.count('0')
    c = (z0 // 2 > 0) ^ (n & 1 and s[n // 2] == '0')
    def isPalindrome(s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    if isPalindrome(s):
        print("BOB" if c else "ALICE")
    elif z0 == 2 and n & 1 and s[n // 2] == '0':
        print("DRAW")
    else:
        print("ALICE")

for _ in range(int(input())):
    solve()