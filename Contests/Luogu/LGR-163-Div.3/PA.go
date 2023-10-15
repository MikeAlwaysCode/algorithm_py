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

	var n, t int
	Fscan(in, &n)
	a := make([]int, n)
	b := make([]int, n)
	s := 0
	for i := range a {
		Fscan(in, &a[i], &b[i])
		s += b[i] * 100 / a[i]
	}
	Fscan(in, &t)
	if s >= t {
		Fprintln(out, "Already Au.")
		return
	}
	for i := 0; i < n; i++ {
		if (a[i]-b[i])*100/a[i] < t-s {
			Fprintln(out, "NaN")
			continue
		} else {
			p := 100 / a[i]
			Fprintln(out, (t-s+p-1)/p)
		}

	}
}

func main() { solve(os.Stdin, os.Stdout) }
