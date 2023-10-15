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

	var T, n, rating int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		for i := 0; i < n; i++ {
			Fscan(in, &rating)
		}
		c := make([]int, n)
		for i := range c {
			Fscan(in, &c[i])
		}
		ans := 0
		suff := c[n-1]
		for i := n - 2; i >= 0; i-- {
			ans = max(ans, suff-c[i])
			suff = max(suff, max(max(suff-c[i], suff+c[i]), c[i]))
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
