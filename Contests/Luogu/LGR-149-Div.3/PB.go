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

	var n, a, l, r int
	Fscan(in, &n)
	for i := 1; i <= n; i++ {
		Fscan(in, &a)
		if a == 1 {
			if l == 0 {
				l = i
			}
			r = i
		}
	}
	if l > 0 {
		Fprintln(out, r-l+1)
	} else {
		Fprintln(out, 0)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
