package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	// n = sint()
	// A = ints()
	// B = ints()
	// # dp[i]：当前填小于等于i的方案数
	// dp = [0] * 3001
	// dp[A[0]] = 1
	// for i in range(A[0] + 1, 3001):
	//     dp[i] = dp[i - 1]
	//     if i <= B[0]:
	//         dp[i] += 1
	// for a, b in zip(A[1:], B[1:]):
	//     tmp = [0] * 3001
	//     tmp[a] = dp[a]
	//     for i in range(a + 1, 3001):
	//         tmp[i] = tmp[i - 1]
	//         if i <= b:
	//             # 当前可以填i，加上前一位dp[i]方案数
	//             tmp[i] = (tmp[i] + dp[i]) % MOD
	//     dp = tmp
	// print(dp[-1])

	const mod = 998244353
	var n int
	Fscan(in, &n)
	a := make([]int, n)
	b := make([]int, n)
	for i := range a {
		Fscan(in, &a[i])
	}
	for i := range b {
		Fscan(in, &b[i])
	}
	f := make([]int, 3001)
	g := make([]int, 3001)
	f[a[0]] = 1
	for i := a[0] + 1; i < 3001; i++ {
		f[i] = f[i-1]
		if i <= b[0] {
			f[i]++
		}
	}
	for i := 1; i < n; i++ {
		for j := 0; j < 3001; j++ {
			if j < a[i] {
				g[j] = 0
			} else if j == a[i] {
				g[j] = f[j]
			} else {
				g[j] = g[j-1]
				if j <= b[i] {
					g[j] = (g[j] + f[j]) % mod
				}
			}
		}
		f, g = g, f
	}
	Fprintln(out, f[3000])
}

func main() { solve(os.Stdin, os.Stdout) }
