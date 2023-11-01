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

	var n, m, k, x int
	Fscan(in, &n, &m, &k)
	a := make([]int, m)
	for i := 0; i < n; i++ {
		Fscan(in, &x)
		a[x-1]++
	}
	sort.Ints(a)
	s := 0
	for i := 0; i < m-1; i++ {
		s += a[i]
	}
	if k <= s {
		Fprintln(out, a[m-1])
	} else {
		Fprintln(out, n-k)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
