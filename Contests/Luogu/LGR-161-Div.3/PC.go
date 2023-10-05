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

	var n, k int
	Fscan(in, &n, &k)
	l := make([]int, n+1)
	r := make([]int, n+1)
	a := make([]int, n+1)
	for i := 1; i <= n; i++ {
		Fscan(in, &a[i])
		if l[a[i]] == 0 {
			l[a[i]] = i
		}
		r[a[i]] = i
	}
	b := make([]int, n+1)
	for i := 1; i <= n; i++ {
		Fscan(in, &b[i])
	}

	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, k+1)
	}

	for i := 1; i <= n; i++ {
		if l[i] == 0 {
			continue
		}
		dp[i][1] = b[i]
		for j := 1; j < i; j++ {
			if l[j] == 0 || r[j] > l[i] {
				continue
			}
			for m := 1; m <= min(j, k-1); m++ {
				if dp[j][m] == 0 {
					continue
				}
				dp[i][m+1] = max(dp[i][m+1], dp[j][m]+b[i])
			}
		}
	}

	ans := 0
	for i := 1; i <= n; i++ {
		ans = max(ans, dp[i][k])
	}

	if ans == 0 {
		Fprintln(out, -1)
	} else {
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
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
