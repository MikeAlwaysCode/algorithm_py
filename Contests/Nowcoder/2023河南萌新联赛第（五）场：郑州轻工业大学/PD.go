package main

import (
	"bufio"
	// "container/heap"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n int
	var s string
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &s)

		ans := 0

		dp := make([]int, 2)
		for _, c := range s {
			if c == '0' {
				dp[0] += 1
				dp[1] = 0
			} else if c == '1' {
				dp[0] = 0
				dp[1] += 1
			} else {
				dp[0] += 1
				dp[1] += 1
			}
			ans = max(ans, max(dp[0], dp[1]))
		}

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
