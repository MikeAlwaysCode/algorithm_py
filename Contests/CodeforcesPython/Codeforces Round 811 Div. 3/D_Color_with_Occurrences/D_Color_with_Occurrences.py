def solve() -> None:
    t = input()
    n = int(input())
    a = list()
    for _ in range(n):
        a.append(input())
    
    ans = list()
    tLen = len(t)
    s = e = 0
    while e < tLen:
        id = pos = -1
        tmpEnd = e
        for i in range(s, e+1):
            for j in range(n):
                sLen = len(a[j])
                if i + sLen > tLen or i + sLen <= e:
                    # 大于t长度 or 不及前面到达的终点e
                    continue
                if t[i: i + sLen] == a[j]:
                    if i + sLen > tmpEnd:
                        tmpEnd = i + sLen
                        id = j
                        pos = i

        if id == -1:
            # 当前位置范围完全没有匹配的，返回-1
            print(-1)
            return
        ans.append((id+1, pos+1))
        if tmpEnd < tLen:
            s = e + 1
            e = tmpEnd
        else:
            break
    print(len(ans))
    # for i in range(len(ans)):
    #     print(ans[i][0], ans[i][1])
    # print((ans[i][0], ans[i][1]) for i in range(len(ans)))
    [print(ans[i][0], ans[i][1]) for i in range(len(ans))]

q = int(input())

for _ in range(q):
    solve()