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
    n, x = mint()

    if x == n:
        print(n)
        return
    
    while n > x:
        lb = n & -n
        n -= n & -n
        if n == x and not n & (lb << 1):
            print(n | (lb << 1))
            return
    print(-1)

    '''
    if n & x != x:
        print(-1)
        return

    if x == n:
        print(n)
        return
        
    max_bit = n.bit_length()
    check = False
    i = max_bit + 1
    for bit in range(max_bit, -1, -1):
        if (n >> bit) & 1:
            if check:
                if (x >> bit) & 1:
                    print(-1)
                    return
            elif (x >> bit) & 1 == 0:
                if i != bit + 1:
                    print(-1)
                    return
                n |= 1 << i
                i = bit
                check = True
        elif not check:
            i = bit

    print(n - (n & ((1 << (i + 1)) - 1)))
    '''

for _ in range(int(input())):
    solve()
