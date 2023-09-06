package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, u, v int
	Fscan(in, &n)
	a := make([]int64, n)
	for i := range a {
		Fscan(in, &a[i])
	}
	g := make([][]int, n)
	for i := 0; i < n-1; i++ {
		Fscan(in, &u, &v)
		u--
		v--
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	check := func(x int64) bool {
		y := int64(math.Sqrt(float64(x)))
		return y*y == x
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, 2)
	}
	var dfs func(x, p int)
	dfs = func(x, p int) {
		for _, y := range g[x] {
			if y == p {
				continue
			}
			dfs(y, x)
			dp[x][1] += max(dp[y][0], dp[y][1])
			if check(a[x] * a[y]) {
				dp[x][1] = max(dp[x][1], dp[x][0]+dp[y][0]+2)
			}
			dp[x][0] += max(dp[y][0], dp[y][1])
		}
	}
	dfs(0, -1)
	ans := max(dp[0][0], dp[0][1])
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
