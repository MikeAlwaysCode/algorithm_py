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

suit = "CDHS"

def solve() -> None:
    n = sint()
    z = suit.index(input())
    cards = [[] for _ in range(4)]
    for card in input().split():
        i = suit.index(card[1])
        cards[i].append(card[0])

    ans = []
    k = 0
    cards[z].sort()
    for i in range(4):
        if i == z:
            continue
        cards[i].sort()
        j = 1
        while j < len(cards[i]):
            ans.append(cards[i][j - 1] + suit[i] + ' ' + cards[i][j] + suit[i])
            j += 2
        if j == len(cards[i]):
            if k >= len(cards[z]):
                print("IMPOSSIBLE")
                return
            ans.append(cards[i][j - 1] + suit[i] + ' ' + cards[z][k] + suit[z])
            k += 1
    while k < len(cards[z]):
        ans.append(cards[z][k] + suit[z] + ' ' + cards[z][k + 1] + suit[z])
        k += 2
    for p in ans:
        print(p)

for _ in range(int(input())):
    solve()
