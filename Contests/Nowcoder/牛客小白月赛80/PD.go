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

	var n, m, k, x int
	Fscan(in, &n, &m, &k)
	a := make([]int, m)
	for i := 0; i < n; i++ {
		Fscan(in, &x)
		a[x-1]++
	}
	for i := 0; i < m; i++ {
		if k+a[i] > n {
			Fprint(out, -1, " ")
		} else {
			Fprint(out, (n-k-a[i]+m-2)/(m-1), " ")
		}
	}

	Fprintln(out)
}

func main() { solve(os.Stdin, os.Stdout) }
