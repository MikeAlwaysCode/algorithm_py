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

	var n, q, l, r, x int
	Fscan(in, &n)
	pos := make([][]int, n+1)
	for i := 1; i <= n; i++ {
		Fscan(in, &x)
		pos[x] = append(pos[x], i)
	}
	for Fscan(in, &q); q > 0; q-- {
		Fscan(in, &l, &r, &x)
		Fprintln(out, sort.SearchInts(pos[x], r+1)-sort.SearchInts(pos[x], l))
	}
}

func main() { solve(os.Stdin, os.Stdout) }
