from string import ascii_lowercase


class DoubleWordLadder:
    def transform(self, A, B):
        if A == B:
            return tuple(B)

        ans = []
        n = len(A)
        for i in range(n):
            if A[i] != B[i]:
                for x in ascii_lowercase:
                    if x != A[i] & x != B[i]:
                        ans.append(A[:i] + x + A[i+1:])
                        ans.append(A[:i] + B[i] + A[i+1:])
                        break
        
def main():
    A = "donation"
    B = "solution"
    sol = DoubleWordLadder()

    print(sol.transform(A, B))

if __name__ == '__main__':
    main()