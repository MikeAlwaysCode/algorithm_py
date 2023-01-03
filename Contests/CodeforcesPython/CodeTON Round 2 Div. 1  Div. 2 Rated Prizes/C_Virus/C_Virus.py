t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = []
    pre = a[-1] - n
    for i in a:
        nif = i - pre - 1
        if nif > 0: l.append(nif)
        pre = i

    if len(l) <= 0:
        print(n)
        continue
    l.sort()
    # print(l)
    infect = 0
    protect = 0
    for i in range(len(l) - 1, -1, -1):
        tmp = l[i] - infect
        # print(tmp)
        if tmp <= 0:
            break
        elif tmp <= 2:
            protect += 1
            break
        else:
            protect += tmp - 1
            infect += 4
        # print("Protect:",protect)
        # print("Infect:", infect)

    print(n - protect)