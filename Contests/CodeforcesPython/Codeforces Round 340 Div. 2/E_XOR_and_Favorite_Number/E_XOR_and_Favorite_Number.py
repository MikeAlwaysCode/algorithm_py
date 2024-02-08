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
    n, q, k = mint()
    nums = ints()
    left = []
    right = []
    for _ in range(q):
        l, r = mint()
        left.append(l - 1)
        right.append(r + 1)
    
    pres = [0] * (n + 1)
    for i, x in enumerate(nums):
        pres[i + 1] = pres[i] ^ x

    # Mo's algorithm
    qi = list(range(q))
    '''
    block_size = int(1.4 * n // (int(q ** 0.5) + 1)) + 1
    qi.sort(key = lambda x: (right[x] // block_size, left[x] * (-1) ** (right[x] // block_size)))
    '''
    block_size = int(n ** 0.5)
    qi.sort(key = lambda x: ((left[x] - 1) // block_size + 1, right[x]))

    # ans = [0] * q
    ans = [None] * q
    curr = l = r = 0
    cnt = [0] * (1 << 20)

    def add(x: int):
        nonlocal curr
        curr += cnt[pres[x] ^ k]
        cnt[pres[x]] += 1
    
    def delete(x: int):
        nonlocal curr
        cnt[pres[x]] -= 1
        curr -= cnt[pres[x] ^ k]

    for i in qi:
        nl, nr = left[i], right[i]
        while r < nr:
            add(r)
            r += 1
        while nr < r:
            r -= 1
            delete(r)
        while nl < l:
            l -= 1
            add(l)
        while l < nl:
            delete(l)
            l += 1
        ans[i] = curr

    print(*ans, sep = "\n")


solve()
