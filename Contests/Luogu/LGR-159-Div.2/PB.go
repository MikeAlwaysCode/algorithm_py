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

	var T, n, m, k, x int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m, &k)
		ans := m
		pos := make([][]int, k+1)
		for i := 0; i < n; i++ {
			Fscan(in, &x)
			pos[x] = append(pos[x], i)
		}
		for i := range pos {
			l := 0
			for r := range pos[i] {
				if pos[i][r]-r <= m {
					ans = max(ans, min(n, m+r+1))
					continue
				}
				for ; pos[i][r]-pos[i][l]-r+l > m; l++ {
				}
				ans = max(ans, min(m+r-l+1, n))
			}
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
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
