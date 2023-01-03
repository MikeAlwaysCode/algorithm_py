n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for ai in a:
    s.append(s[-1] + ai)

def calc(i, j, m):
    while i <= n and j <= n:
        diff = s[j] - s[i]
        if diff == m:
            return (i, j)
        elif diff > m:
            i += 1
        elif diff < m:
            j += 1
    return False

if calc(0, 0, p):
    i, j = calc(0, 0, p)
    if calc(j, j, q):
        i, j = calc(j, j, q)
        if calc(j, j, r):
            print('Yes')
            exit()
print('No')