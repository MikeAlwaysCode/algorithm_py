t = int(input())
for _ in range(t):
    mab, mbc, mca = map(int, input().split())

    if min(mab, mbc) == mca or min(mab, mca) == mbc or mab == min(mbc, mca):
        print("YES")
    else:
        print("NO")