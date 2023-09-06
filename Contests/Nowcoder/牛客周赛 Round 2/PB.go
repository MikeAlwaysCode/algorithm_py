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
	var s string
	Fscan(in, &s)

	p, pp, cur := 0, 0, 0
	for i := 1; i < n; i++ {
		cur = p
		if s[i] != s[i-1] {
			cur = max(cur, pp+a[i]+a[i-1])
		}
		pp, p = p, cur
	}
	Fprintln(out, cur)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
