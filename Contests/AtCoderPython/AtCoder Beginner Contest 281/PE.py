# https://atcoder.jp/contests/abc281/tasks/abc281_e
mod = 998244353


def main():
    import sys
    input = sys.stdin.readline

    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

        def lower_bound(self, w):
            if w <= 0:
                return 0
            x = 0
            k = 1 << (self.size.bit_length() - 1)
            while k:
                if x + k <= self.size and self.tree[x + k] < w:
                    w -= self.tree[x + k]
                    x += k
                k >>= 1
            return x + 1

    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    A_sorted = sorted(list(set(A)))
    idx = {a: i+1 for i, a in enumerate(A_sorted)}
    L = len(idx)
    bit_num = Bit(L)
    bit_val = Bit(L)
    for a in A[:M]:
        i = idx[a]
        bit_num.add(i, 1)
        bit_val.add(i, a)
    ans = []
    k = bit_num.lower_bound(K)
    k_num = bit_num.sum(k)
    ans.append(bit_val.sum(k) - A_sorted[k - 1] * (k_num - K))
    for i in range(M, N):
        a = A[i]
        b = A[i - M]
        ja = idx[a]
        jb = idx[b]
        bit_num.add(ja, 1)
        bit_num.add(jb, -1)
        bit_val.add(ja, a)
        bit_val.add(jb, -b)
        k = bit_num.lower_bound(K)
        k_num = bit_num.sum(k)
        ans.append(bit_val.sum(k) - A_sorted[k-1] * (k_num - K))
    print(*ans)


if __name__ == '__main__':
    main()
