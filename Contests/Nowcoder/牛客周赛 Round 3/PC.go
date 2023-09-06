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

	var n, m, a, b int
	Fscan(in, &n, &m, &a, &b)

	ans := 0
	r1 := n / 2
	if r1 > m {
		r1 = m
	}
	for x := 0; x <= r1; x++ {
		v1 := x * a
		v2 := min(n-2*x, (m-x)/2) * b
		ans = max(ans, v1+v2)
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
