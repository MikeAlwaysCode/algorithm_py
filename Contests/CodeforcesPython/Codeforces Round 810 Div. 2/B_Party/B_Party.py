t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n

    pairs = []
    mina, index = 10 ** 5, 0
    for i in range(m):
        x, y = map(int, input().split())
        pairs.append((x, y))

        b[x-1] += 1
        b[y-1] += 1

    if not ( m & 1 ):
        print(0)
        continue
    # print(b)
    for i in range(m):
        if b[pairs[i][0]-1] & 1:
            mina = min(mina, a[pairs[i][0]-1])
        if b[pairs[i][1]-1] & 1:
            mina = min(mina, a[pairs[i][1]-1])
        if not ((b[pairs[i][0]-1] + b[pairs[i][1]-1]) & 1):
            mina = min(mina, a[pairs[i][0]-1]+a[pairs[i][1]-1])
    print(mina)