package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n int
	Fscan(in, &n)

	a := make([]int, n)
	for i := range a {
		Fscan(in, &a[i])
	}

	dp := make([]int, 3)
	var t string
	for _, v := range a {
		Fscan(in, &t)
		if t == "AA" { // 0
			dp[0] = max(dp[0]+v, dp[2]+v)
		} else if t == "aa" { // 1
			dp[1] = max(dp[1]+v, dp[2]+v)
		} else { // 2
			dp[2] = max(max(dp[0]+v, dp[1]+v), dp[2]+v)
		}
	}

	ans := 0
	for _, v := range dp {
		ans = max(ans, v)
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
