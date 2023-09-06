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

	var n, m, r, c int
	Fscan(in, &n, &m, &r, &c)
	g := make([][]int, n)
	pres := make([][]int, n+1)
	pres[0] = make([]int, m+1)
	ans := -int(1e18)
	for i := range g {
		g[i] = make([]int, m)
		pres[i+1] = make([]int, m+1)
		for j := range g[i] {
			Fscan(in, &g[i][j])
			pres[i+1][j+1] = pres[i][j+1] + pres[i+1][j] - pres[i][j] + g[i][j]
			if i+1 >= r && j+1 >= c {
				ans = max(ans, pres[i+1][j+1]-pres[i+1-r][j+1]-pres[i+1][j+1-c]+pres[i+1-r][j+1-c])
			}
		}
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
