import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

def solve() -> None:
    s = input()
    cnt = qc = 0
    for c in s:
        if c == "(":
            cnt += 1
        elif c == ")":
            cnt -= 1
            if cnt < 0:
                # 当前)比(多，由于s必定是一个合法rbs，前面必须有一个?变成(
                cnt += 1
                qc -= 1
        else:
            if cnt > 0:
                qc += 1
            else:
                # 如果前面()一样多，当前?不可能变成)
                cnt += 1
        
        if cnt == 0 and qc == 1:
            # 如果前面()一样多，且存在一个?，则?不可能变成)
            cnt += 1
            qc -= 1
    
    print("YES" if abs(cnt) == qc or qc == 1 else "NO")

for _ in range(sint()):
    solve()