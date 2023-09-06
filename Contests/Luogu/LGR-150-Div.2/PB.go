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

	var n, q, k int
	Fscan(in, &n, &q)
	a := make([]int, n*n)
	for i := range a {
		Fscan(in, &a[i])
	}
	sort.Ints(a)
	a = a[(n-1)*n:]
	for ; q > 0; q-- {
		Fscan(in, &k)
		j := sort.SearchInts(a, k)
		Fprintln(out, n-j)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
