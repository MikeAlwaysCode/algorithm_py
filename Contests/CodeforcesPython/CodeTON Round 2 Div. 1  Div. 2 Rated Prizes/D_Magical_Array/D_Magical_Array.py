t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    # Operation 1
    # 1. ai−1×(i−1)+ai×i+aj×j+aj+1×(j+1)=i×(ai−1+ai)+j×(aj+aj+1)−ai−1+aj+1
    # 2. (ai−1+1)×(i−1)+(ai−1)×i+(aj−1)×j+(aj+1+1)×(j+1)    =i×(ai−1+ai)+j×(aj+aj+1)−ai−1+aj+1
    # See what? Yes, even if you give lots of operation 1 to array a, the sum of (ai×i) remains. Thus, you can easily find ck.
    
    # Operation 2
    # 1. ai−1×(i−1)+ai×i+aj×j+aj+1×(j+1)+aj+2×(j+2)    =i×(ai−1+ai)+j×(aj+aj+1+aj+2)−ai−1+aj+1+2×aj+2
    # 2. (ai−1+1)×(i−1)+(ai−1)×i+(aj−1)×j+aj+1×(j+1)+(aj+2+1)×(j+2)    =i×(ai−1+ai)+j×(aj+aj+1+aj+2)−ai−1+aj+1+2×aj+2+1
    # This operation will add 1 to the result of ∑ai×i.

    chk = dict()
    val_o1 = 0
    for i in range(n):
        val = sum([arr[i][j] * (j + 1) for j in range(m)])
        if val not in chk:
            chk[val] = i + 1
        else:
            chk[val] = -1
            val_o1 = val
    # print(chk)
    for k, v in chk.items():
        if v != -1:
            print(v, k - val_o1)
            break