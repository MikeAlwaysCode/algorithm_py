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
	const maxint int = 1e9

	var n, m, v, mx int
	Fscan(in, &n, &m)
	g := 0
	a := make([]int, n)
	for i := range a {
		Fscan(in, &a[i])
		g = gcd(g, a[i])
		mx = max(mx, a[i])
	}
	b := map[int]bool{}
	for i := 0; i < m; i++ {
		Fscan(in, &v)
		b[v] = true
	}
	// Fprintln(out, g)
	dp := make([]int, mx+1)
	for i := 2; i <= mx; i++ {
		dp[i] = maxint
	}

	for k := range b {
		for i := k; i <= mx; i += k {
			if dp[i/k] != maxint {
				dp[i] = min(dp[i], dp[i/k]+1)
			}
		}
	}

	ans := maxint
	f := func(x int) int {
		res := 0
		for _, v := range a {
			v /= x
			if dp[v] == maxint {
				return maxint
			} else {
				res += dp[v]
			}
		}
		return res
	}
	for d := 1; d*d <= g; d++ {
		if g%d > 0 {
			continue
		}
		ans = min(ans, f(d))
		if d*d != g {
			ans = min(ans, f(g/d))
		}
	}
	if ans == maxint {
		Fprintln(out, -1)
	} else {
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func gcd(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
