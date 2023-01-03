def solve() -> None:
    n, q = map(int, input().split())
    MX = 1005
    area = [[0] * MX for _ in range(MX)]
    pref = [[0] * MX for _ in range(MX)]

    for i in range(n):
        h, w = map(int, input().split())
        area[h][w] += h * w
    
    for i in range(1, 1001):
        for j in range(1, 1001):
            pref[i][j] = pref[i][j-1] + pref[i-1][j] - pref[i-1][j-1] + area[i][j]
    
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))

    for i in range(q):
        hs, ws, hb, wb = query[i][0], query[i][1], query[i][2], query[i][3]
        print(pref[hb-1][wb-1] - pref[hs][wb-1] - pref[hb-1][ws] + pref[hs][ws])
        # print("res:", pref[hb-1][wb-1] - pref[hs][wb-1] - pref[hb-1][ws] + pref[hs][ws])

t = int(input())
for _ in range(t):
    solve()