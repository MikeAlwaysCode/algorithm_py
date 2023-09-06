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

	var T int
	var a, b, l, r int64
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &a, &b, &l, &r)
		x := b - a
		mn := (x + r - 1) / r
		if mn*l > x {
			Fprintln(out, -1)
			continue
		}
		mx := x / l
		if mx*r < x {
			Fprintln(out, -1)
			continue
		}
		Fprintln(out, mn, mx)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
