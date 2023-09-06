package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, k, a, b int
	Fscan(in, &n, &k)
	s := make([]int, n)
	d := make([]int, n)

	for i := range s {
		Fscan(in, &a, &b)
		s[i] = a*7 + b*2
		d[i] = s[i]
	}
	sort.Ints(d)

	for _, v := range s {
		if v+100 >= d[n-k] {
			Fprintln(out, "Yes")
		} else {
			Fprintln(out, "No")
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
