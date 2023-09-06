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

	var n, a, b int
	h := make([]int, 8)

	li := [4]int{2, 3, 2, 3}
	hi := [4][3]int{{3, 3, 3}, {2, 1, 1}, {1, 3, 0}, {2, 2, 2}}
	end := [4][3]int{{0, -2, 0}, {0, 0, 0}, {0, 0, 0}, {-1, -1, 0}}

	for Fscan(in, &n); n > 0; n-- {
		Fscan(in, &a, &b)
		a /= 90
		mx := 0
		for i, j := b-1, 0; j < li[a]; j++ {
			mx = max(mx, h[i+j]+hi[a][j])
		}
		for i, j := b-1, 0; j < li[a]; j++ {
			h[i+j] = mx + end[a][j]
		}
	}
	for _, v := range h {
		Fprint(out, v, " ")
	}
	Fprintln(out)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
