def solve(arr) -> None:
    for i in range(N):
        for j in range(i+1, N):
            if not ( (arr[i][j] == arr[j][i] and arr[i][j] == 'D') or (arr[i][j] == 'L' and arr[j][i] == 'W') or (arr[i][j] == 'W' and arr[j][i] == 'L' )):
                return "incorrect"
    return "correct"

N = int(input())
a = []
for i in range(N):
    a.append(str(input()))

print(solve(a))
