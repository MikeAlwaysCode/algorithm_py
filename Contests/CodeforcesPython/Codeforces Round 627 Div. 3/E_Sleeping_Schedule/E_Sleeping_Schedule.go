package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func CF1324E(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, h, l, r int
	Fscan(in, &n, &h, &l, &r)
	var a int
	// arr := make([]int, n)
	dp := make([]int, n+1)
	pres := 0
	for i := 0; i < n; i++ {
		// Fscan(in, &arr[i])
		Fscan(in, &a)

		pres += a
		for j := i + 1; j >= 0; j-- {
			if j > 0 {
				dp[j] = max(dp[j], dp[j-1])
			}
			if (pres-j)%h >= l && (pres-j)%h <= r {
				dp[j]++
			}
		}
	}

	ans := 0
	for _, v := range dp {
		ans = max(ans, v)
	}
	Fprintln(out, ans)
}

func main() { CF1324E(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
